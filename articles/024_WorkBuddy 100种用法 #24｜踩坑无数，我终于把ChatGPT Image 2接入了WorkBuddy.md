# WorkBuddy 100种用法 #24｜踩坑无数，我终于把ChatGPT Image 2接入了WorkBuddy

- 合集序号：24
- 公众号：我与ai的那些事
- 发布日期：2026-04-24
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328379&idx=1&sn=0d7d423fcdd4d7b3541f70c0d019e95b&chksm=8830307cbf47b96a312b90c1e2584133822f706881514dffeb07889ad29b1babdbce700233d0#rd
- 正文字数：2269
- 正文图片：9

## 摘要

WorkBuddy 100 种用法第 24 篇，实测 ChatGPT Image 2 接入踩坑要点，手把手教你完成 API 调用与 Skill 封装，快速打造可复用 AI 绘图工具

## 正文

最近ChatGPT Image 2特别火，网上一大堆教程教你怎么调用。我正好想把AI绘图能力接到WorkBuddy里，就跟着教程试了一遍。结果踩了一路坑。

网上的教程我试了好几个，发现一个共同问题：他们大多没真正跑通过，代码是拼凑的，步骤是缺失的。 你按他们的流程走，大概率卡在半路，还不知道怎么解决。

我把自己完整踩过的四个坑记下来，帮你直接省时间：

坑一：先创建API Key

很多人以为注册OpenAI账号就能直接调用API，其实不是。你必须先到OpenAI后台的API Keys页面，手动创建一个API Key。没有Key，代码写得再对也调不通。创建的时候记得复制保存，这个Key只显示一次，刷新页面就没了。

坑二：账号必须先绑卡，再充值

调用Image 2 API不是免费试用的。但很多人不知道的是，不是直接就能充值——你的OpenAI账号必须先绑定一张信用卡或借记卡，完成绑卡后，才能往账户里充值。余额里至少要有10美元，接口才会正常响应。没绑卡、没充值的话，接口直接报额度不足。很多教程压根没提这一步，让你以为代码写错了。

坑三：接口调用一直报“未验证”

我按文档写好代码调接口，结果返回的错误是“organization not verified”（组织未验证）。查了才发现，调用Image 2这个模型，账号必须完成身份认证。不是普通的邮箱验证，是要在OpenAI后台提交个人或开发者身份认证，也就是KYC。

坑四：KYC认证等审核

提交认证资料后不是立即生效的，要等审核通过。审核期间你调接口永远报权限错误，很多人到这里就以为代码写错了，其实是账号状态没通过。

这四个坑我逐个踩完，API终于调通了。下面这张图就是我测试时生成的——一只戴着宇航员头盔的橘猫坐在火星上，效果确实不错。

能正常出图了，但问题也来了——每次想用的时候都要翻代码、改参数、重新跑脚本，太麻烦。更关键的是，如果我想把这个能力分享给朋友用，他们还得懂Python、会配环境，门槛太高。

我想的是：能不能像安装一个App一样，别人拿到就能用？

这就是今天要讲的主题：把API调用封装成一个通用的WorkBuddy Skill。

从一段脚本到一个Skill

WorkBuddy的Skill机制其实就是一个标准化的目录结构，加上一个主程序和一个说明文档。我把验证通过的API调用代码，按照Skill的规范重新组织，它就变成了一个可安装、可配置、可复用的组件。

整个封装过程分为三步：

第一步：设计命令行接口

参数设计是关键。我最终确定了这套参数体系：

-
• prompt（必填）：图片描述，支持中文

-
• --api-key：API Key，三种方式传入

-
• --size：图片尺寸，支持三种比例

-
• --quality：生成质量，low/medium/high三档

-
• --n：批量生成数量

-
• --background：是否透明背景

-
• --output-dir：输出目录

-
• --output-name：自定义文件名

第二步：实现配置优先级

为了让这个Skill真正通用，API Key的设置必须灵活。我设计了三级优先级：

-
1. 命令行参数（最高优先级，适合临时调用）

-
2. 配置文件（适合个人长期使用）

-
3. 环境变量（适合服务器部署）

无论你在什么场景下使用，都能找到合适的配置方式。

第三步：写一份给别人看的文档

一个Skill能不能被他人使用，文档占一半。我写了完整的README，包含：

