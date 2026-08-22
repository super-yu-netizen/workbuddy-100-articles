# WorkBuddy 100种用法 #45 | 折腾半天，终于让 AI 翻开了我的微信读书

- 合集序号：45
- 公众号：我与ai的那些事
- 发布日期：2026-05-15
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328959&idx=1&sn=c96bec35ae91f2b97e3869d6e7852e5a&chksm=88303238bf47bb2e59b51db67ae695edb5b8fa4e3a568dbf4d1037bbea31c7d64763b0fc6dc6#rd
- 正文字数：3142
- 正文图片：11

## 摘要

手把手教你怎么用MCP把WorkBuddy连上微信读书，中间踩了三个坑，最后成功让AI一句指令就帮我查书架、搜笔记。

## 正文

我打开 WorkBuddy，问了句：

“

workBuddy 如何接入 微信 读书mcp

WorkBuddy 给我解释了 MCP 是什么，然后说网上有人做了微信读书的 MCP Server，npm 包叫 mcp-server-weread。

我回了一句：

“

你帮我全局安装，并配置，我去获取cookie给你。

WorkBuddy 直接执行了：

npm install -g mcp-server-weread

装完之后告诉我：全局安装成功，现在需要你去获取微信读书的 cookie。

我去 Chrome 登录了 weread.qq.com，从 F12 开发者工具的 Application 面板里复制了 cookie，发给它。

这是我的第一版 cookie：

“

wr_skey=oCJUXSVR; wr_vid=39829589; wr_gid=268425945; wr_fp=1822681908; wr_rt=web%40Yjcdm1uItuka9fedMqf_AL

WorkBuddy 收到之后，把这个 cookie 配进了 ~/.workbuddy/mcp.json：

{
"mcpServers":{
"mcp-server-weread":{
"command":"mcp-server-weread",
"env":{
"WEREAD_COOKIE":"wr_skey=oCJUXSVR; wr_vid=39829589; wr_gid=268425945; wr_fp=1822681908; wr_rt=web%40Yjcdm1uItuka9fedMqf_AL"
}
}
}
}

然后说：配好了，重启一下 WorkBuddy 就能用了。

“

配置完，我紧接着问：

“

我的书架有哪些书

WorkBuddy 搜了一遍工具列表——没找到 weread 的 MCP 工具。

它说需要重启 WorkBuddy 才能加载新的 MCP 配置。

我重启了。

重启之后再问：

“

我已经重启了，现在看下

WorkBuddy 又搜了一遍——还是没找到。

“

找不到工具，但 cookie 刚刚配的，不应该是过期啊。

WorkBuddy 决定跳过 MCP，直接用 curl 测试一下 cookie 能不能用。

结果报错了——errcode: -201，认证失败。

cookie 过期了。

我给的 wr_skey=oCJUXSVR 是一个已经过期的登录凭证。

“

WorkBuddy 建议我重新登录微信读书，再拿一次 cookie。

但中间还有个小插曲。

WorkBuddy 在排查的过程中，搜到网上有人做了一个 CookieCloud 同步工具，网址是 cc.chenge.ink，可以自动同步 cookie。

我试了一下：

“

https://cc.chenge.ink[1] 这个网站都打不开

这条路走不通，还是手动来吧。

“

我从 Chrome 的 Application > Cookies 面板重新复制了 cookie，这次特别注意确认登录状态是活跃的。

新版 cookie 发给 WorkBuddy：

“

wr_skey=MAHO7y0e; wr_vid=39829589; wr_gid=268425945; wr_fp=1822681908; wr_rt=web%40Yjcdm1uItuka9fedMqf_AL

“

你看这个可以吗

WorkBuddy 拿新 cookie 用 curl 测了一下——这次成功了，返回了我书架 54 本书的数据。

“

但是，MCP 工具在 WorkBuddy 里还是搜不到。

虽然 curl 能通，说明 cookie 是对的，但 MCP Server 本身没有被 WorkBuddy 加载起来。

WorkBuddy 查了启动日志，发现日志里完全没有 MCP 相关的启动信息。它怀疑可能是 WorkBuddy 没有正确识别 weread 的配置。

这个阶段我一度以为是不是配置文件格式有问题，或者 npm 包没装对。

后来我看到了原因。

WorkBuddy 里新配置的 MCP Server，需要在设置界面里手动点一下信任，才会真正启动。

光写进 mcp.json、重启 WorkBuddy，是不够的。

新加的 MCP 会被 WorkBuddy 识别到，但默认处于「未信任」状态，不会运行。你要在【MCP 服务管理】里找到它，手动点信任，它才会被启动。

我点了信任。

然后跟 WorkBuddy 说：

“

我重启了，你现在看下我的书架

这次 WorkBuddy 搜 MCP 工具，终于搜到了：

mcp__mcp-server-weread__get_bookshelf
mcp__mcp-server-weread__search_books
mcp__mcp-server-weread__get_book_best_reviews
mcp__mcp-server-weread__get_book_notes_and_highlights

4 个工具，全部可用。

“

工具通了，直接查书架。

几秒钟，结果回来了。

52 本书，带完整的分类、阅读进度、阅读时长、笔记数量：

书名

作者

进度

阅读时长

笔记

《人民的名义》

周梅森

99%

5小时45分

-

《精进》

采铜

31%

2小时17分

3条

《你一年的8760小时》

