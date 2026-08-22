# WorkBuddy 100种用法 #98 | 发现一个排版更好的Skill，6套主题全试了一遍，排完直接推到公众号草稿箱

- 合集序号：98
- 公众号：我与ai的那些事
- 发布日期：2026-07-07
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330187&idx=1&sn=90eb91394183af2db931022119db778b&chksm=8830370cbf47be1ad6dd7b0f44cc8e62262856867c44ada8135d04f9051f6c56fb0b8bde49b8#rd
- 正文字数：3052
- 正文图片：10

## 摘要

在 GitHub 发现 gzh-design 排版 Skill，6 套主题全试了一遍，再配 baoyu 推送到公众号草稿箱，打通排版推送全链路。

## 正文

TOOL·工具发现与评测

2026.07

排版样式总是那几个来回换？

排版选择 不再

来回换那几个

gzh-design·6套主题·一键排版·草稿箱直达

WorkBuddy 100种用法 #98

公众号排版gzh-design

📦 5 Parts + Conclusion

👉 滑动

PART 01

发现

DISCOVERY

PART 02

安装

INSTALL

PART 03

排版

LAYOUT

PART 04

组合

COMBO

PART ///

写在最后

LAST WORDS

我与AI的那些事·工具发现笔记

排版选择多了，不再是那几个来回换

之前我一直用 wenyan mcp 和 baoyu-post-to-wechat 这两个 Skill 来排版和推送公众号文章。两条路都能走通：wenyan 排版+推送一条龙 ，baoyu 有自己的主题、MD 转 HTML 再推到草稿箱。主题样式够用，但时间长了，就那几个来回换，总觉得 排版少了点新鲜感 。

直到今天在 GitHub 上刷到一个东西。

01

PART

在 GitHub 上发现一个 Skill

DISCOVERY

下午在 GitHub 上刷到一个 Skill： gzh-design 。

我对 WorkBuddy 说：

看下这个skill https://github.com/isjiamu/gzh-design-skill 他有什么作用？

WorkBuddy 看完告诉我，这东西的 核心能力 是：

把 Markdown 自动排版成可以直接粘贴到公众号编辑器的 高质量 HTML ——粘贴后 样式不丢失 。

它自带 6 套主题 ，每套不是配色方案，而是 完整的组件库 ——引言卡片、章节标题、代码块、作者签名，全是经过合规校验的 HTML 片段：

主题

适合什么

摸鱼绿

教程、测评、清单

红白

深度分析、观点

石墨极简

科技评论、专业观点

留白禅意

随笔、极简

摸鱼票据

工具对比、创意评测

橄榄手记

内刊、案例复盘

还有个 主题生成器 ：一句话描述风格，或者给一张参考图，它就能生成一套全新组件库保存下来复用。

排版确实比之前的方案丰富多了。但有个问题—— gzh-design 只排版，不管推送 。它输出的是一段 HTML，你需要手动复制粘贴到公众号编辑器。

要是手动复制粘贴，那跟我之前用 baoyu 直接 MD→HTML→推送的效率比，反而倒退了。

不过我想了下： 排版用 gzh-design，推送用 baoyu，两个拼起来就行了。

02

PART

审查+安装：两句话就搞完了

INSTALL & SECURITY AUDIT

我对 WorkBuddy 说：

装一个试试

但装第三方 Skill 不能直接就装——谁知道里面有没有藏什么？WorkBuddy 自发做了一轮 安全审计 。

它把仓库克隆到临时目录，逐个检查核心文件：

SKILL.md

纯 Markdown 工作流定义，没任何可执行代码。安全。

validate_gzh_html.py

校验脚本，只读 HTML 检查合规性，用标准库，不联网。安全。

component_lint.py

组件库检查，同样只读+标准库。安全。

extract_docx.py

Word 转 Markdown 工具，标准库，只输出本地。安全。

wrap_preview.py

预览页包装器，读模板+替换占位符，标准库。安全。

审查结果： P2（安全） —— 零网络调用 、 零外部依赖 、 零敏感操作 。可以直接装。

WorkBuddy 装到 ~/.workbuddy/skills/gzh-design/ ，清理 .git ，跑了一遍 lint—— 0 ERROR 。

整个过程大概三分钟。我做的事：给链接、说装一个。剩下的全是 WorkBuddy 自己干的—— 克隆、审查、安装、验证 。

03

PART

排版试试：这篇就是用 gzh-design 排的

LIVE LAYOUT TEST

装完了，我说：

使用刚安装的 skill 排下版，我看下效果

WorkBuddy 加载了 gzh-design Skill，读了摸鱼绿组件库，组装完整公众号 HTML，跑合规校验—— 0 ERROR 、 165 处 <span leaf> 包裹 。然后生成了带「复制到公众号」按钮的预览页。

你现在看到的这篇排版，就是 gzh-design 摸鱼绿主题生成的。

排版效果我满意。但我不想手动复制粘贴——直接让 baoyu 推到草稿箱。

04

PART

排版+推送，两个 Skill 拼起来

COMBO WORKFLOW

排版搞定了，接下来就是推送。我之前一直用的 baoyu skill 不只能推 MD，也能 直接推 HTML 到草稿箱 。

所以流程变成：

排版流程

gzh-design 排版出 HTML → baoyu 推送进草稿箱

不需要手动复制粘贴，不需要中间环节。两个 Skill 各干各的活，拼起来反而比之前的方案更顺畅—— 排版更丰富 ，推送照样一键到草稿箱。

为了直观对比，我说：

重新推送下，分别使用6套主题推送下

