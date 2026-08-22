# WorkBuddy 100种用法 #52 | 一个人怎么变成一支团队？多Agent模式完全指南

- 合集序号：52
- 公众号：我与ai的那些事
- 发布日期：2026-05-22
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329091&idx=1&sn=cc59c4f102c9932a977e52f2d753dc94&chksm=88303344bf47ba5239b2cbc7c9cd0fcf6491ce42b080c56e5c7cd34860b6c7dc413b1dd1541e#rd
- 正文字数：2612
- 正文图片：6

## 摘要

WorkBuddy内置三种多Agent模式——自动子Agent、并行子Agent和Team团队协作，一个人就能变成一支团队。本文用两个实操案例，手把手教你触发和使用。

## 正文

"WorkBuddy 有多 Agent 模式吗？多agent怎么分角色？"

早上社群里有人问了这个问题。并让出个具体案例。

我看了觉得——这个问题确实值得单独写一篇。因为多 Agent 可能是 WorkBuddy 里最被大家忽略的能力。好多人用了很久都不知道，自己其实已经用过了。

所以这篇不搞教学大纲，就当聊天，把我自己摸索出来的东西分享下。

先说结论：你可能已经在用了

对，你没看错。

你在 WorkBuddy 里说"帮我看看这个项目结构"的时候，背后不只是"一个 AI"在回答你。实际上它会自动派一个小助手（子 Agent）去扫描文件、搜索关键词、理解逻辑，最后把结果汇总回来告诉你。

整个过程你是无感的。你只看到回复变快了、内容更详细了。

这就是多 Agent 的第一种用法——自动子 Agent。不需要你做任何操作，WorkBuddy 自己判断什么时候需要"叫人帮忙"。

具体来说，自动子 Agent 有这几种"小助手"：

子 Agent 类型

擅长干什么

你会感觉到的

Explore

快速扫描项目结构、搜索关键词、理解代码逻辑

回复特别快，直接给了你文件列表或搜索结果

Plan

和 Explore 类似，但能力更强，能做更复杂的分析

拿到的分析结果比平时更深入

general-purpose

通用型，什么都能帮忙干

复杂任务突然被拆成了几步并行完成

Fork

复制一份你的完整对话上下文，带着记忆去干活

好像"另一个你"在帮你做事，因为它记得前面聊的所有内容

最常见的是 Explore——你说"帮我看看这个项目"，它就会派一个 Explore 子 Agent 去扫描文件、搜代码。整个过程你是无感的，只觉得回复变快了、内容更详细了。

但如果你想让多 Agent 发挥更大作用，得主动一点。接下来是我自己试出来的两种方式。

我怎么知道它在用多 Agent？

说实话，刚开始我也不确定。后来试多了，总结出几个能感知到的信号：

-
速度明显变快了——以前一句话得等半分钟的，几秒就回来了，因为背后好几个在同时跑

-
回复分了好几段——有时候你会看到一个回复里出现了不同角度的内容，像是几个人分别写的最后拼在一起

-
工具面板里出现了不同的 Agent 名称——如果你留意右侧的工具调用记录，会看到类似 "Explore"、"general-purpose" 这样的标签，说明这是不同子 Agent 在干活

-
Fork 模式最明显——因为它继承了你的完整对话上下文，回复里会表现出"它记得我们刚才聊过什么"的感觉

所以如果你好奇"这到底是单 Agent 还是多 Agent 在工作"，看一眼工具面板就知道了。

方式一：一句话让 AI 同时干两件事

有天我要准备一篇公众号文章，需要同时做两件事：查资料和写草稿。

以前我会先让它查资料，等结果回来，再让它写草稿。前后得等两轮。

后来我试了换个说法：

帮我同时做两件事：1）搜一下 2026 年最热门的 3 个 AI 记账 App，列出特色功能；2）帮我写一个 HTML 页面，做一个简单的记账表单

就多了"同时"两个字。

然后我发现——它真的同时做了。两个子 Agent 各干各的，一个去搜竞品，一个去写代码，最后两份结果几乎一起返回给我。

所以这个方式特别简单，记住一个关键词就行：同时。或者用"并行"也行。

适合什么场景？几个互相不依赖的小任务，想快点拿结果的时候。

我后来常用这种方式：同时翻译一份文档 + 同时做数据表格，省下来的时间是真的香。

方式二：创建一个"虚拟团队"

这个方式我一开始觉得挺玄的，试了之后才发现是真好使。

起因是我要做一个项目：调研 AI 工具排行榜，然后根据调研结果写文章，最后检查一遍有没有问题。

