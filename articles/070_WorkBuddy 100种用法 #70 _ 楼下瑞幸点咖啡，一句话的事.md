# WorkBuddy 100种用法 #70 | 楼下瑞幸点咖啡，一句话的事

- 合集序号：70
- 公众号：我与ai的那些事
- 发布日期：2026-06-09
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329435&idx=1&sn=5878feda4bdcf1ebdeef13aa30aecfe6&chksm=8830341cbf47bd0a8b23cf346915a842e9df4f72a836792a165cbbd77b2dcd05c1394886a5de#rd
- 正文字数：1774
- 正文图片：5

## 摘要

把瑞幸咖啡 MCP 接入 WorkBuddy，查门店、看优惠、点咖啡全在对话里完成，连 App 都不用打开。

## 正文

晚上我突发奇想：楼下就是瑞幸，能不能让 WorkBuddy 帮我点一杯？

说实话，一开始我下意识觉得不可能——AI 助手怎么能帮我点咖啡？这又不是写文章查资料，涉及真实付款和到店取餐，总感觉有堵墙。

但转念一想，之前WorkBuddy 100种用法 #61 | 让AI帮你点麦当劳？WorkBuddy这个技能我玩嗨了已经用 WorkBuddy 点过麦当劳了吗？那时候麦当劳的 MCP 也是接入之后就能点餐。瑞幸会不会也有？

于是我试着搜了一下，结果真的找到了。

瑞幸居然出了官方 MCP

2026 年 6 月 1 日，瑞幸咖啡正式上线了 AI 开放平台，网址是 open.lkcoffee.com。它提供了三种接入方式：MCP Server、Skill 离线包和 CLI 工具。

咱们在 WorkBuddy 里用，最简单的方式就是 MCP Server，基于 Streamable HTTP 协议，远程连接，不用装任何东西。

第一步：去官网登录拿 Token

打开 open.lkcoffee.com/mcp[1]，页面长这样：

点击右上角「登录」，用手机号 + 短信验证码登录：

登录成功后，右上角会变成「AI控制台」，点开后选择「点击创建或者查看Token」：

Token 生成后，有效期一个月。页面会显示「复制 MCP 配置 JSON」按钮，直接复制即可：

第二步：在 WorkBuddy 里配置 MCP

把刚才复制的 MCP 配置粘贴到 WorkBuddy 的 MCP 配置里。打开 WorkBuddy → 专家->连接器->自定义连接器 → MCP 服务管理 → 配置 MCP，贴进去就行。

然后你会发现列表里多了一个叫 my-coffee 的服务，首次连接需要点「信任」：

点完信任，这个服务就激活了。整个过程不到 2 分钟。

试试看能做什么

我直接跟 WorkBuddy 说：「🔍 查找附近门店」。

WorkBuddy 立刻开始调用 MCP，几秒钟后回复了我家附近 8 家瑞幸门店的信息：哪家营业中、哪家打烊了、营业时间、距离多少米，一清二楚。

最近的一家就是楼下的时代盛华店，可惜我去查的时候已经 21:18，它 21:00 就关门了。最近还在营业的是王府井百货中心店，离我 665 米，走路 7 分钟。

然后我又问：「楼下那家有什么优惠？」

WorkBuddy 直接搜了这家店的菜单，告诉我有两款 9.9 元 的特价饮品：Hello苹果茉莉和小青桔茉莉冰奶，原价都是 16 元，省 6.1 元。

其他美式、拿铁什么的都是原价，没活动。

除了下单，还能干啥？

瑞幸的 MCP 提供了 8 个工具，覆盖了点咖啡的全流程：

功能

工具

用法举例

查门店

queryShopList

"我家附近有哪些瑞幸？"

搜商品

searchProductForMcp

"我想喝生椰拿铁"

看详情

queryProductDetailInfo

"这杯咖啡有哪些选项？"

调属性

switchProduct

"换少冰、半糖"

订单预览

previewOrder

"看看这单多少钱"

创建订单

createOrder

"帮我下单"

查订单

queryOrderDetailInfo

"我的取餐码是多少？"

取消订单

cancelOrder

"我不要了"

也就是说，从「查哪家店开门」到「看看什么便宜」到「帮我下单」到「取餐码多少」——全程不用打开瑞幸 App，跟 WorkBuddy 聊就行。

而且据官方说，它还会自动匹配优惠券和咖啡库券，不会错过最低优惠。下单后返回微信支付链接，你确认付款就行。

一个小意外

聊天过程中还有个有意思的细节：WorkBuddy 其实不知道我在哪里。我让它查附近门店时，它用了默认坐标，结果查出来的门店不是我这的。

后来我想了办法——IP 定位、macOS 定位服务都试了，但因为网络环境和权限问题，定位都不太准。最后我直接告诉它「我在xn时代盛华」，它才精准定位到楼下的门店。

这也说明一个事：AI 工具再厉害，有些基础信息还得人来提供。告诉它你在哪，它才能把活干对。

现在我已经把瑞幸 MCP 配置好了，明天早上买咖啡，一句话就能搞定。

如果你也经常在瑞幸买咖啡，推荐试试这个配置，真的很省事。

这是WorkBuddy 100种用法第70篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #MCP #瑞幸咖啡 #AI点单 #连接器 #效率工具 #自动化 #生活场景 #智能助手 #咖啡

引用链接

[1] open.lkcoffee.com/mcp: https://open.lkcoffee.com/mcp

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNZEBuWt7qicC3YWAUeoENTrwJBFEmfxzucRRPO6DzScD8maIG7KDKfskHx21D6lRgI6pBPUkdicztV0ZywKyQRw2chQmkicT5cpk/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMdFj1ajGhNKiaT5nymsGmdTqGLOENy3LicOkULqmVNKghsjiasmpsZ6iczgMKt81D2flYAsMygQrTYd2ia73DY8Ktyu2sbpURJ6Y3I/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN6oFjLIbGn5IL2icnKp7YvHmfLgQTOLl66PqNEUdVATqASbLQ38CPB2GBp5FQILV1heyfhHQ6fWIr1c7Kz6vVEGQF9DCQ0HfzY/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMKoxGgibJiaDUOem360NyhG6OQN6aukIFEZr7JloxS7xoff7LIJqVZkayM0LNjZDszvBjlpIBnNRaTiaycxoL0ibbqGiamfUG4yPGE/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNrmZvns0RiaGeDolKpBUiccM5v0ibc1J4Nm3IhlnJuagYWDubcELxtt5wLW9vXC3MpJk0EXAOMOd1slJPLhu5D6I67Bwf82P3Npk/640?from=appmsg