WorkBuddy 把 6 套主题 全部排版、校验、推送 了一遍。我公众号草稿箱里现在有 6 个版本，标题末尾标了 [摸鱼绿] 、 [红白色系] 、 [石墨极简风] 、 [留白禅意风] 、 [摸鱼票据风] 、 [橄榄手记] 。

主题

校验

推送

摸鱼绿

0 ERROR

✅

红白色系

0 ERROR

✅

石墨极简风

0 ERROR

✅

留白禅意风

0 ERROR

✅

摸鱼票据风

0 ERROR

✅

橄榄手记

0 ERROR

✅

6 套主题 全部 0 ERROR ，全部推送成功。打开草稿箱就能逐个对比效果。

///

LAST

写在最后

LAST WORDS

回过头看这轮对话

我做的

WorkBuddy 做的

发了个 GitHub 链接，说「看下这个skill」

分析功能、拆解6套主题、解释技术原理

说「装一个试试」

克隆仓库、逐文件安全审查、判定P2安全、安装

说「排下版我看下效果」

加载组件库、组装HTML、跑合规校验、生成预览页

说「6套主题都推一遍」

6套主题分别排版+校验+baoyu推送，全0 ERROR

说白了，我全程就动了 嘴和眼睛 。

我的几点感受

① 排版选择多了

不再是那几个来回换。gzh-design 的6套主题是完整组件库，引言卡、章节标题、代码块、签名区全是现成片段。还有主题生成器，一句话就能出新风格。

② 排版和推送拆开，反而更灵活

gzh-design 专注排版出好看的 HTML，baoyu 专注推送进草稿箱——两个 Skill 各干各的活，拼起来比之前一条龙更顺畅。

③ 不用手动复制粘贴了

gzh-design 本身是手动模式（输出 HTML 需要复制粘贴），但配上 baoyu 直接推 HTML 到草稿箱，中间环节就没了。

④ 全链路 WorkBuddy 自己跑通

发现→审查→安装→排版→推送，我说了四句话，整条链路就跑完了。不是「帮我排版」，是「帮我干了一件我本来干不了的事」。

最后

这轮下来，我搞清楚了三件事：

1
gzh-design 的排版比之前的方案丰富——6套主题+主题生成器，不再是那几个来回换；

2
排版和推送可以拆开组合——gzh-design 出 HTML，baoyu 推草稿箱，不用手动复制粘贴；

3
从发现一个 Skill 到 6 套主题全部试完推完，全程我只说了四句话——这才是 100 种用法该有的样子。

说句实话：gzh-design 是开源 Skill，作者甲木跟摸鱼小李一起做的，有兴趣可以去 GitHub 看看。但不管你用不用这个 Skill，核心逻辑是一样的—— 好工具拼起来用，比一条龙更灵活。

如果这篇文章对你有帮助，欢迎点个赞、在看、转发，让更多人看到。

既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。

点赞

在看

转发

THANKS FOR READING

这是WorkBuddy 100种用法第98篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #公众号排版 #gzh-design #Markdown排版 #微信公众号 #AI排版 #Skill #AI工具 #自动化排版 #内容创作

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMyd8Z4l3I4AMDFcmemWCEcWveCiceyDMicOrZvGRLnDvSCoh7rn2xy2Q93WBIibkljRfCTPWEXt5hIjTdFeQnlyeTG5GAGlmbp3Q/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM1scCkvZ0KOTbk7fRvEib3q468niczh8NfMeAmUTxskOHKDlVVgYxyjJvKnEvv70Zvcx4qsNpoxbbFoN67rLOMyCELClHL123J4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROHWX2fUg2p44zQOoByKdDqQ5vn8hCkuxah2WacJAJ2ZGJYsIPvY22lG56QNdrsu33w6oTJfjLygdC8iaVag9BRW1UPFhluPYIY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROq0KLCVoRuDUfGnAtcXVfOLiaNhdKHsNzqsSrIc1tGa7GexONJp4fHRmpVxkI9mFns6cF9MhfDDgNEmP5e4u9K0xDibp2CCDUHQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMLfDwgtgicb9LjicvAicHf38D8Yrhjkic3oRMJ1lGCH4v9GU829IFy6ay7KUVuPdEInibFpv8bTSZmYGJYaWnHdz9aNQuzAWTibibuKg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROrYGCGHt6VhInTGOLibBvWibSeEkBV0Vyg7h40hIJZ2kNKyBFrePlTzFVTiaktHNjSlU25plWKN2pjdowqoAP1PxBQWDoY9b46wE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPQDVfIXnmSqzwnjGENIDOpcC1wvibJtx4to13iclMnE4sfqWAJ0v8D8dbMvaGmJKzOGcpn1arOOqSvicNz7HFDxRZv64G9Z1LhMU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROjRLNvbkWp5cxSGZsriaqbOhgTyEy5qwbVIWTNZ4KtMPgA64BRQ9u2RLvUyC2M4LicicQUo6Rvs2bOV67SpBJialPic4IxguicyBuW4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRORjNLKP1t1FFJoMfE0LIPicibUe8OUDCcJTQPDsJaAYSEHRcxBdCyJiavXy5qo1Nj2rdY18AmwSsOaejyWUvMeBOQdtS9MqOAa0w/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPPXTd5XoSialKEvkmRdRxZACmmujfrrnNAF2PtjicevEK9CicuwLOkpPMdcj2SE1zLqJMxtE4hPSAOaUL3ll97NlT0l5Q73HMbtc/640?wx_fmt=png&from=appmsg
