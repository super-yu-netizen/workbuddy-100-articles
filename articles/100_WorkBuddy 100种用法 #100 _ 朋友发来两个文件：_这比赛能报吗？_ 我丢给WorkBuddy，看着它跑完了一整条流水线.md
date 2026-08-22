# WorkBuddy 100种用法 #100 | 朋友发来两个文件："这比赛能报吗？" 我丢给WorkBuddy，看着它跑完了一整条流水线

- 合集序号：100
- 公众号：我与ai的那些事
- 发布日期：2026-07-09
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330200&idx=1&sn=e31b006479020d757ef7a550394932b1&chksm=8830371fbf47be0971c3e3c0b3331f9543294698d9b29f8f9a4330babb0a40d9dda742327410#rd
- 正文字数：2341
- 正文图片：7

## 摘要

朋友甩来两份比赛文件丢给WorkBuddy，它OCR读文件出解读报告、自查官网倒计时纠正日期、改HTML补奖励与报名清单、一键部署上线。

## 正文

WORKBUDDY 100种用法2026.07.09

朋友发来两个文件 · “这比赛能报吗？”

一个真实对话：把文件直接丢给 WorkBuddy，看它跑通整条流水线

DOODLE

读文件 · 出报告 · 认错 · 查官网 · 改格式 · 部署上线

案例复盘AI办公

PROLOGUE
一百期特辑

100期了。这一篇不聊功能，就是一段真实对话——朋友甩来两个文件，我看都没看直接丢进去，WorkBuddy 自己跑通了整条流水线：读文件、出报告、认错、查官网、改格式、部署上线。

今天中午，朋友微信甩过来两个文件，附了一句：“看下这个比赛，我们小企业能报不？”

一个是 .pptx（企业组报名流程），一个是 .pdf（大赛通知）。我一个都没点开，直接把两个文件拖进 WorkBuddy 的对话框，回了一句：“读取下这两份文件，总结下讲了什么，给我一份解读报告。”然后我就去倒了杯水。

把两个文件丢进 WorkBuddy，开始这趟流水线

01

PART

它先解决了“文件根本读不动”的问题

READ & PARSE

等我回来，报告已经出了。但更让我意外的是它怎么读的：

-
那份 PPTX 是 19 步报名系统的截图操作手册，文字极少，全是图。WorkBuddy 把它当压缩包解包，从 slideN.xml 里把步骤文字抽了出来。

-
那份 PDF 才是硬骨头——它是 OFD 转出来的扫描件，12 页，用常规工具提取一个字都拿不到。WorkBuddy 调起 OCR（tesseract + 中文包），把 12 页全文识别了出来。

一会儿工夫，一份解读报告躺在那儿：资格判定、赛道匹配、行动清单，还附了官方咨询电话。

PPTX 解包 + 扫描 PDF 用 OCR 读出 12 页

你们在“资格”上完全符合——大赛面向科技型中小企业，不设规模下限，只设“2025 年营收 ≤ 2 亿元”的上限，小微企业天然达标。企业数字化业务最匹配「新一代信息技术」赛道。真正的硬门槛是自主知识产权（软著/专利）。

02

PART

它会认错，而且自己跑去查证

SELF-CORRECT

报告里写：报名截止 2026 年 6 月 30 日，deadline 已过。

我多嘴问了一句：“这个截止日期你从哪来的？”

WORKBUDDY 说
出处溯源

出自你发来的第二份 PDF 第 6 页原文，还把那句话贴了出来——“地方赛参赛报名截止日期为 2026 年 6 月 30 日。” 并补了一句：它用北京赛区公告做了交叉核对，一致。

追问“截止日期从哪来的”，它贴出 PDF 第 6 页原文

我说：“你去官网看看，有显示地方赛还有 6 天。”

它真去了。官网首页要靠 JS 渲染，普通抓取拿不到——它启了真实浏览器把页面渲染出来，读到了首页实时倒计时：

官网实时倒计时——还剩 6 天，它推翻了自己的结论

地方赛参赛报名截止：6 天 11 小时 44 分 20 秒

也就是实际截止约 2026 年 7 月 15 日，比通知写的 6 月 30 日延后了半个月。

WORKBUDDY 说
主动认错

“你看到的没错，是我之前只依据那份通知、没去官网核实实时状态，结论下早了。抱歉。”

维度

通知写的

官网实际

截止日

2026-06-30

≈ 2026-07-15（倒计时约 6 天）

性质

名义截止

系统报名实际关闭时间

该信哪个

参考

以官网实时倒计时为准

