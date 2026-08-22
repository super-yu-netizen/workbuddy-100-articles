# WorkBuddy 100种用法 #78 | 用 WorkBuddy 连上钉钉，我才发现它这么好用

- 合集序号：78
- 公众号：我与ai的那些事
- 发布日期：2026-06-17
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329727&idx=1&sn=6dc076b2d79409bea86b80b932765dd9&chksm=88303538bf47bc2eff598db08e819c36f0f75bf659f33ff7254ea21563107a005bf6ba9ae3d6#rd
- 正文字数：2285
- 正文图片：15

## 摘要

一条指令查未读消息、回群表情、看审批流程——钉钉连接器让办公协同不用切 App，对话里全搞定。\x0d\x0a摘要：

## 正文

前两天有读者在公众号下面留言：

说实话，钉钉我好久没用了，现在公司办公主要在企业微信上。但既然有需求，今天有点空就试了一下。没想到，真的方便。

连接钉钉

打开 WorkBuddy，点左上角 「连接器」 按钮，找到 DingTalk（钉钉），点进去就能看到连接入口：

点击 「连接」，弹出授权窗口，显示钉钉能做什么——AI表格、考勤、日历、群聊、机器人、通讯录、文档、钉盘、AI听记、待办、审批……光看这个列表就吓一跳，功能比想象的多太多了：

接下来是扫码登录。用手机钉钉扫一下电脑上的二维码：

扫完后手机会弹出一个确认页面，提示"DingTalk–工作空间"要登录你的账号，点 Log In 就行：

然后选择你要连接的组织（企业）：

最后一步，确认授权范围——获取个人头像、昵称等基本信息，点 Accept：

⚠️ 注意：如果提示「该组织尚未开启 CLI 数据访问权限」

别慌，这是正常的！说明你们公司的管理员还没开放这个权限。

页面上会有一个 「立即申请」 按钮，发给管理员审批就行。管理员同意后就自动跳转到授权成功页：

整个过程不到 2 分钟，搞定。

连上了能干嘛？

我连上之后第一件事就是让 AI 帮我查消息：

「帮我看下钉钉有什么消息？」

结果一下子拉出来 8 个未读会话：

群名

未读数

最新时间

淘宝ods更新监控

594

今天 19:50

魔搭ModelScope开发者联盟群

6629

今天 17:48

[小程序智能客服]服务群

54

6月14日

rpa+竞争数据xx沟通群

51

6月10日

xxx账号监控

1

6月5日

工作通知:xx科技

1

5月26日

美工特训营直播群

1

去年12月

工作通知:阿里云开发者社区

1

去年6月

看到这个列表我就笑了——6629 条未读的魔搭群，这得是多爱刷屏啊……

我接着问 AI：「淘宝ods更新监控都说了啥？」，它直接把最近的几条消息拉出来了：

06-17 19:50 sycm(机器人) 播报-ufirst-886-28
06-16 23:50 sycm(机器人) 播报-ufirst-891-30
06-16 22:50 sycm(机器人) 播报-ufirst-891-30
...（每隔一小时一条）

原来全是机器人自动播报的 ODS 数据更新状态，594条未读全是这类噪音。这种群最适合设免打扰，AI 也主动提了这个建议。

再看魔搭群的消息就有意思了——有人在讨论 GLM 5.2 的 API 支持，还有 ICML2026 预讲会的直播通知，信息密度很高。

不止看消息，还能回复

这是我最惊喜的功能——可以直接在对话里操作钉钉。

我说：「帮我在魔搭群里回个表情」，AI 先帮我拉取了最近的消息让我选，然后问我回哪个表情：

📌 你要给哪条消息回表情？
→ 席朋朋 - "有没有新手"

📌 回什么表情？
→ 👏 鼓掌

选完之后，一秒完成，群里多了一个鼓掌表情回应。整个过程不用打开钉钉 App，就在对话框里搞定了。

💡 支持的交互方式：

-
发群消息 / 单聊消息（以你本人身份）

-
表情回应（点赞/鼓掌/大笑/666 等）

-
引用回复某条消息

-
机器人发消息（如果有配置机器人）

一句话查待办、日历、审批

连上钉钉后，我试着问了几个日常办公问题：

「看看我今天什么待办？」 → 返回空列表（好吧，我确实不在钉钉上管待办 😂）

「看下今天的日历」 → 也没有日程安排

「有没有待审批的流程？」 → 审批列表也是空的

虽然结果都是空的，但这个过程让我意识到一件事：以前要分别打开三个不同的页面/应用才能看完的信息，现在一句话就能全部查到。

如果你的公司重度使用钉钉，这些功能的价值就更大了：

-
📋 待办事项一键查看 + 创建 + 指派

-
📅 日程管理 + 查同事闲忙状态 + 订会议室

-
✅ 审批流程查看 + 同意 + 拒绝 + 转交

特别是审批这块——支持完整的 OA 流程操作，包括：

-
查看待处理审批

-
查看/添加评论和抄送人

-
同意/拒绝/撤销

-
转交任务给他人

-
查询已发起/已处理的审批记录

而且每次审批操作前，AI 都会先跟你确认，不会自动执行，安全放心。

钉钉到底能做多少事？

整理了一下完整的能力清单（可能比你以为的多很多）：

🔔 消息 & 群聊

-
收发群聊/单聊消息、搜索历史消息

-
创建/管理群聊、邀请成员、设置群主

-
机器人发消息、Webhook 告警

