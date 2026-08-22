# WorkBuddy 100种用法 #68 | 让AI帮你发小红书，全程不到10分钟

- 合集序号：68
- 公众号：我与ai的那些事
- 发布日期：2026-06-07
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329405&idx=1&sn=2f34ee82ed6a4f863467e96f8d93d68d&chksm=8830347abf47bd6cc480e81c39556556f3a0cad352310cabc15f2685764eb1de94e79c682fa0#rd
- 正文字数：2540
- 正文图片：13

## 摘要

你能帮我发小红书吗?到笔记成功发布，不到10分钟。安装MCP连接器、生成内容、AI配图、一键发布，全流程自动化。\x0d\x0aWorkBuddy 1

## 正文

今天早上，我打开 WorkBuddy，问了一句：

你能帮我发小红书吗？

就这么简单一句话，开启了一段让我自己都没想到的旅程。

从查资料、安装配置、到内容生成、AI配图、最终发布——全程不到10分钟。

第一步：先回答"能不能"

他的第一反应是检查自己有哪些能力：

-
内容生成 ✅ — 我已安装两个小红书内容生成技能（xhs-content-gen、xiaohongshu-writer-expert），可以生成标题、正文、标签

-
直接发布 ❌ — 没有小红书的 MCP 连接器，无法直接操作平台

结论：能生成内容，但不能发布。

我不太相信，让他去 GitHub搜索，看有没有现成的方案。

第二步：GitHub 找到宝藏项目

搜索 GitHub 后，找到了 3 个主要项目，并做了对比：

项目

Stars

语言

支持发布

搜索/互动

状态

xiaohongshu-mcp

14k
⭐

Go+Python

✅ 图文+视频

✅ 全功能

🟢 活跃

xhs-mcp

—

Node.js

✅ 图文+视频

✅ 基本功能

🟢 活跃

RedNote-MCP

1.1k ⭐

TypeScript

❌ 只读

✅ 搜索/评论

🔴 停更

毫不犹豫选择了 xiaohongshu-mcp：14k Stars、功能最全、最近还在更新。

💡 提示：项目地址：https://github.com/xpzouying/xiaohongshu-mcp[1]

第三步：安装配置（全自动）

确定方案后，让他给我安装：

① 下载二进制文件

# macOS x86_64 版本
curl -L -o xiaohongshu-mcp-darwin-amd64.tar.gz \
"https://github.com/xpzouying/xiaohongshu-mcp/releases/download/v2026.05.28.0902-17500db/xiaohongshu-mcp-darwin-amd64.tar.gz"
tar -xzf xiaohongshu-mcp-darwin-amd64.tar.gz
chmod +x xiaohongshu-mcp-darwin-amd64 xiaohongshu-login-darwin-amd64

这里有个小插曲：他一开始下载了 ARM64 版本，发现我的 Mac 是 x86_64 架构，自动切换到了正确的 AMD64 版本。这就是 AI 主动排查错误的能力——不需要你指出问题，他自己发现、自己修复。

② 配置 MCP 连接

{
"xiaohongshu-mcp": {
"url": "http://localhost:18060/mcp",
"type": "streamablehttp",
"disabled": false
}
}

写入 ~/.workbuddy/mcp.json，一个 JSON 配置项搞定。

③ 扫码登录

运行登录工具，弹出浏览器窗口，用小红书 App 扫码。Cookie 自动保存，下次不用重复登录。

⚠️ 注意：小红书不允许同一账号在多个网页同时登录。如果你用 MCP 登录了，就不要在其他网页端登录同一个账号（手机 App 不受影响）。

④ 启动 MCP 服务器

nohup ./xiaohongshu-mcp-darwin-amd64 > /tmp/xhs-mcp.log 2>&1 &

服务器跑在 localhost:18060，注册了 13 个 MCP 工具：

类别

工具

📤 发布

publish_content、publish_with_video

🔍 发现

list_feeds、search_feeds、get_feed_detail

💬 互动

post_comment、reply_comment、like_feed、favorite_feed

👤 用户

user_profile

🔐 账号

check_login_status、get_login_qrcode、delete_cookies

第四步：信任连接器，验证成功

安装完成后，在 WorkBuddy 的连接器页面找到 xiaohongshu-mcp，点击「信任」。

信任后立即验证：

✅ 已登录
用户名: xiaohongshu-mcp

13 个小红书工具全部可用！

第五步：一键生成内容 + AI 配图 + 发布

用户说了一句话："帮我发一条小红书图文笔记，主题为 WorkBuddy 使用心得，图片使用即梦生成，无水印。然后发布。"

AI 开始全自动处理：

生成内容

以10年老程序员视角撰写，标题 "用AI写代码是什么体验？WorkBuddy使用心得"，4个核心卖点，结尾引导互动。

即梦AI配图（无水印）

使用即梦图片生成4.0，生成了 3 张 1080×1440 的配图：

图片

描述

封面图

