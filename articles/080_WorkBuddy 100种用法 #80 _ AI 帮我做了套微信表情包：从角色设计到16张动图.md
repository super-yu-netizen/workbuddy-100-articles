# WorkBuddy 100种用法 #80 | AI 帮我做了套微信表情包：从角色设计到16张动图

- 合集序号：80
- 公众号：我与ai的那些事
- 发布日期：2026-06-19
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329796&idx=1&sn=972f92760d90889e77a0237153300867&chksm=88303683bf47bf950a25f2af2301ac07a1e21a6a3dc6a69207ca7cf10db4a423b292b9b5832a#rd
- 正文字数：2310
- 正文图片：44

## 摘要

不会画画也能做微信表情包？用 AI 从角色设计到批量生成 16 张动态表情、透明背景处理、配套素材生成，再到平台提交审核，全程没开 Photoshop。附完整工具链和实操截图。

## 正文

上一篇WorkBuddy 100种用法 #79 | 从零搞懂微信表情包上架：注册·规格·流程·避坑一次说清把规格、流程、避坑都搞清楚了。接下来是真的动手做。

今天这篇，你会知道：

-
• 怎么让 AI 设计一个专属 IP 形象

-
• 静态图 vs 动态 GIF，技术路线怎么选

-
• 16 张表情批量生成，全程用了哪些工具

-
• 透明背景、配套素材，怎么一键处理

第一步：先有个 IP 形象

规格搞清楚了，但第一个问题是——做什么形象？

我跟 WorkBuddy 说：

我：「我没有明显方向，你可以针对我的身份和我的公众号定位，帮我设计一套方案出来吗？我想使用 AI 生成。」

WorkBuddy 从我的资料里提炼了关键信息：

-
• 公众号 「我与AI的那些事」，定位 AI 工具 + 效率技巧

-
• 正在日更 「WorkBuddy 100种用法」 系列

-
• 形象叫 可乐，数字搭子 🛠️

然后给了我一套方案：蓝灰色企鹅 + 圆框眼镜 + 键盘挂件，二头身 Q 版，扁平手绘风格。

「可乐」这个人设就这样定下来了。

第二步：AI 生第一张角色定型图

方案有了，下一步是出图。

WorkBuddy 直接调用混元生图，出了第一版「可乐」：

我看了说：要无水印的啊，记住了，全部需要无水印。

于是换用混元生图（支持无水印参数），重新生成：

蓝灰色企鹅 + 圆框眼镜 ✓，键盘挂件 + Hello 屏幕 ✓，没水印 ✓。

风格确认，可以批量跑了。

第三步：静态还是动态？

角色定了，下一个问题——做静态 PNG 还是动态 GIF？

我问 WorkBuddy：

我：「我想生成动态的 GIF，能搞定吗？」

WorkBuddy 给了两个技术路线对比：

路线

怎么做

效果

A：文生视频 → 转 GIF

混元生视频 → 下载 MP4 → ffmpeg 转 GIF

动画流畅，适合简单动作

B：逐帧生成 → 合成 GIF

每张单独生成再合成

精确控制，但帧间可能跳

选了路线 A，先试一张看效果。

技术验证通过：

-
• 混元文生视频 → 自动下载 MP4 → ffmpeg 转 GIF → 压缩到 319KB（≤500KB ✓）

-
• 240×240 正方形，符合微信审核规格

但有个问题：视频生成没法做透明通道，背景是白色实底。微信不强制透明，但透明背景体验更好。这个后面再处理。

第四步：批量生成 16 张

第一张效果 ok，我直接说：

我：「继续按这个风格跑完 16 张。」

WorkBuddy 建了任务列表，分批生成。覆盖的日常聊天场景：

#

表情

大小

状态

01

你好

319KB

✅

02

好的

355KB

✅

03

谢谢

297KB

✅

04

收到

219KB

✅

05

加油

312KB

✅

06

晚安

274KB

✅

07

哈哈哈

330KB

✅

08

疑问

298KB

✅

09

委屈

303KB

✅

10

生气

274KB

✅

11

摸鱼

296KB

✅

12

点赞

281KB

✅

13

难过

318KB

✅

14

惊讶

307KB

✅

15

偷笑

324KB

✅

16

拜拜

311KB

✅

16 张，全部符合微信规格，全程 AI 生成 + 自动压缩。

第五步：处理透明背景

全套图出来了，但白色背景在聊天界面里有点突兀。

WorkBuddy 用 泛洪算法（Flood Fill） 从四角扫描，把白色背景像素全部替换为透明：

-
• 企鹅的白色肚皮保留（被轮廓包围，泛洪到不了）

