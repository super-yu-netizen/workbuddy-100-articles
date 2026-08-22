#!/usr/bin/env python3
"""Archive a public WeChat album and extract searchable article text.

This script only uses Python's standard library so it can run in a clean local
environment. It saves the source HTML as well as cleaned text and indexes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import random
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ALBUM_URL = (
    "https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum"
    "&__biz=MzA4OTE4MjYzMg%3D%3D&scene=1"
    "&album_id=4449024189949444100&count=3"
)
ALBUM_ID = "4449024189949444100"
BIZ = "MzA4OTE4MjYzMg=="
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 Chrome/124.0 Safari/537.36 MicroMessenger/8.0.50"
)
BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "div", "dl", "dt", "dd",
    "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3",
    "h4", "h5", "h6", "header", "hr", "li", "main", "nav", "ol", "p",
    "pre", "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
}


def fetch(url: str, *, referer: str | None = None, retries: int = 4) -> bytes:
    headers = {
        "User-Agent": UA,
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.7",
        "Accept-Encoding": "identity",
    }
    if referer:
        headers["Referer"] = referer
    if "f=json" in url:
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last_error = exc
            time.sleep((1.5 ** attempt) + random.random())
    raise RuntimeError(f"fetch failed after {retries} attempts: {url}") from last_error


def normalize_url(value: str) -> str:
    value = html.unescape(value.strip())
    if value.startswith("http://mp.weixin.qq.com"):
        value = "https://mp.weixin.qq.com" + value[len("http://mp.weixin.qq.com"):]
    elif value.startswith("//"):
        value = "https:" + value
    return value


def safe_filename(value: str, limit: int = 72) -> str:
    value = re.sub(r"[\\/:*?\"<>|\x00-\x1f]", "_", value)
    value = re.sub(r"\s+", " ", value).strip(" ._")
    return value[:limit] or "untitled"


def clean_text(parts: list[str]) -> str:
    text = html.unescape("".join(parts)).replace("\u200b", "").replace("\xa0", " ")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


@dataclass
class AlbumArticle:
    position: int
    title: str
    url: str
    msgid: str
    itemidx: str
    create_time: str
    cover_url: str


class InitialAlbumParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "li":
            return
        data = {key: (value or "") for key, value in attrs}
        classes = set(data.get("class", "").split())
        if "js_album_item" in classes:
            self.items.append(data)


class ArticleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, str]] = []
        self.capture_kind: str | None = None
        self.capture_depth = 0
        self.title_parts: list[str] = []
        self.author_parts: list[str] = []
        self.body_parts: list[str] = []
        self.images: list[str] = []
        self.description = ""
        self.og_image = ""
        self.canonical = ""
        self.ignore_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: (value or "") for key, value in attrs}
        element_id = data.get("id", "")
        self.stack.append((tag, element_id))
        if tag in {"script", "style", "noscript"} and self.capture_kind == "body":
            self.ignore_depth += 1
        if self.capture_kind is None and element_id in {"activity-name", "js_name", "js_content"}:
            self.capture_kind = {
                "activity-name": "title",
                "js_name": "author",
                "js_content": "body",
            }[element_id]
            self.capture_depth = len(self.stack)

        if tag == "meta":
            prop = data.get("property", "") or data.get("name", "")
            content = data.get("content", "")
            if prop in {"og:description", "description"} and content and not self.description:
                self.description = clean_text([content])
            elif prop == "og:image" and content and not self.og_image:
                self.og_image = normalize_url(content)
        elif tag == "link" and data.get("rel") == "canonical":
            self.canonical = normalize_url(data.get("href", ""))

        if self.capture_kind == "body" and not self.ignore_depth:
            if tag in BLOCK_TAGS:
                self.body_parts.append("\n")
                if tag == "li":
                    self.body_parts.append("- ")
            elif tag == "br":
                self.body_parts.append("\n")
            elif tag == "img":
                source = data.get("data-src") or data.get("data-original") or data.get("src")
                if source:
                    source = normalize_url(source)
                    if source not in self.images and not source.startswith("data:"):
                        self.images.append(source)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if self.capture_kind == "body" and tag in BLOCK_TAGS and not self.ignore_depth:
            self.body_parts.append("\n")
        if self.capture_kind == "body" and tag in {"script", "style", "noscript"} and self.ignore_depth:
            self.ignore_depth -= 1
        if self.capture_kind is not None and len(self.stack) == self.capture_depth:
            self.capture_kind = None
            self.capture_depth = 0
        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if not data or self.ignore_depth:
            return
        if self.capture_kind == "title":
            self.title_parts.append(data)
        elif self.capture_kind == "author":
            self.author_parts.append(data)
        elif self.capture_kind == "body":
            self.body_parts.append(data)


def parse_album_metadata(source: str) -> dict[str, Any]:
    def grab(pattern: str, default: str = "") -> str:
        match = re.search(pattern, source)
        return html.unescape(match.group(1)) if match else default

    return {
        "title": grab(r"\btitle:\s*'([^']*)'"),
        "description": grab(r"\bdesc:\s*'([^']*)'"),
        "account": grab(r"\bnick_name:\s*'([^']*)'"),
        "article_count": int(grab(r"\barticle_count:\s*'(\d+)'", "0")),
        "read_count": int(grab(r"\bread_count:\s*'(\d+)'", "0")),
    }


def parse_initial_articles(source: str) -> list[AlbumArticle]:
    parser = InitialAlbumParser()
    parser.feed(source)
    times = re.findall(r'class="js_article_create_time album__item-info-item">(\d+)</span>', source)
    covers = re.findall(r'album__item-img" style="background-image: url\(([^)]+)\)', source)
    items: list[AlbumArticle] = []
    for index, data in enumerate(parser.items):
        items.append(AlbumArticle(
            position=index + 1,
            title=data.get("data-title", ""),
            url=normalize_url(data.get("data-link", "")),
            msgid=data.get("data-msgid", ""),
            itemidx=data.get("data-itemidx", "1"),
            create_time=times[index] if index < len(times) else "",
            cover_url=normalize_url(covers[index]) if index < len(covers) else "",
        ))
    return items


def fetch_album_index(root: Path) -> tuple[dict[str, Any], list[AlbumArticle]]:
    source_bytes = fetch(ALBUM_URL)
    source = source_bytes.decode("utf-8", errors="replace")
    (root / "raw" / "album.html").write_bytes(source_bytes)
    metadata = parse_album_metadata(source)
    articles = parse_initial_articles(source)
    if not articles:
        raise RuntimeError("No initial album articles found")

    page_dir = root / "raw" / "album_pages"
    page_no = 1
    continue_flag = 1
    while continue_flag and len(articles) < metadata["article_count"]:
        last = articles[-1]
        params = urllib.parse.urlencode({
            "action": "getalbum",
            "__biz": BIZ,
            "album_id": ALBUM_ID,
            "count": 10,
            "begin_msgid": last.msgid,
            "begin_itemidx": last.itemidx,
            "x5": 0,
            "f": "json",
        })
        url = "https://mp.weixin.qq.com/mp/appmsgalbum?" + params
        payload_bytes = fetch(url, referer=ALBUM_URL)
        (page_dir / f"page_{page_no:02d}.json").write_bytes(payload_bytes)
        payload = json.loads(payload_bytes.decode("utf-8"))
        if payload.get("base_resp", {}).get("ret") != 0:
            raise RuntimeError(f"Album API returned error: {payload}")
        response = payload.get("getalbum_resp", {})
        raw_items = response.get("article_list", [])
        if isinstance(raw_items, dict):
            raw_items = [raw_items]
        seen = {(item.msgid, item.itemidx) for item in articles}
        added = 0
        for raw in raw_items:
            key = (str(raw.get("msgid", "")), str(raw.get("itemidx", "1")))
            if key in seen:
                continue
            articles.append(AlbumArticle(
                position=len(articles) + 1,
                title=html.unescape(raw.get("title", "")),
                url=normalize_url(raw.get("url", "")),
                msgid=key[0],
                itemidx=key[1],
                create_time=str(raw.get("create_time", "")),
                cover_url=normalize_url(raw.get("cover_img_1_1", "")),
            ))
            seen.add(key)
            added += 1
        continue_flag = int(response.get("continue_flag", 0))
        page_no += 1
        if not added:
            break
        time.sleep(0.15 + random.random() * 0.15)
    return metadata, articles


def utc_date(timestamp: str) -> str:
    try:
        return datetime.fromtimestamp(int(timestamp), tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError, OSError):
        return ""


def article_markdown(article: AlbumArticle, parsed: dict[str, Any]) -> str:
    image_lines = "\n".join(f"- {url}" for url in parsed["images"]) or "- 无"
    return (
        f"# {parsed['title'] or article.title}\n\n"
        f"- 合集序号：{article.position}\n"
        f"- 公众号：{parsed['author']}\n"
        f"- 发布日期：{utc_date(article.create_time)}\n"
        f"- 原文链接：{article.url}\n"
        f"- 正文字数：{parsed['char_count']}\n"
        f"- 正文图片：{len(parsed['images'])}\n\n"
        f"## 摘要\n\n{parsed['description']}\n\n"
        f"## 正文\n\n{parsed['body']}\n\n"
        f"## 正文图片链接\n\n{image_lines}\n"
    )


def fetch_one(article: AlbumArticle, root: Path) -> dict[str, Any]:
    result: dict[str, Any] = asdict(article)
    result.update({"status": "failed", "error": "", "title_actual": "", "author": "",
                   "description": "", "body": "", "char_count": 0, "images": [],
                   "image_count": 0, "canonical_url": "", "html_sha256": ""})
    try:
        source_bytes = fetch(article.url, referer=ALBUM_URL, retries=5)
        source = source_bytes.decode("utf-8", errors="replace")
        parser = ArticleParser()
        parser.feed(source)
        title = clean_text(parser.title_parts) or article.title
        author = clean_text(parser.author_parts)
        body = clean_text(parser.body_parts)
        if len(body) < 80:
            flags = "访问过于频繁|环境异常|验证码|内容已被删除|NO_CONTENT"
            detected = re.findall(flags, source)
            raise RuntimeError(f"article body too short ({len(body)} chars); flags={detected}")
        parsed = {
            "title": title,
            "author": author,
            "description": parser.description,
            "body": body,
            "char_count": len(re.sub(r"\s+", "", body)),
            "images": parser.images,
            "canonical_url": parser.canonical or article.url,
        }
        stem = f"{article.position:03d}_{safe_filename(article.title)}"
        raw_path = root / "raw" / "articles" / f"{article.position:03d}.html"
        md_path = root / "articles" / f"{stem}.md"
        raw_path.write_bytes(source_bytes)
        md_path.write_text(article_markdown(article, parsed), encoding="utf-8")
        result.update({
            "status": "ok",
            "title_actual": title,
            "author": author,
            "description": parser.description,
            "body": body,
            "char_count": parsed["char_count"],
            "images": parser.images,
            "image_count": len(parser.images),
            "canonical_url": parsed["canonical_url"],
            "html_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "raw_html_file": str(raw_path.relative_to(root)),
            "markdown_file": str(md_path.relative_to(root)),
        })
    except Exception as exc:  # keep crawl moving and report every failed item
        result["error"] = str(exc)
    return result


def download_cover(article: AlbumArticle, root: Path) -> dict[str, Any]:
    if not article.cover_url:
        return {"position": article.position, "status": "missing", "file": ""}
    try:
        data = fetch(article.cover_url, referer=ALBUM_URL)
        suffix = ".png" if data.startswith(b"\x89PNG") else ".jpg"
        path = root / "covers" / f"{article.position:03d}{suffix}"
        path.write_bytes(data)
        return {"position": article.position, "status": "ok", "file": str(path.relative_to(root))}
    except Exception as exc:
        return {"position": article.position, "status": "failed", "file": "", "error": str(exc)}


def write_outputs(root: Path, metadata: dict[str, Any], articles: list[AlbumArticle],
                  results: list[dict[str, Any]], covers: list[dict[str, Any]]) -> None:
    results.sort(key=lambda item: item["position"])
    covers.sort(key=lambda item: item["position"])
    cover_by_position = {item["position"]: item for item in covers}
    for result in results:
        result["cover_file"] = cover_by_position.get(result["position"], {}).get("file", "")

    (root / "album_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "article_index.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (root / "article_full.jsonl").open("w", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")

    csv_fields = [
        "position", "title", "title_actual", "status", "create_time", "publish_date",
        "author", "char_count", "image_count", "url", "cover_url", "cover_file",
        "markdown_file", "raw_html_file", "description", "error",
    ]
    with (root / "article_index.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        for result in results:
            row = dict(result)
            row["publish_date"] = utc_date(str(result.get("create_time", "")))
            writer.writerow(row)

    lines = [
        f"# {metadata.get('title', '微信合集')}：文章目录",
        "",
        f"- 公众号：{metadata.get('account', '')}",
        f"- 合集说明：{metadata.get('description', '')}",
        f"- 合集标注文章数：{metadata.get('article_count', 0)}",
        f"- 本次抓取成功：{sum(1 for item in results if item['status'] == 'ok')}",
        f"- 本次抓取失败：{sum(1 for item in results if item['status'] != 'ok')}",
        f"- 抓取时间：{datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "",
        "| 序号 | 日期 | 标题 | 字数 | 图片 | 状态 |",
        "|---:|:---:|---|---:|---:|:---:|",
    ]
    for item in results:
        title = item.get("title_actual") or item.get("title") or "无标题"
        link = item.get("markdown_file", "")
        title_cell = f"[{title}]({urllib.parse.quote(link)})" if link else title
        lines.append(
            f"| {item['position']} | {utc_date(str(item.get('create_time', '')))} | "
            f"{title_cell} | {item.get('char_count', 0)} | {item.get('image_count', 0)} | "
            f"{item.get('status', '')} |"
        )
    (root / "文章目录.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    report = {
        "album_expected": metadata.get("article_count", 0),
        "album_indexed": len(articles),
        "articles_ok": sum(1 for item in results if item["status"] == "ok"),
        "articles_failed": sum(1 for item in results if item["status"] != "ok"),
        "covers_ok": sum(1 for item in covers if item["status"] == "ok"),
        "total_clean_chars": sum(int(item.get("char_count", 0)) for item in results),
        "total_inline_images": sum(int(item.get("image_count", 0)) for item in results),
        "failed_articles": [
            {"position": item["position"], "title": item["title"], "error": item["error"]}
            for item in results if item["status"] != "ok"
        ],
        "generated_at": datetime.now().astimezone().isoformat(),
    }
    (root / "crawl_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="workbuddy_100_research/archive")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--retry-failed", action="store_true")
    args = parser.parse_args()
    root = Path(args.output).resolve()
    for path in [root / "raw" / "album_pages", root / "raw" / "articles",
                 root / "articles", root / "covers"]:
        path.mkdir(parents=True, exist_ok=True)

    if args.retry_failed:
        metadata = json.loads((root / "album_metadata.json").read_text(encoding="utf-8"))
        previous = json.loads((root / "article_index.json").read_text(encoding="utf-8"))
        articles = [AlbumArticle(
            position=int(item["position"]), title=item["title"], url=item["url"],
            msgid=str(item["msgid"]), itemidx=str(item["itemidx"]),
            create_time=str(item["create_time"]), cover_url=item.get("cover_url", ""),
        ) for item in previous]
        failed_positions = {int(item["position"]) for item in previous if item["status"] != "ok"}
        failed_articles = [item for item in articles if item.position in failed_positions]
        print(f"retrying failed articles: {sorted(failed_positions)}", flush=True)
        replacements = {item.position: fetch_one(item, root) for item in failed_articles}
        results = [replacements.get(int(item["position"]), item) for item in previous]
        covers = [
            {"position": int(item["position"]), "status": "ok" if item.get("cover_file") else "missing",
             "file": item.get("cover_file", "")}
            for item in previous
        ]
        write_outputs(root, metadata, articles, results, covers)
        report = json.loads((root / "crawl_report.json").read_text(encoding="utf-8"))
        print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
        return

    metadata, articles = fetch_album_index(root)
    print(f"album: {metadata.get('title')} | indexed {len(articles)}/{metadata.get('article_count')}", flush=True)

    results: list[dict[str, Any]] = []
    covers: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        article_jobs = {pool.submit(fetch_one, article, root): article.position for article in articles}
        cover_jobs = {pool.submit(download_cover, article, root): article.position for article in articles}
        completed = 0
        for future in as_completed(article_jobs):
            result = future.result()
            results.append(result)
            completed += 1
            if completed % 10 == 0 or result["status"] != "ok":
                print(f"articles: {completed}/{len(articles)} | last #{result['position']} {result['status']}", flush=True)
        for future in as_completed(cover_jobs):
            covers.append(future.result())

    write_outputs(root, metadata, articles, results, covers)
    report = json.loads((root / "crawl_report.json").read_text(encoding="utf-8"))
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