-
• 安装依赖

-
• 三种API Key配置方式的详细步骤

-
• 从简单到复杂的6个使用示例

-
• Python代码调用示例

-
• 完整的参数说明表

-
• 常见问题解答

-
• 质量与价格参考

Skill的文件结构

封装完成后，整个Skill的目录结构非常清晰：

gpt-image/
├── README.md # 完整使用文档
├── SKILL.md # WorkBuddy识别配置
├── config.example.txt # 配置文件模板
├── scripts/
│ └── generate_image.py # 主程序
└── references/ # API参考文档

用户只需要安装依赖、设置API Key，然后一行命令就能生成图片：

python3 generate_image.py "一只戴着宇航员头盔的橘猫坐在火星上" --quality high --n 3

让工具真正流动起来

这次封装让我意识到：写代码只是第一步，让代码变成别人能用的工具，才是价值放大的关键。

WorkBuddy的Skill机制提供了一套标准化的封装规范，你只需要：

-
1. 把核心逻辑写成一个带参数的命令行脚本

-
2. 写一个README告诉别人怎么用

-
3. 按照目录结构放好文件

三步下来，一段个人脚本就变成了一个可分享的组件。

写在最后

从调通API到封装成Skill，本质上是一个从“能用”到“好用”再到“别人也能用”的过程。网上教程多，但真跑通的少。如果你也在折腾Image 2，希望我踩过的这四个坑能帮到你。

如果你也有一些常用的API调用脚本，不妨按照这个思路封装成Skill，既方便自己，也能帮到别人。

这是「WorkBuddy 100种用法」系列第24篇，前面23篇已经覆盖了很多实用场景，如果你刚关注，可以翻一翻历史文章。想要本文封装好的GPT Image 2 Skill，关注公众号后回复「ChatGPTImage2」，我会把完整代码和使用说明发给你。

本期互动

你有没有被网上教程坑过的经历？或者想封装什么API？欢迎在评论区聊聊。

#WorkBuddy #AI工具 #效率提升 #ChatGPT #GPTImage #API踩坑 #KYC认证 #自动化脚本 #开发者工具 #开源分享

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNFktbyibSiawvhUQJk7bcXNvZ5TTroLR1CPDDKK2IdPoiaXY3Vz2ZncqIsPxEIOg9rezrswMtibJI99kCvQ1U1v2sypibMvicXMTkDw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPhibMXQCgZfhic0jlrdQcSY02wia9J7rqNfqN0DpP2RntD0OLHGRfhSPGtLfgMDhlggTJNbKBN5H1RuOkcyHCsJJxWT9km44Cwag/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRMt9fWnHnWn3ZPy77hLicOU2nlKWsBLMWOp1gYcAldFAChNLTqsoccgWOLRLCOWwicDtX1y2VTtYoQBM6ia1wPzfFSO69SEOAicRbk/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROgIoupwbAyvkvtm5w1T9rjXeI5eO7seOJrKWyaDSXibuGK03j3WZHYlV7ib8AkSFgWaVOchGyjkJ5pVia3RKneGXnZIS7UZZJhFw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRO9CCNlvwib701lehft1ITAvhrcNOdqnqoiaiaBPkrPXCvHNxsUOMutSLicrRdlIGcSW74NUgVlRdfE2RtZViasoo8F21RHRxibwfDes/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRNPtZhO3vDWxALiaRWrYn0aOuLILOCWerbdYpMibmomBSDTuaCwNIsX23pg45pr1gCZUdibWpc86LGC84QZPxYGuG6lu9D9xyz19o/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP3aCRBCHA8bbbNtR90kicXXwmZkZQGtBjT8dTGCHKjFWQMSz67MhqcNkF6UWLJrnqxAyFGqpxFHDYTiamg9uJV7jnJYvK6kNkS0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNJXmV9cbDOu1ozGofEKBGmibsSpGpXDibWwrLVgx9hn78UUeNBSibKevyJvYzgyOBC7BSgpbRyqhTYnvdAKgR4663xwGY2ITtLicM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP7I3wy8ic1jiciaPXc8riazUbUkicNCKH81oLolBQNHWuMVD2KLtFTdCqo5TwJjvOVfCwtw8afC47gYxxR7JtL0Arv2lA9spPIXIe8/640?wx_fmt=png&from=appmsg