-
• 16 张全部写入 transparency=0 标记（标准 GIF 透明格式）

处理后文件大小：61KB ~ 126KB，远低于 500KB 上限。

第六步：生成配套素材

主图搞定了，但上架还需要 4 类配套素材：

素材

尺寸

大小限制

表情缩略图

120×120 px

≤ 50KB

详情页横幅

750×400 px

≤ 80KB

表情封面图

240×240 px

≤ 80KB

聊天面板图标

50×50 px

≤ 30KB

这张图如果用 AI 重新生成，风格可能不统一。WorkBuddy 的做法是：从主图里截取「可乐」的形象，重新排版，保证 IP 一致性。

工具链总结

回过头看，整套流程用到的工具：

环节

工具

用途

IP 设计

WorkBuddy + 混元生图

角色定型、风格确认

动态生成

混元文生视频

生成动作视频

格式转换

ffmpeg

MP4 → GIF

压缩

TinyPNG / ffmpeg

压到 ≤500KB

透明处理

Python + PIL

去白底

配套素材

WorkBuddy

自动截取 + 排版

全程没打开 Photoshop。

第七步：提交审核

素材全部就绪，登录 sticker.weixin.qq.com 开始提交。

第 1 步：选「表情专辑」

进入「我的作品」，点右上角「提交作品」→ 选「表情专辑」。

第 2 步：上传表情

类型选 动态表情（GIF 格式），批量上传 16 张主图。

右侧实时预览效果——能看到整套表情在聊天界面里的样子。

第 3 步：填基本信息

-
• 名称：可乐的日常（5 字）

-
• 介绍：可乐，一只会写代码的小企鹅，陪你聊天、工作、摸鱼～

-
• 横幅：750×400 px

-
• 封面：240×240 px

-
• 图标：50×50 px

第 4 步：填附加信息

-
• 类型：卡通表情 / 其他

-
• 风格：日常 + 搞笑（可多选）

-
• 主题：万能通用

-
• 上架地区：中国大陆 / 全球

点「提交」，等审核。

全程回顾

从「我想做一套表情包」到「已提交审核」，完整链路：

环节

工具

耗时

了解规格 + 流程

WorkBuddy 对话

10 分钟

IP 形象设计

混元生图（迭代 2 版）

5 分钟

批量生成 16 张动图

混元文生视频 → ffmpeg 转 GIF

~30 分钟

透明背景处理

Python 泛洪算法

自动

配套素材生成

WorkBuddy 自动排版

自动

平台注册

微信扫码 + 邮箱验证

3 分钟

填信息 + 提交

sticker.weixin.qq.com

5 分钟

全程没打开 Photoshop，没花一分钱外包。

如果你也想做一套专属表情包，可以把你的想法丢给 WorkBuddy，它会从 IP 设计到生成全程带你走完。

这是 WorkBuddy 100种用法第 80 篇，持续日更，每篇都是真实场景。

关注我，一起探索 WorkBuddy 的更多玩法。

