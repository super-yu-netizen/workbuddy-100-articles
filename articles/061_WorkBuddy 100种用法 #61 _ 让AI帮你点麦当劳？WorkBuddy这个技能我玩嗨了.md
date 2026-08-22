# WorkBuddy 100种用法 #61 | 让AI帮你点麦当劳？WorkBuddy这个技能我玩嗨了

- 合集序号：61
- 公众号：我与ai的那些事
- 发布日期：2026-05-31
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329268&idx=1&sn=f2c8b701be812cda7a498b6bfcc6a46a&chksm=883034f3bf47bde5876b4cc7a418c69394fdda5cab065b5477f0ef3d3a1c9d11a5fb0289a223#rd
- 正文字数：1339
- 正文图片：14

## 摘要

今天发现WorkBuddy技能列表里有个麦当劳助手，从配置到领券全程AI搞定。手把手教你用MCP连接麦当劳官方API，一键查优惠、领券、找门店。

## 正文

今天闲逛 WorkBuddy 的技能市场，突然看到一个熟悉的面孔——麦当劳助手 🍔

支持查菜单、查门店、领优惠券、比价、跟踪订单状态……功能还挺全的。

顺手就点了「去试试」——

第一步：让它帮我看有啥优惠

装好之后，我直接发了一句：「帮我看看麦当劳有啥优惠」

结果……WorkBuddy 告诉我：连接器还没配置。

原来麦当劳助手背后用的是 MCP（Model Context Protocol） 协议，需要先拿到麦当劳官方的 API Token 才能用。

行吧，那就配！

第二步：获取麦当劳 MCP Token

WorkBuddy 给了一个链接：https://open.mcd.cn/mcp[1]

打开之后是麦当劳的 MCP 开放平台：

点右上角「登录」，手机号 + 验证码就能登：

登录成功后，回到首页，点「立即体验」：

弹出一个 Token 对话框，点「激活」：

勾选同意服务条款，点「同意」：

然后你就拿到了一串 Token，点复制图标把它拷下来：

⚠️ 这个 Token 代表你的麦当劳会员身份，别随便分享给别人哦。

第三步：把 Token 告诉 WorkBuddy

拿着这串 Token，直接发给 WorkBuddy 就行：

「2OxmzjhbS3g7SwEOtSmPwqJmZQumKV5N 这是我的 token，帮我配置下」

WorkBuddy 秒回：配置写入成功，验证通过 ✅

但还没完——它提示还要手动做一步：信任连接器。

第四步：信任麦当劳 MCP 连接器

打开 WorkBuddy 的 连接器管理页 → 自定义连接器，找到 mcd-order：

点击那个蓝色的「信任」按钮——

看到 mcd-order 变成绿色，显示 23/23 个工具已启用，说明连接成功了！🎉

第五步：开始用！查优惠 & 一键领券

重新问一句：「查麦当劳优惠券」——

这次真的出来了！当前可领取的优惠券一览无余：

优惠券

状态

🥔 免费脆薯饼

可领取

🍔 11.9元 麦辣鸡腿汉堡

可领取

🍿 19.9元 小食任选2

可领取

🍳 满分饱饱双人早餐

可领取

🍟 好薯成双早餐

可领取

接着我说：「帮我一键领取」——

5 张券，秒领！ 全部到账 ✅

每张券都带独立券码，去店里直接出示就能用。

这个技能还能干什么？

除了领优惠券，麦当劳助手还支持这些操作：

-
🔍 查询附近门店 — 告诉它你的城市，自动列出最近的店和营业时间

-
📋 查看卡包 — 你已经领了哪些券、什么时候过期

-
📅 活动日历 — 当前有哪些促销活动（比如六一儿童节的免费圆筒）

-
🛒 菜单与比价 — 查看在售商品和价格

-
📦 订单跟踪 — 下单后追踪配送状态

整个过程你不需要打开任何 App 或网页，跟 AI 聊几句就把事办了。

总结一下

整个流程其实就 4 步：

发现技能 → 获取 Token → 配置 + 信任 → 开始使用

第一次配置大概花 3 分钟，之后就完全不用管了。以后想吃麦当劳，跟 WorkBuddy 说一句话就行。

