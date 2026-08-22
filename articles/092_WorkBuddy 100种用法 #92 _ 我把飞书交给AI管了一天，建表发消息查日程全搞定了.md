# WorkBuddy 100种用法 #92 | 我把飞书交给AI管了一天，建表发消息查日程全搞定了

- 合集序号：92
- 公众号：我与ai的那些事
- 发布日期：2026-07-01
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330030&idx=1&sn=2215bd65c2501100135271826b80dd57&chksm=883037e9bf47beff07ccbd8eaa29d6d69634c99e7b557faf7aa3fbf5ad17340740a805aac627#rd
- 正文字数：2574
- 正文图片：13

## 摘要

连接飞书后，动嘴就能让AI建多维表格、拉群发消息、查日程，十分钟的手动操作一句话搞定，效率拉满。

## 正文

以前用飞书，我的操作路径是：登录 → 点开飞书 → 找到多维表格 → 新建 → 设计字段 → 录数据 → 调格式 → 切看板视图 → 发到群里让同事看。

一步一步点，少说十分钟。

今天在 WorkBuddy 里试了一下，飞书这边的事，动嘴就行。

先连接飞书

开始之前，先把 WorkBuddy 和飞书连上。

打开 WorkBuddy 的「连接器」页面，往下找，能看到 Feishu（也就是飞书的国际版名称）。

点一下 Feishu，会弹出一个简介卡，下面有个绿色的「连接」按钮。

点完会跳到 Feishu Open Platform，让你创建一个 CLI 应用。它会自动帮你填好名字，比如我这里是「可乐's Feishu CLI」，直接点 Create 就行。

下一步就是授权。飞书的权限列表很长，包括文档评论、群消息、审批、任务、日历等等。你不用逐条看，直接点「Add and Authorize」。

授权成功后会显示「Permissions added and authorized」的确认页。到这个页面，飞书和 WorkBuddy 就正式连上了。

注意一件事：首次连接是一次性授权。后面每当你让 WorkBuddy 做一件新事——比如查日程、发消息、建群——飞书还会弹一次权限申请。这是飞书的细粒度安全模型，不是 WorkBuddy 故意折腾你。授权过一次就累积在账号里，后续不会再问。

WorkBuddy 连上飞书之后，能干什么？今天花了点时间测了一遍——从建表到查日程、从建群到发消息，一条龙跑完。

先说结论：除了个别需要管理员开通的权限，绝大部分常用操作，AI 都能替你跑完。而且最关键的是，你不需要搞清楚飞书的 API、不需要记字段 ID、不需要知道 chat_id 是什么。你只需要说人话。

建一张多维表格，从零到有

我上来就让它建一张「7月计划」的表格。

我说："在飞书多维表格里建一张表叫7月计划，放任务跟踪的字段：标题、负责人、截止日期、状态（未开始/进行中/已完成）。"

它建好了。然后我说："在任务跟踪里新增一行，标题=Q2 上线评审、状态=进行中、截止=2026-07-20。"

也加上了。

整个过程我全程没碰飞书。等它干完，我打开链接一看，表格干干净净，字段都对。

然后我说："按负责人统计未完成任务数。"

它跑了聚合查询，返回来了——当前只有一条未完成记录，负责人还是空的。

对，负责人里那个「张三」我没填，因为飞书通讯录里搜不到这个人。它老老实实告诉我："搜不到张三，负责人字段先空着，你手动补。" 不会硬塞一个错误的值进去。

查日程，3 秒出结果

我说："查今天的日程。"

然后飞书的权限弹窗来了。扫码授权，搞定。它告诉我今天没有安排。

整个过程比我自己打开飞书日历还快——因为我不用等客户端加载，不用切视图。一句话的事情。

建个群，把 AI 机器人拉进去

接下来我想试试 IM 消息。

先在 WorkBuddy 里搜群聊，找到了一个 TRAE 大赛的活动群。我说往这个群发条消息 👋。

然后，飞书的权限逻辑来了。

先是要 im:message 权限。扫码，授权。然后又要 im:message.send_as_user 权限——以我本人的身份在群里发消息。再扫。

扫完两次之后，我以为能发了。结果它报了一个 230027 错误：外部群的安全策略，不允许第三方应用以用户身份发消息。

换 Bot 发。也不行——Bot 不在那个群里，我是个普通群员，没权限拉 Bot 进外部群。

于是我说："帮我建个新群。"

又要授权——im:chat:create_by_user。第三次扫码。

这次终于全程跑通了：

-
WorkBuddy 建了一个叫「AI助手测试群」的群

-
自动把应用机器人拉了进去

-
Bot 进群后马上发了一条"👋 嗨，我是可乐的AI助手，建群成功！"

一气呵成。

建完群我说："把通讯录里的人拉进来。"

它翻了一圈，只找到「鸿泷」一个也聊过的外部联系人，但因为是跨租户用户拉不进内部群。于是给了我一个邀请链接，我手动转发就行。

来算一笔账：前前后后扫码授权了 4 次。看起来有点烦，但换个角度想——这些权限都是一次性的。今天授权完，以后建群、发消息、查日程再也不用重复扫了。

飞书的安全模型就是这样的：一个操作一个 scope，粒度很细。不是 WorkBuddy 的问题，是所有第三方应用做飞书集成的通病。好消息是授权累积，越用越顺。

真正的杀手锏：建了个公众号选题库