三件事，三种不同的能力。我试着这样跟 WorkBuddy 说：

帮我创建一个团队，3 个角色：

1. 调研员：搜索「2026年最受欢迎的AI工具排行榜」，整理成表格
2. 写手：根据调研结果写一篇 1000 字的公众号文章草稿
3. 审查员：检查文章有没有错别字和逻辑问题

三个人同时开工，最后汇总给我。

然后我看着工具调用面板，真的出现了三个不同的 Agent 在同时工作——一个在搜索网页，一个在写文件，一个在读文件。

最后给我交了一份表格、一篇草稿、还有审查意见。比我自己一件一件做快了至少一半。

这里有个细节值得一提：三个角色是有不同权限的。调研员只能搜索和读网页，写手能写文件和执行命令，审查员只能读文件不能改。这样各司其职，不会互相踩。

这种"角色定位 + 权限隔离"是 Team 模式和普通并行最大的区别。并行子 Agent 是几个能力相同的小助手同时干活，而 Team 模式是不同专业的人做不同的事，像真正的团队分工一样。

Team 模式怎么触发？

上面那个案例是最直接的方式——你明确说"创建一个团队"。但其实还有几种触发方式：

触发方式

举个例子

适合场景

直接说"创建团队"

"帮我创建一个团队，一个调研一个写码"

你已经很清楚要怎么分工

给一个复杂的多任务列表

"第一步调研竞品，第二步写代码，第三步做测试"

任务多且明确，让 WorkBuddy 自己判断怎么拆

自然语言描述角色分工

"我需要一个调研的、一个写代码的、一个检查的"

你想用人话表达，不想学格式

我自己用下来，最推荐第三种——因为最自然，你不需要记任何格式，直接说"谁负责什么"就行。

怎么判断该不该用多 Agent？

试了几次之后，我总结了一个简单的判断标准：

能同时干的，就同时干。干不了同时的，就别硬拆。

具体来说——

适合多 Agent

不适合多 Agent

几件事互相不依赖，谁先干都行

B 必须等 A 做完才能开始

任务类型差别大（一个搜索一个写码）

同一个任务的多个步骤

工作量不小，并行能明显提速

简单问答或小修改

举个例子：你要"先查资料，再根据资料写方案"——这种情况就不适合并行，因为写方案必须等查完资料。但如果你要"查 A 领域的资料 + 查 B 领域的资料"——这两个就可以并行。

划重点

折腾了这么多，其实新手只需要记住三句话：

-
"帮我同时做 A 和 B" → 触发并行子 Agent

-
"创建一个团队，一个负责调研，一个负责写代码" → 触发 Team 模式

-
其他时候正常说话就行 → WorkBuddy 会自动判断要不要用子 Agent

不用记技术名词，不用学配置。像跟一个团队对话一样说话，就可以了。

多 Agent 的本质就这么朴素：把一个人的活，分给多个"小助手"同时干。 你只需要说清楚要什么、哪些事可以同时做。剩下的事，WorkBuddy 替你搞定。

一个人，确实可以变成一支团队。

这是WorkBuddy 100 种用法第51篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNqPY0UqSgCU2rJ3TXxruB9B7iaLEh1j5KGS4iaJibbwZBuqaPJs85DJQiaTL2uEe2WxhB4KfdwvhibyGPaktAguiaicQ50eyGvpBJngo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPSsL1qHK1wxSerm8QstOWD3uav9EEiay2JIaNtm1SewEID8WajOiacm4jvlbKhd8UgmBChnFAwr6wriblw8AaTH5t6Hia5pMFtek8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPDJThOVIWgx6bZ1d4bWXRIACNYGyib4zTcWbTmibEbFmk5YWwRibmunx2NRRia0lgZYKx9icav2lYNic4l6LBTBBHPVicUXzwxxvSLEE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPtyWaOOkzfs51BecgC6oaM9mh41TPEGibveAhVaLYkCicSRg55pdI5AooqmdiabqrD6SDD5f1NB2YNAAcpJ6o27D156zHalBkicws/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPbxNuibsVO8UV3emRyzW3gJ5Lq3gSkXdLqLAyLiaWesmibSI81qhOVmcMy0QcibaUT0j3aX0dEj4BzvuzdHRxXWHM0P1jV7YYtiahs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROWcicaX3kdlv3txP1RtddFT4Sic9bI1BnRF7TKUrJyK3ibIXnBguomxBoap9X7lHkicgFWKZw6ndJsIicYhVGMGgpyWzjia21LnrpBw/640?wx_fmt=png&from=appmsg