-
表情回应、引用回复、撤回消息

-
查看未读会话、置顶会话

📅 日历 & 日程

-
创建/查询日程、邀请参会人

-
预订会议室、查看闲忙时段

-
今日议程一览

✅ 待办

-
创建/完成待办、子待办

-
设置截止日期、指派执行人

-
循环待办支持

🏢 OA 审批

-
全流程审批操作（发起/同意/拒绝/转交/撤销）

-
评论、抄送、操作记录

-
已发起/已处理/抄送我的审批

👥 通讯录 & 搜索

-
搜索企业内人员（按姓名/部门/职责/电话）

-
查部门成员

📧 邮箱

-
收发邮件、搜索、回复转发

📄 文档 & 多维表

-
创建/编辑/阅读钉钉文档

-
多维表增删改查、导入导出

🎙️ 其他

-
考勤打卡/假期余额

-
DING 消息发送

-
AI 听记（会议摘要）

-
AI 搜问（搜人/搜知识/搜行为）

-
钉盘文件管理

-
日志（日报/周报模板提交）

15 大模块，基本覆盖了你日常用钉钉的所有场景。

写在最后

这次体验给我的感受是：WorkBuddy 的连接器不只是"能连"，而是真的"能用"。

不是那种连上了只能查个天气的玩具级集成——而是可以真正帮你干活的生产力工具。查消息、回表情、走审批、管日程……这些动作不需要切换 app，在同一个对话里就能完成。

如果你还在每天被各种工作 app 切来切去搞得头大，不妨试试把常用的工具都接到 WorkBuddy 上来。说不定就像我一样——连上之后就回不去了。

这是WorkBuddy 100种用法第78篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #钉钉 #办公协同 #AI办公 #连接器 #审批流程 #消息管理 #待办事项 #日历管理 #效率工具

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPdSEwK3CaHGwg7ia56AuwaUL41pNkcsJMCJfDNAkhibcXYxrMRiavsP5VwGo9Cv976dM34B6t1bGu2B8bM7dicz83yEKY7TZFNVtc/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRN4HdDVLJQIfkMwMGXqBQ1ibThTeozhh6sCxhOTJtrn1UFQHLHU5k4IaWQsbSYXBp7qar0YCS2TxNwqtXKyrvqoHOhxGlnQsuyo/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMbhX6kRia6HicoJgR0OW3iapUyUC2Myiar272ibj68FdcRuwDpTFdVokjBD5k3sh0b8fz4fXXxiaav9TKxbRsh0Wibo3lOQxaric921bE/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMCC6AuocQxsB9OWKVNicwAuqEXL60hKlwzJy8EWIQmS1EicG9iaFvcHFql1xbV412iaqxZnf8JiaNRUMURgnnMFf5UzGQu0jMGcPXM/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRPRViaseTbvickupmZyHFlgzbSZtxEW0egMTcmruhSuZQcjz3nfWpib9aXv18VmOdNWnd1vJib8qVEb0pqJSMchUWTUX9ItICUVqa8/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPI8zJIDaicdIzkmicZp7OqiaN7zGLB5INzicBQ1Bnib0aibBYSXSvIhsuviblTajgkyl9lmFA379VmJAmrvOXsyocACn2YuayB7prpAA/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM3zhXzEnfsTCn9tffljEF6sQYzXpPRAe43bCNDJ5gRYFwgbFnEbh17f8mlZpmAv2WS2N5jphbE8gp3kic5Tiak03NkEgwR2pbj0/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMB8ibz9nR3EIYe7nlP6CXZEzib68STtCuSKu39wmubgf5jU1E11ypryv2fm7QgOz4oH5uwYFrrtvAU7XwJ3fgiaicmSGIdnl3t3to/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM6bb9xCJzSF8082Zlibw0BlyCwsqn5CcibYmXmdriauiaRXwBcVhHTRUJmTsPvwNeD0MKA4d2IfpXah9I05edFibiaNV8KDqSVYnDFA/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNxEibR7TzAUTlzXmhl3BtW7oAzgcqneql7uuOB8ZXKF3ib2Jmm0QSrHZ5icUBAoAwN5I8sgHFSFsgQ772iaoVEpBZ1vBbgEtScDwQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNVicYbaLy5elFQs5YJMGWPtXY8xicUIWVAp0tADMnxpSEibb6qaxSjxKrVvEcvicyUEatUOLfSqpSibn6u4IxWSfxHI7qVQhibZZNlM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROXPlut5pvRiaPZibicMmRx7nUvPKqZVUNKRiadat0W036VL6v6VrBxqp0byiaHzwdHGaFO15I9cbQpZol6hhC2NoUvDkib127y4f0Ew/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMksVBibbrbmk8Vrsmx8aseicAoal6zOzYr3WeSz00wg2FY4M3ghPCYDvSibpq7PJJxJlnE3gvLjkH9gnCsibKHvxV0oe0FicjZlJeI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMs7m1qZFwXB2NNgGeO4rAqjR0ic5CudMdtxwNz4kqiaoNibsdVWh1S8ibic5wlEro90ibaXVEajib9yKGaeYGuuqkQMI0TAVT6Eu6ZGU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMkiamAHlfsnnY0KSztdz1Bgg3WshtuFL9PyIsF8aqUOUmvwCicPicjQx6nPQ1pqzicAhMNs23HHgVTwuRPticJaykE6g2oBkopRdIs/640?wx_fmt=png&from=appmsg