前面那些都是探索。真正让我觉得"这东西确实有用"的是后面。

我说："飞书的多维表格有什么使用场景？"

它列了一堆——项目跟踪、CRM、内容运营、资产盘点……每个场景都说得很具体。我挑了一个最切身的：公众号选题库。

我说："试下。"

然后它在飞书里创建了新 Base「公众号选题库」，自动设计了一套字段：

字段

类型

标题

文本

副标题

文本

系列

单选（WorkBuddy 100种用法 / AI工具测评 / 效率方法论 / 其他）

状态

单选（待写 → 写作中 → 待审 → 已发布）

发布日期

日期

预期阅读量

数字

文章链接

URL

备注

文本

不是瞎建的——每个字段都合理，颜色标记也配好了（待写=灰、写作中=蓝、已发布=绿）。这说明它理解"选题库"这个场景的业务含义，不是简单地翻译成了字段列表。

建好之后我说："把我最近写的文章录进去。" 它把我的 #83 到 #86 文章几十条记录批量写进去了，连带发布日期、系列标签、状态标记都对。

最后还出了个小插曲：#91 因为更新时标题匹配没对上，生成了两条重复记录（一条待写、一条已发布）。我让它检查，它搜出了重复、定位了旧记录 ID、用 --yes 确认删除，一刀清干净。

这一整套跑下来，我意识到一件事：WorkBuddy + 飞书，等于你有了一个能直接操作飞书的 AI 助手。不用打开飞书客户端，不用在一堆菜单里找"新建多维表格"，不用手动录入几十条数据。在对话框里说人话就行。

顺手定了条规则

最后我跟它约定了一件事：以后我说"推送到公众号"，它自动去飞书选题库里把那条标为「已发布」，写上发布日期。

这条规则我让它写进了长期记忆，以后每次推送文章它都会自动执行，不用我每次说"顺便更新一下选题库"。

说白了，这就是我想要的——一个能记住事情、能在不同系统之间自动化协作的 AI。一次建好基础设施，后面它自己跑。

这是WorkBuddy 100种用法第92篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #飞书 #多维表格 #AI办公 #自动化 #公众号运营 #效率工具 #选题管理 #飞书IM #AI自动化

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO7Bn7J8gplMMTMQtptxXFfJ9NcMXDJdZRibZp7VaaFeakC4jNJiawOJOAPQa1dcBEMlXlmpIaSkd6MedR99Dte43qOfIFiaREJJM/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNkCv6jTVYLcXHWD0RuHKFFtAicqASf8QvnibY7AiaYib4UCLV81pTmOwXT0PkfM6PDRqBKN3qjFPTswLFHBAaiamCyy6ZCHqIJ2cfY/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROmF1Pibj4UhQ7ic2Ijcr9wBSyqoerERaXSj6MLRibh2LH1Hyt05tylePFibtIb1P4nfjSOuL88LI9mJVdqbZ4aGLB0tFF7DJNy0xc/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMNzkKZacibhwqmsicuWrPCr1sgyjlE488VTQW28NRtEWYfBXCAGeHC9NlqjN9JMWDaicwvjhvFsnt1byfJOibXeBXicvUpqbX1INRk/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROicfiaHPBic46OJjeHfRtoyMibEenfSuGYrH3VzzwVmBW0sdKqcKPXibbRqK8YkN9hQVXXYm4luu7q7P0iaAVkicib68Non5woDstpvbw/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP446pGtu4ia1fOg1iaj1xACLDq0ibklYicvo0lXHz6zic5PvqroT7Gb0rwiaZBkDUtjDK08YJjQohGTdAJEphlicdXJ7o6jmn43BnANE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMIPWRKRicxvYv5zZ1qZH1H2dIVJFjugkLib0WVibkujF7cTvuybzvyn3JFcm7R3lmaD5FSd50WPumlo76bPoE8mIYn4f4luSYwZc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMa3ichyqicicO8IHNGHmLZPcnia9lpAtpUrNe7Lnia7868X5RjVxzH4fHJQT0eYMCaGQ5jjjvEDn5xiaNzicA2q35yOHNgFxeL01ye0M/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMk7zicJAub90FL1UeSBJRySibLOGVK4807TwSHm2GJKXlIIQuDAqVhQBKVlTsKn8dCzPWj0eDl4evQ5XmGIqRQv4IXxruuhpwkA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNTbvHY0q4RZgWibk29xt7XCn03ibcmBWw3iczDUkHG0Oib4x29SxlhNhhEJ1icQJKjjda10wIBcfiamRtD0VTNjyYGHljUonthG5NKM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMIDfzkuynkQAZlMibwB5gUSc6y4GxwdHuIMJYO36AwiapWrrEibYwqAh3aLPPRK1yIdKDkMzxTtI4qBkIkdFwshdLDAkdib2BzPibQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPj9QFvReQLahWxibPQWXJAbeV3zBKBARhwAHib5BMWWHjvTgjh3BoWymMkueHmsfibPm2JDAHJ2WXuAMBfWwTt6U3npBk2NnZicc0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMLbmBdaBJfGyQlk8qsaUfKI6NTTk6Ut7IP9stX8Y9KEjmyggyX411qDzLOX34mQMEz0RhCbibSksWBxcKN5YFODGuuQk0QYeEk/640?wx_fmt=png&from=appmsg