AI助手与人类协作场景，扁平插画风

功能展示

AI工具界面特写，多面板布局

氛围图

居家办公场景，温馨治愈风格

发布成功

调用 publish_content 工具，一键发布：

内容发布成功
标题: 用AI写代码是什么体验？WorkBuddy使用心得
图片: 3张
状态: 发布完成

手机端查看效果：

回顾整个流程

从第一句对话到笔记上线，整个过程：

"你能帮我发小红书吗？"
↓
搜索 GitHub → 找到 14k Star 项目
↓
下载安装 → 配置 MCP → 扫码登录
↓
生成内容 → 即梦配图 → 一键发布
↓
✅ 发布成功

全程不到10分钟。

最关键的3点：

-
MCP 连接器是核心 — 它让 AI 直接操作小红书平台，从"只能生成内容"变成"能完整发布"

-
AI 主动排查问题 — 下载错架构？自动发现自动修复。用户全程不用操心技术细节

-
全链路自动化 — 内容生成 → 图片生成 → 发布，一句话搞定

你能学到什么

-
MCP 连接器的力量：学会利用开源 MCP 项目扩展 AI 能力边界

-
AI 不是被动执行：好的 AI 助手会主动搜索、对比、选择最佳方案

-
自动化思维：从"帮我写内容"进化到"帮我完成整个发布流程"

相关工具

工具

链接

用途

xiaohongshu-mcp

GitHub[2]

小红书 MCP 连接器

即梦AI

火山引擎

AI 图片生成（无水印）

WorkBuddy

官网[3]

AI 编程助手

这是WorkBuddy 100种用法第68篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

引用链接

[1]https://github.com/xpzouying/xiaohongshu-mcp

[2]GitHub: https://github.com/xpzouying/xiaohongshu-mcp

[3]官网: https://www.workbuddy.ai

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM3dwPQ0S44zrLUAy5on7hKyzQn87vaHgaEI3TPKdVy0ZqS7Ee2NQyibqCBYK89L84iaPl8iaicPNic5yqXDzlFRW1KvRnDq9icx3t80/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMK9JIKicMPnsLpWwytEES8d6FGLEcoYAPfFicwwFzShxXG7Yq2ia1VicyOz1a5icicgyaxBMqjFsQK8GKlUY3iaviaql5UHvzMJmPmJ78/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMFvVl5vHtLKuvpktaURgTGUdZOIl14UHjOTqZabpmFOzXDNBlD3D5kBiaYm0M9ePtNQCgooHh0RRYwpnrhh6tiaIBN6noEba3U8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMV8GSvfsxiajbshIcD75nhlOicibFkjh8hokwNQK3AIibuhGtd8wibUgN3ENKBDDtf6tW3bC1RIJxwhC9Kp9Lom5CJnzHRrVia8x1aA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROxn7Sl5jGkAI16N3MwLicVicIdGoCYHyGliaEPLFm2uVl0r4LBM3icwmPiaakusj3FfGB5W2KSlI2kHSibwypfYVGia1E740MWibRDEws/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROjaV76rPToxmsicJcDu1kYOSLUrA4AU9AYcYYIbEY2qx1RrNleWXXhzePricw6Y4LibVBNpaEocIIZLSricP2uCmdtnfStic7EsMfM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROdick0DP49eUXDSf0qNc4QhAyPhickqOdJma7gIibVvKq1DuaiaAZfyUAxS9eiaAUncjnKTMfP18N7aNT6G5IGRLxwBFQepz1gTtdU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROL82MwX3vrEpjGURY6J9XqQVsoia2VciaAw5xVrxynibn0ZK4PXHEh8pNCxPYsBewadLPslURmPgNfMzJQzCYKTvGUbV07b3U2L4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMibIHFy7Nicv0PLDHVtP8C37WXabo5NoVUZalicsw8PysczibXcGDIc4leL4leN6FubPibIS6yvViczsia5nPXUXwibKPsZic5upkj2pOA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP3FjIGURHOlyOBzrsIib0YE0XzHjLbxVX2hEstoApJiaZ8iaiaiaJfy2Zq7891gq5UQaddzcawmZRUsrKJq1pTOtIPMHmniciafBfFic8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMV118YeY3e4laVVicCBcz6qX3ph00qyy03qia7c9LoficuJxiccPgZlQWxkUMClGLhXtmbRxwHtV3eLMXfCd0DPJmTDRMxmJUleJA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO681XyoXsbjdST46QFzV4xrdXvGZ38TgVxKicwe4KYuKuQ7eiaJXJzYyWxwFYzkBGOrx88UIrGeUv7T0dc3FnViajBrgJLtrAlP8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRNzdwyUlaib0pCmNibluMS1YLu0hhYQ7ovYibYQQoPrKLvewTxDLeosPxSVicd6cibKWkNMPibGXBL2wg2vmEdscaP5JIzQnicDSLFPc8/640?wx_fmt=jpeg&from=appmsg
