# WorkBuddy 100种用法 #76 | 微信群里建个内部资料库？IMA知识库0成本搞定

- 合集序号：76
- 公众号：我与ai的那些事
- 发布日期：2026-06-15
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329675&idx=1&sn=78ceee22d98411890af61e52af8d1863&chksm=8830350cbf47bc1a5eb545226409906edcf087e43c737abf77bc3584966b75e2c6b1c3c74091#rd
- 正文字数：2476
- 正文图片：7

## 摘要

微信群资料混乱难找？本文记录我用 WorkBuddy 一步步搞定 IMA 知识库的全过程：选型对比、权限设置、防外人闯入，零成本建起微信群专属资料库。

## 正文

大家有没有这种经历：建了个微信群，想往里丢点资料——PDF、文档、课程链接……结果文件满天飞，找的时候翻半天找不到；新进群的人问"之前发的那个资料在哪"，你又得重新发一遍。

更头疼的是，你想建一个内部资料库，只有群里的人能看，外面的人进不来，但不知道怎么搞——网盘权限太粗、公众号附件有限制、小程序开发又不会。

今天这篇文章，就是解决这个问题的。

我直接去问 WorkBuddy，从"两个知识库有啥区别"一直问到"怎么防外人进来"，它全程陪我跑完了整个方案设计。下面把这段对话整理出来，你可以照着做。

先说结论：IMA 知识库是目前最适合普通人在微信群里建内部资料库的工具，免费、零门槛、权限可控。

一、先搞清楚：乐享和 IMA 有啥区别？

我第一个问题是：腾讯的乐享知识库和 IMA 知识库到底有啥区别？哪个更适合微信群用？

WorkBuddy 去搜了一圈，然后给我拉了一张对比图，顺便把两个产品的定位讲清楚了。

腾讯其实有两个知识库产品，很多人分不清：

-
腾讯乐享知识库 —— 面向企业的，定位是企业级知识管理平台

-
IMA 知识库（ima.qq.com） —— 面向个人/小团队的，是个 AI 智能工作台

简单对比一下：

腾讯乐享

IMA 知识库

定位

企业级知识管理平台

个人/小团队智能工作台

费用

企业付费

个人免费

格式支持

103 种（含音视频）

20+ 种常见格式

AI 能力

RAG 问答 + 知识萃取

DeepSeek/混元双模型

适用场景

公司内部协作沉淀

个人收集 + 轻量分享

WorkBuddy 给我的总结很到位：乐享是公司的档案室，IMA 是你的第二大脑。

二、哪个能直接放在微信群里？

搞清楚区别之后，我问了第二个问题——也是最关键的一个：哪个能直接放在普通微信群里？

答案很直接：只有 IMA 能。

原因很简单。IMA 有微信小程序「ima知识库」，你在共享知识库里生成一个分享链接或二维码，发到微信群里，群友点开就能看——不需要下载 App，不需要注册企业微信，零门槛。

而乐享对接的是企业微信，如果你的群是普通微信群（不是企业微信群），群友根本打不开乐享的内容。

所以如果你是普通用户，想在微信群里分享资料，IMA 是唯一能直接用的。

三、IMA 的权限怎么设？

确定用 IMA 之后，下一个问题自然就是权限了。

我问 WorkBuddy："IMA 里如何设置权限？我已经连接了 IMA skill，你帮我创建一个知识库做个示例。"

它先帮我查了现有的知识库列表，发现我已经有一个共享知识库「workBuddy工作区」（13 条内容，我是所有者）。然后告诉我：IMA 的 OpenAPI 目前不支持通过 API 创建知识库——创建只能在客户端操作，但它可以帮我在创建好后往里添加内容。

接着它详细讲了 IMA 的权限体系。IMA 的共享知识库支持三种角色：

角色

能做什么

所有者（管理员）

管理成员、修改设置、增删内容

编辑者

上传文件、编辑内容

查看者

只能浏览和 AI 问答

具体操作也很简单。手机端微信搜「ima知识库」小程序，进入共享知识库，点右上角「···」→ 成员管理，就能邀请成员并分配角色。电脑端在 ima.copilot 客户端里操作，路径类似。

四、我不想群外人加入，怎么设置？

这是我最关心的问题。我的共享知识库，是不是所有人都能加入？

WorkBuddy 帮我去查了「workBuddy工作区」当前的权限状态，查完告诉我一个问题：

access_status 是 1（公开可发现），join_type 是 1（允许自由加入）。

这意味着：只要别人找到这个知识库的链接，就能直接加入，不需要我审批。