一个 AI 愿意在你指出错误后，真的去现场核对、承认自己下早了结论——这一点，比它会读书值钱多了。

03

PART

你改需求，它换格式重做

REMAKE

我顺势说：“更新报告，不要 docx，用 html；另外看下这比赛有奖励吗？报名需要什么准备？”

它去官网抓了《参赛企业注册报名操作指南》那份 PDF，把材料清单、7 大系统填写模块、6 步流程全抽了出来，然后重做成一份单文件 HTML 报告（自带样式，离线也能看），新增了两整块：

解读报告长这样（完整版可在线查看，见文末上线地址）

改 HTML、补奖励和报名准备清单

比赛有奖励吗？

地方赛现金奖

各地自定，北京最高 30 万。

全国赛荣誉

五类赛道一二三等奖 + 创新创业 50 强。

高价值非现金资源

对小微其实比现金更香：国家级基金推荐通道、银行授信+利息优惠、科技型中小企业/高新/专精特新「小巨人」资质绿色通道、大企业融通对接，北京还能积分落户创新创业加分。

报名要准备什么？

实物材料

营业执照、统一社会信用代码、软著/专利证书、财务数据、公司章程。

系统要填 7 大模块

企业基本信息、人员结构、核心技术（最费时）、股东&融资、核心团队、商业计划书、创业服务需求。

6 步操作流程

并特别标了企业认证审核要 1–3 个工作日——这是最容易卡在最后一天翻车的坑。

04

PART

你说“部署上线”，它真部署了

DEPLOY

我看报告没问题，回了两个字：“部署上线。”

它把 HTML 整理成 index.html，一键推到云端（CloudStudio），回了我一个可分享链接 ——手机、电脑直接打开就是完整报告，还能转给同事。

报告上线地址

https://15468f1645f54c0ebe08973432e51ae5.app.codebuddy.work

一键部署上线，拿到可分享链接

整段对话到此闭环。从两个不想看的文件，到一份上线可分享的报告，WorkBuddy 自己串完了一条流水线：

...PIPELINE

读文件（PPTX解包 + 扫描PDF OCR）

　→ 抽信息（资格 / 赛道 / 截止日）

　　→ 交叉验证（北京赛区公告）

　　　→ 自我纠错（官网实时倒计时推翻原结论）

　　　　→ 多格式重做（docx → 单文件 HTML）

　　　　　→ 抓官方指南补全奖励 & 准备清单

　　　　　　→ 一键云部署上线

朋友那边的后续：窗口还剩 6 天，我让他今天先把账号注册和企业认证做了，别卡在最后一天。

这是WorkBuddy 100种用法第100篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

赞

在看

收藏

THANKS FOR READING

#WorkBuddy#AI办公#中国创新创业大赛#OCR识别#AI自动纠错#智能解读报告#一键部署上线#公众号写作#数字化工具#百期纪念

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROlo1p57KibDSJLZNXutXt07O5IFDpAxEyzGH2krcTVS8fQiaOPzcOwt1W093z28QslCRHOE3qFahJiaGribC1yX5YAJRxy185YAfk/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO9yL55k00WPorFIxec0cQ7m85t1etm3Gdr720Uo7JSCGAhZBvMsxch0joFrFPEX6Ihk8x56o9OsFOj9oTbOokibYoWfhawnyd0/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROibaWF23u0Oib7Eu25yqk5DVEBtKMuzQohofpArgrbZJPeU4ThzFsh9XU3UeWE9EMr5y1kfpNnaJ0yhq1SExib8ysBHPkISBNzicg/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPQanaKVPFeoPW9T9Q1ibeAZPqDonHIcxXdibVqkyF1ZJnhrRP3okYicJfXrFr6m86jyWIP0wicOha7TqHONa7p75GyVu7iclZeZsdM/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROdehYFbtHnN6CJh3e9I5GNWukwibF6zxnxSfLFg57JzqkjM4icJAHlkbcxtuwdIMQTE0HibBb3ZfuKmOhYkp5BmiarJVChicibe5fao/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNF7M8ZAV71bvIb5KkFCJ7PHLLeHKbvIpC33yXNNia2RuUlBqPIFqmQcYS5hP9W2ogp7wiaKk1pZicer4akscfWlQ5g5DuBGibGe30/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPT8gibPib1U4nkAKx6h8t53HcHH01WnCjy9ZS7lEaicxGlynYEUCGHmaawNvZ23fcqAAyl7ZwKEpqo8WmAzrSJWaH2J2fibSBJoTQ/640?from=appmsg
