# WorkBuddy 100种用法 #17｜WorkBuddy空目录一键清理

- 合集序号：17
- 公众号：我与ai的那些事
- 发布日期：2026-04-16
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328256&idx=1&sn=4c6b69ab70e1e009b1581cf92d7992e8&chksm=88303087bf47b9910f122600290ef46494f20075bef46caed483aa6108370775ac01939e9167#rd
- 正文字数：1940
- 正文图片：3

## 摘要

WorkBuddy 运行后产生大量空目录，手动清理麻烦又危险。本文教你用 AI 生成安全脚本，一键清理空目录，不删错、不踩坑，目录瞬间清爽。

## 正文

昨天打开 WorkBuddy 文件夹，里面突然冒出一大堆纯数字时间戳目录，比如 20260323122341、20260415002335 这类名称。

点进去一看，全是空目录！

密密麻麻一堆，强迫症真的忍不了。

关键是：

自动化任务有专门的 automation-claw-* 目录，跟这些垃圾空目录完全两码事。留着没用，手动删又怕删错。

于是我直接丢给 WorkBuddy 一句话：

我目录里全是时间戳空目录，帮我写个安全脚本，只删空的，重要目录别动。

搞笑的是：它一开始还找错目录了😂

我让它直接定位目录，结果它直接给我跑到：

~/.workbuddy/

里面啥也没有。

我当场给它骂了一顿：你给老子好好看看，workBuddy在那个目录！

~/WorkBuddy/

就差一个点，AI也会踩坑。

确认规则：只删空目录，重要目录一律保留

我跟它明确要求：

-
只删空的时间戳目录

-
有内容的目录绝对不动

-
Claw、cover-images、项目目录必须保留

-
automation-claw-* 自动化目录跳过不碰

扫了一遍我这里：68个目录，52个是空的。

AI 确认规则后，直接给我生成了安全脚本。

WorkBuddy 生成的清理脚本

是一个 Python 脚本，功能如下：

-
指定 WorkBuddy 主目录为 ~/WorkBuddy

-
设置白名单目录，不会被删除

-
支持预览模式，不实际删除任何内容

-
支持执行模式，真正删除空目录

-
自动跳过自动化任务目录 automation-claw-*

-
只删除完全为空的目录

#!/usr/bin/env python3
import os
import argparse

# WorkBuddy 正确主目录
WORKBUDDY_DIR = os.path.expanduser("~/WorkBuddy")

# 白名单：需要保留的重要目录
KEEP_DIRS = {
"20260401205421",
"20260402113022",
"20260403162254",
"20260415002514",
"Claw",
"cover-images",
}

def main():
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--dry-run", action="store_true", help="预览模式，不删除")
group.add_argument("--execute", action="store_true", help="执行清理")
args = parser.parse_args()

for item in sorted(os.listdir(WORKBUDDY_DIR)):
path = os.path.join(WORKBUDDY_DIR, item)

# 只处理文件夹
if not os.path.isdir(path):
continue

# 跳过白名单 + 自动化目录
if item in KEEP_DIRS or item.startswith("automation-claw-"):
continue

# 只删空目录
if len(os.listdir(path)) == 0:
print(f"{'✅ 删除' if args.execute else '📋 将删除'}: {item}/")
if args.execute:
os.rmdir(path)

if __name__ == "__main__":
main()

使用方法分为两步：

第一步：先运行预览模式，查看哪些目录会被删除，不执行删除操作。

第二步：确认无误后，再运行执行模式，完成清理。

两步使用，超级安全

1）先预览（不会删任何东西）

运行脚本并传入 --dry-run 参数，查看待删除列表。

python3 cleanup_workbuddy.py --dry-run

2）确认无误，再执行删除

运行脚本并传入 --execute 参数，正式清理空目录。

python3 cleanup_workbuddy.py --execute

核心规则（绝对不会误删）

-
只删 WorkBuddy 产生的空目录

-
跳过重要白名单目录

-
跳过 automation-claw-* 自动化任务目录

-
支持先预览再删除

最后说一句

用 WorkBuddy 越频繁，这类残留空目录就越多。

不用手动删，不用懂代码，直接丢给 AI 说一句：帮我清理空目录，别删错。

10 秒搞定，目录瞬间清爽。

这是「WorkBuddy 100种用法」系列第 17 篇，真实对话、真实踩坑、直接能用。

关注我，持续更新剩下 83 种用法，每天一个实用小技巧。

#WorkBuddy #空目录清理 #文件管理 #效率工具 #Python脚本 #时间戳目录 #自动化办公 #安全清理 #工作流优化 #AI办公

预览时标签不可点

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNoLgMuTibNmV51ac6uuV0x5ba1fC8eYwtAcvXAoY5ia32wRrwQYcPwPrAk6abQsDLhpyDb5zYLGUFwjUo5yibO3hd3QfXoq1bQSs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMDDFlZyEXjiaRmXia6sFjr5CdyoveyXTpwe8uZ0royKcNg0zz6a3Ursg1reJQrrOYGxRpeYHJWlL4ez5D3TxNicYHCI6nNBZboWI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNPrIDATGMzVtkicoSveAtITiaLMIGib6kUMAMxVEA6Wnvug9bougLft9jcTJ0Uxbxiam5wzTINfzepSTSSORviarVVw4nZYVyjClag/640?wx_fmt=png&from=appmsg