#微信表情包 #AI生成 #WorkBuddy #表情包制作 #动态表情 #GIF制作 #混元生图 #公众号变现 #微信开放平台

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMQOVhodJBoviaXYI3tTgnBDuuuSS8ZFzqo5icE9DRRYcbEpGPgODOt3X1YnA4dNru07FBQFgsZhXNob2CR4QEKicdo0aoGQx0E3U/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMWHUz9BdxRlcLZEszpsS0ym0E2mVJkFeotKBZicX0UU59tDIOvxBFgcOrYg7srga65YlE2Z6icq0pNAzbqtQEo4WC0hDtic8tTNw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNJ8gr2fLswmibt4khBXA9YHRL7ic07UV064bmhPrZFa3ZQ5n11B8ElOGz04xxXpp2nzrnJfSuhHtFBaqrPEPauMvbZSCqKC9Ofs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP4cCefGWnRHuV2D4NfWtKdbJia8sglhaN87cERf4t2Z22KlYwhulwpDPoZYEbI8JppD2JrzqJqOINhU8SiaNDKhAYeOKdyIw8pM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP6b9PYdjLGf29pT596e6oiaSco8Ziapp7VLrhnP97KxM6K4vDWNPdlBVGvEEVfASa9CRGD77wpFXmST9sYN951Q6Xyb9hdphFgQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRPEL8G52ghhYZBW9nibQjdtxabiceHXRnWSLuwkFxEr5ra2eueRSF8k51nlkyicWfG9aYxhIyeo8hgaQLtrpucIVCVewoOctRoBTE/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPMUwmgJLwEnhsI9DYqUwuNlmR2JroibEpwWrPx71j7Ctr1lVfjdLfUH4erbvCvptwx9AibSo1Kib4hH9HGoz21MSuDDFZ1QB227s/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRMbZmawnXUUck4je7EXz7iauxumAVprh20AppRN4PSH7ia3OiaSeOQoukFoV9ia1Wibtnf5GRIf6zibtVuEibFeHMGyKCWxxpoOfvJGnk/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRPHYkXNC6j2WKuWRRYAp4t16GcL97V9ic7KEPohWFABFNUUm6NOxvibpYffRk7y24TVZHOCZyQJ24DmU1MTAFRKDJT9ZB0f8lMlk/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRMBBJFz8O4bKiaRnz4Ko84VAibiczTPeC9oG8Rragia4nppxEZTPibhnzeubHoqiaPcX7goUKvcwW7mKFdgAydqf4r25Xb7x4zJajXwc/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRM29maSsdXda5AvH5H5QZbYOqSTeqia64xohlQ7LYgUQnLAfWCpfRib9QUmWaRcfKhCacRNWcdnp7kdsW2IZibIicvOc1YXicjK73LE/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRNfTh87AyicrJSozezoEGpvnrXVncAflibpw1dQxdkXJ3wI8CbWIEdEcecXCHC6qcmdfohLichbRCsCibDFWUmw1ICbIWwI0EjVbCw/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRNlMcpU8T3yWPWWumHw2JScR5zuxfyXDzsg3csNuDqibkGZEXkjz5zQ41GOibuDCOqwYJ692D7mOO4ZT2hStBxEwI0np5NmOMgics/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRPeDPhayoAKqibGa7ib4sichHt3LlNSQ9tbTbysm65uAL7YZ8Hcz7eF3Ia6jL1Kt1gsmD9DQUC75YDXhkMUfCdYNI2BBNo2ub2bKE/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbROTGC72Ywj8Gqrt69j3vWkIAutGwaIOcicxtbq9Bnz1MtOGadByicPN8ypONNxGeNcZACjpNRCnAZGCDtzegbrvw71UwyregdCVM/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROl5bQccoqHmhrUMRJA1ybiaZXrQm9WEocGiaHfmricO1xWzdicibPm8kzho2yjAllhn1dL5tAibshpzxpaKMLH538QyT1vSW5FhY4rs/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRMUxoXrp5wRJzxoibyaUdnXeBI9SNHhPBY54DeGpHxQ5CxjNgRD4Eibriclodz1nHkpho4sibhEhPp8Ajq6KCefvthXHicbeV311hSA/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbROOiclaRulApDlJRcmsp6GIzPCnJqSlUrEJpvD7YDibU0gUfwwiarTibbQBpuXauFibuvPjTHV4sCPesr7TkpCtXz6OAXIpU2QicibJvU/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRPLY6HX8eQwFTnegaMKHQtptxtHQXqdeOuU1V4XwKbY6DuYtA1INad0LFHvwfakRY2RKojkAvyv74q52zpfsLacSED8fVcshiaI/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRPP82ricYDLeXud1NuWB1elvnXZJibfjiazutNEDAOWBrCIYFeMV2r3EMHWINcYNTXaM1Tv3qr5Xb9APqStPt2A7TGcHJAaX4cJicg/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROunJqqlwkMluRzHiaqa4pkZRwqSUSGv0ZRaXfLOtT9HlImbLVWh9Qge83KTDMD1m6k7ic4spGC4yQUGH4tjGH1ZWmf79TJD2kiao/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRMibC0vxULeIoiczxCJ8awQmF1iaUUEJvALSib1qzsbC3BHOrASD9PlTwVEEaHnxv2GR0QS6Ozg7K9Z1nR4JfC65986kAnMrINqUqU/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRPJFsEAbnqI2jxjSt42JPpyD4whrpIILrPFKd9sgnnVWoX9ibvTibTgxnyuVt6RgbW1bWEZVqTg36yds7xo4rNnvgpxKuJe4icrac/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRPbJHoVAzI2CywOy2vRK7c8ny9USONcmNXuFxCNz3PrAiaTqRb4qcFM0SWRT1KISwEkjQbXw1LfOp3Llmhl3w6WRvLR77JHm6ia0/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbROM7iapuR4mvLnuAOvwG1eCSJ6IWPvlPoicY1dTyhEm9HfnsShaUXnzxW39JvlMqwG0BJSPzeIF1QtgjYMMIjI0Qh1mNdjsRa9D8/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRMDzrSDc5zwCicDeU905LY0Xu0zCbUOLndEGVBqmpP78STjic1e5Z7NcWK30Gz4IAicsGwRqibVCfR29OhDol7gaoQp0osIOQfXJW4/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRM7niabtqVrWC5O8paibKMOFcZiaQvxx1j1t4BqPLUJsiaeAFyvFlBQYVKlicn94icCyC4oBXxiahIb9WJhwbFY5y1OSmeuOBzEcakgVo/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRO6yKSV72bch84UGR5bsfRGlhyp4ic5QvsC5axTeQgicNJl5TCdwWngguqd6icIeaKQO1lonicSpyqm3DbMxJyJ582gjatfCibW0nDk/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROZiaGcDTQGHEI0v5c0yPWr8fYvXhl37BicTFFIicgnGvz4HKPCmrwUpsbTgHKONY0Gcx1SfFN12DB7ibv3EoLFRxM0GwN5d2R0KAY/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRMXeBJB1qx42yictKY5gNdc10ic5LnKT2t7oXqoMxRkSiavP0GFlMTCNnaVCqnn27HrmnMibQQnd6EKc8h8gjIVMCoXl5jicGibVtIwI/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROIictnZukzibNFeYaEfAdYibIYbWpnzDYkRgVTuia0Rq1b14D7ickGZonfKTKsJHUwRxCP0PG5HjGGlZIiaVn0WIUsYlSeJbTKDRrh0/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRPiafxFF6gFpFZsoyEPBxXYYiavOEfJX15t05NHGUZhngeZQwyyuSzSiawhsUjOsR9ZefBRqiavxKCmeMNOe8Jmwo0rXGQ8xGTMfPQ/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROs13BHYURHftrKpOOjrbPqdMe9V76JqVIttCZicqQg5VZxgJrV4mibh5lBaYjFd3xSAYpXb8kWHdI8CibCbQ2hDql7CjbvYrhJib4/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRO7ThI8XbBzFtxISmWe7SYwfydSzRCaJFWBWTVROIfVqHOoibs9vrTzq4iaYyQ743ncHykO1X8UpcX4HZFSbUNasfeeqJE1CwKHU/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRPe3C3BqSTQb40Z58OoGdgPrFGNc3VBMWh5cSEzt8xyATdibHwwv7w3O5fRWqsN0QicqjZd3HbJLaNxmoxJ3ZSeOlhT5YewoMEYI/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROJ2cklD5IOgVXOm17WFloJRJUStEiaGRsDJDFbLMQYsdWJiczkCQ0bichFeHvW33XqSazHqReicYWNM0G5VpTXej16LwP5ElpH9bw/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbROyElzaxHKI3BSrx1Dia57Pp5XqayogcDmesRmW4I1Fl9MyMWD1k2I6CTbRicEEcK8YngLvtlJeCTqKicpUzia3PibjrOf4lyaCjwia0/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_gif/s516EMWvbRNlKv1Snwl6R21TgNjSHvHU9ZuPrUrND5Qu7TYXXicOEPTg1XbQaTvQCuibbR6P1WgIWroVMlwvE0LWnibY6SPibPnPDHPOLPC7ic44/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_gif/s516EMWvbRMZCbQxYzKjbYicnXPWx46wYjNtK7viboibolTQCUqicVSRrSBZoCXDdnNZiaAErKrk9nfc3xkGLhicLfRXib2P5f7esPfT2A0YQ8mtpg/640?wx_fmt=gif&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMdnQ9CPVOPwaMHE80tEsYPricAqTBqXBib9hg7TicIy0aeib2diaelk1Kiao4KctIgSbnibyibQmRs1LXibVlK7lDrDavnhMicULJBxNjnE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNGMFdwRlf8HiaKbBg2MZcLUP7PibUTk9VxlfhGoEzPTicvWMwV3gRvGcIna41RDK9r5we8wWKn1jhxWFlOO2wiaVfhVQAOlibmWXUo/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNCLOY70QkSYPXGBPibubpVNUJzgVCnvEslVjZuAQNvQCPticPsViaficeIbt6eibh1Yiae79mPn06iaxiamI5C1iadVLWRbVW7jLrqg9Kk/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPomeOfMClibGcte0M6QKfbtTc1wc7KoRIvEuQYNTXZSV8qiaScGx0ZSH8AVRxtb1AVAV5N0dc4zWZy5Nl9Q5TM2q2kBPvzoAqbM/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMoPPgibrbBH1dZGKYYshTbAkgjVxA7ZBsXafiaGVm8kWu2Z3qD1l5pKYeico9kibHrlo8FrL8aNTuaDcvWa1P5UbvakoaSGibIUTRs/640?from=appmsg