这就是 MCP 的魅力——把外部服务变成 AI 的原生能力。麦当劳只是开始，未来肯定会有更多品牌开放类似接口。想象一下，以后 AI 帮你查快递、叫外卖、订电影票……全靠一个对话搞定。

这是 WorkBuddy 100 种用法第 61 篇，持续日更，每篇都是真实场景。

关注我，一起探索 WorkBuddy 的更多玩法。

#WorkBuddy #AI工具 #麦当劳 #优惠券 #MCP协议 #自动化 #效率提升 #技能市场 #AI点餐 #WorkBuddy100种用法

引用链接

[1]https://open.mcd.cn/mcp

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN8OL1q8jlib6Ac31yOvd4B19yEicJKLNsC7W4EGJ4icm2DicKQbxk7LF8j5eDKE6iasII7IjmSzRQNGqJedZwmiciaDqR4ync5sryibI0/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN3dn28f0ss6Vzia9phFSoibfZc4OCZuuK3AQH1C4h4UCRiarKQ7p76H92EPJKhiakNiaZoYVMTqyl02vyeLe1WUYl1r2a4PiaFCyiaiaA/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM97mFj2CDuGPWAEUNYCN1lfMruNEjnrvKeAVMFCDm1YsibhISE1lEXHrZoDAVRNZGrIic2X46wj6Jhf2Rknpo3U2lZIicTFKzhZI/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROhgIGhbsKJ3rG7gwRCudicS6sobLxSCw7Obw88VJKMyMpDG4Do0cEiaPEGwlH4aacSyKMIGQdSShSxIoiaMnKgDLNicsZUSCvOzoI/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROKLXEqXamHATEQHmMoN6qLeMXibXHG1bdv7mtvPE5pAe0s1yWNsH8pfsd4jdkHB9hMNvOZ1LNs3qvqsic4OdKRicIo8eS7S0uXAM/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROuRntq7RPzxicVoC0QsQxVpU4hKMXKhkLc3Hv0ibt48nrRjUALkicbhWAejDaymOHcgrQt36aShLluwMMZu3EdyibRial1NTuf1T34/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRML6rKTNxMhBIxrCvTyiagDp9iaLylFtjqTzmdI3XjSaMIOmga8TM4XvT4Txf2PuzbcTnEIQpr1aSfplxU3FnPQJib1pianOJ9QSj0/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMy5XLqCTqxnRZ2vNbUqlOEq4yv1ALt452rS3F32vaLKSDyIZr2eXxZFDHcxf24LVnWtcJ1VVlP9dtyxAeLgzfcTHrp0yGDSfU/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbROwicRIvcj7fzQovfibCIp5lO7P7KzxNBItYZibu41ibf2USSme3bnQUspH21nQnrfsOU3jKcwlmFnIrX2xnXhEV9OicrNSFrJ3IdZg/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNy9tGwL3YGR82lxsdJQPl8C8cpdL2gvRcsRUlic6MIkic2sHBGTrxkO1qQjW9fsRBpTS0GWRxFv6ibbPK9Cl3pOKWfaHU3bqWal4/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNVA25q3aM4RrSQ7eEPBa8cQwftP71dnnteTO9ECIXVpOkfbDwribGFbL3AmS8zD9qwWALy2G3DucRCpTIru5kw7RNMZHdpwhiaY/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPDsibVwvGpviajx8OibRYnIibz1jLrgpaE2wDmynl4InbdbfsEOALvsdgpXHDnCCQOmfKMrSCBdqGicb7ZLF3omhAOFH2d79nluuXU/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPfShXwKxJHr8QwFCicdiaLX6DLRUxTGxeRjoicXv3gwmfUibK2DPAp7Kdfic3DJH2LIgmKAibibCYTSeEtfUS0OrJO3tZeg4cQ7lNZSY/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPdQB9sOaiabv5yWcR3Q5EVbWAZmr6XgBYu9qsZfYPReCw83ic0d0iblsic723hg8rvGMZyRicg0frQlXAzFibichBq90gluWPricDPWXI/640?wx_fmt=png