艾力

21%

50分钟

1条

《一万小时天才理论》

科伊尔

9%

18分钟

1条

《我喜欢这个功利的世界》

咪蒙

100%

5小时2分

19条

统计：

-
未读 44 本 | 在读 7 本 | 已读完 1 本

-
付费 39 本

-
有笔记的 5 本

-
最大类别：影视原著（10本）、个人成长（8本）、商业（4本）

“

回头看，踩了三个坑

坑1：cookie 过期了

给的第一版 cookie 里 wr_skey=oCJUXSVR 是过期的，curl 直接报 -201。必须重新登录再拿。最靠谱的方式是从 Chrome Application > Cookies 面板直接复制，确认登录状态。

坑2：外部工具网站打不开

搜到有人做了 CookieCloud 可以自动同步 cookie，但 cc.chenge.ink 根本访问不了，白折腾了一趟。

坑3：MCP 配置完要手动点击信任

这个最隐蔽。mcp.json 写对了、包也装了、WorkBuddy 也重启了，但工具就是搜不到。因为新 MCP 默认不启动，需要去设置里手动点信任。这一步没有任何错误提示，完全靠你自己发现。

WorkBuddy接入微信读书MCP

如果你也想让 WorkBuddy 连微信读书，照着来：

1. 安装 MCP Server

npm install -g mcp-server-weread

2. 获取 cookie

Chrome 打开 weread.qq.com，确认已登录，F12 > Application > Cookies，复制这 5 个值：wr_skey、wr_vid、wr_gid、wr_fp、wr_rt。

3. 配置 mcp.json

编辑 ~/.workbuddy/mcp.json，在 mcpServers 里加上：

"mcp-server-weread": {
"command": "mcp-server-weread",
"env": {
"WEREAD_COOKIE": "wr_skey=xxx; wr_vid=xxx; wr_gid=xxx; wr_fp=xxx; wr_rt=xxx"
}
}

4. 重启 WorkBuddy，手动信任 MCP

重启后在 【MCP 服务管理】 里找到 weread MCP，点信任。别忘了这一步。

接完之后，你就可以直接问 AI：

“

查一下我的书架 我在读什么书 搜一下我笔记里关于「认知」的内容

全部一句话搞定，不用打开微信读书 APP。

MCP 的意义就在这——让 AI 从一个只会聊天的工具，变成能操作你各种服务的助手。微信读书只是一个开始。

你有没有想让 AI 连接的服务？评论区聊聊，下一篇可能就是你的场景。

这是WorkBuddy 100 种用法第45篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #MCP #微信读书 #AI工具 #效率工具 #读书 #书架 #AI助手 #自动化 #npm #WorkBuddy100用法 #微信读书MCP接入

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO6AAkoLkwdibOb68hFzcaGlSvmfkgdYX8SEKbtwqxLqkFlic1a38zX9EJzmBZFNk4ppQerKTd5FP0JTdF619ZcMGVYcCcTcoO60/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPkUu5ahgtzPpnxIEvzicOk0PIptkGgx4ATLwzF5ff8WsGuBplIt2ZgDJWGMAMzOf09WpCbImCfBJCVoBibFKxJMeHEK4ccdlc0k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM1cTN7BPOuN5GSSoYEEEmamLAxaHWFHCic4fg9jSdceNzRWJcqKAIGJ7Ficzj8LnVLrC9ibLGOOoXXbS9VlIco0ZL8oMBt7HPjxU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPnibukibduAbKIKTCSVzNIRGKjh8Kic0Akllib64DgOmGumqmjWqo7egIDHGbW9OaO2ibRmPPD47pFjxu95tVicS6JMHFEX1CGJVXeU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN2pibpprL0arU0T776XDouHUo57Gl16PI3Ka269tnIkyMWmAkrDAU6xN0UOUy9mD3RNuePby8DomQmT2X1IpEFJ9qkCDYMibCCE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPdAANxia89OGtt76SFk1Z08MsFcltV5EL0zDI6VtgiaWviaQO6R53LYHV1Na5z4n2yJLFjn1BjkkCakmjGov0uS3BP3gxzlk1w3k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNB6iazhLzwOaCQMJW3oiaJ81Xy5tzcFG0t1IQa4ZYTQebJxANEMDuf57LLxKeWfvkSppLqMWNwKwiciahXWABibbM7NicTqfNLSYrEk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPPIqwmt8JXL2mibkb4ZqIpr30JobnETvJd6PsS6G9qR6bsHmd48FmEib3QZwiaEZqzTZZafwGEXkiaGDibF6IHFaAauYxCG3k9MqNw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMdPuEhTZTVrq3CtMPjv1cH1qwoDCJlDrogcA198P86icccGepEzLbw3rDMmHXQ4Bhr3DxD0t7zd14LNukQ2U6pScA6C7aNyRKc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN0MZVjMj1x8L0CRo5WtRlNuDwqOjNtfkW0NZFuAibFIPYQTZlaAYTIEtIIovjmePl657qJ7y9NzV9AL7XCOzJ6dUCl2icibwhngA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPSiazF3YDRnOKib8KZCbCCVibic45Goia6kmBuEJM3akf4cWQ3yOaxwibw0P62cApNCFpugxFwv8y1wAb2ibEPqOfwFUrsebdyETpobc/640?wx_fmt=png&from=appmsg