怎么防？WorkBuddy 给了我两步方案：

第一步：把加入方式改为「仅邀请」或「需审批」

在 IMA 客户端操作：打开知识库 → 右上角「···」→ 知识库设置 → 找到「加入方式」→ 改为「仅邀请」。

改完之后，即使链接被转发到群外，别人也进不来。

第二步：在微信群里发邀请链接，只让群友加入

群友加入完成后，还可以撤销分享链接，彻底关闭入口。

WorkBuddy 还特别提醒我，如果不想一个一个手动邀请，可以用「需审批」模式——群友点链接申请加入，我在成员管理里看到后点同意就行。比「仅邀请」多一步审批，但群友不需要我手动邀请也能自行申请。

五、防泄露：没有什么方案是 100% 安全的

我问 WorkBuddy：群友把内容转发给别人怎么办？

它的回答很实在：没有任何方案能做到 100% 防泄露。 但你可以做到「足够麻烦，让大多数人懒得折腾」：

风险

应对

群友转发邀请链接

设「仅邀请」+ 定期更换链接

群友截图/复制内容

关闭导出权限，加水印提示

成员到期不走

定期清理成员列表

外人混入

知识库「仅邀请」是第一道门槛，定期审成员是第二道

六、这次对话给我的最大收获

整个聊完之后，我有几个感受，也是 WorkBuddy 在对话里反复提醒我的：

选工具别贪大求全。 很多人一上来就想要"企业级解决方案"，结果工具太重根本用不起来。对于微信群资料管理这个场景，IMA 的轻量反而成了优势——小程序打开就能用，不需要培训。

先验证再投入。 不要一上来就搭复杂的体系。先用 IMA 建个共享知识库，把资料放进去，在群里分享一周，看看有没有人真正在看、有没有人说"这个东西有用"。有反馈了再考虑精细化运营。

权限比功能更重要。 IMA 的功能其实不算多，但权限设计很合理——所有者/编辑者/查看者三层，加上加入方式控制，已经覆盖了 90% 的微信群内部资料库场景。不需要更多。

AI 对话是最好的使用手册。 这次我全程通过和 WorkBuddy 对话来完成调研、对比、方案设计。不用去看官方文档，不用去百度搜教程——直接问 AI，它帮你查、帮你比、帮你出方案。这才是 AI 工具该有的用法。

写在最后

如果你也在运营微信群，想给群友搭一个内部资料库，建议今天就试试 IMA 知识库：

-
微信搜索「ima知识库」小程序

-
创建一个「共享知识库」

-
往里传几份资料试试

-
生成邀请链接，发到你的微信群里

整个过程不超过 10 分钟，完全免费。

工具本身不值钱，值钱的是你整理好的知识和持续运营的耐心。 工具只是帮你把这件事变得更轻松而已。

这是WorkBuddy 100种用法第76篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROoYgUicEjnEpryHfJRCJ8v3wr3eWpHicE2Jmy9dAKKSoEucgV6O3dnCiaDCiaNibztF0TuicdV2YK9yVG8MVkAJTZhJWykickuKzibtC0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROdzNhaIHe0iaQUPKuheuO4hmFGqJHyOsoXrV1BlKQpma7SIPcVTdbTKr4ewrv0Kia6B6CDKC6R8ha1a5wqAZ72KaG2n7K6wc0Eg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMvFSZ3pic1Ct7MgricK8Ypd1vibYowR77RLT21xLfduVjpiaJxcoJyMMoliaHyJZqnEplxkibIJga0ic0pXEsp1yVxU8omqvqdMaLwDY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMnofetgMX3CGpOzI094EIsGGjqMdBV6wMsicprd9vryA9yODSicNWVqvUh33eQqUib199BbYrLrickakuC55T9Svlr0GySSkmftWw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPTjSZ1gP0ypAPt8qyae7ZD0TOADbcXfrWXib6f746wKmhSqnatxC04IJdcKfIeRCWO7WxiazMvib7T2JsN5sCVfhIvQ2ic6bbqiaYU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNiahwdUZO3azGYZGNyLicNSOTRd2EwvFBcPc5bpFA3sSly7gnAgXsic2FjdsMs96YmhZyDkib9JtUF3cWicqPlhickmiaiabQqqMVZkHE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPZfqNFAepFDibqIOb9psgDzjFISfr9iavfv5e9FWExO7QMG33J3HrNibK4osSI0iczyfGttThCXGDqzIsAicbYv5a0p2ugoHz3yLxs/640?wx_fmt=png&from=appmsg
