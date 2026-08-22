# WorkBuddy 100种用法 #64 | 白嫖！接入 Agnes AI 免费模型

- 合集序号：64
- 公众号：我与ai的那些事
- 发布日期：2026-06-03
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329328&idx=1&sn=1e4b8ece2dca7eb60ea0fedb86e29f0a&chksm=883034b7bf47bda1dadd457ae256c05bee04f7505367e9f9f74dc6c0dcefc126397aa365beb7#rd
- 正文字数：1589
- 正文图片：8

## 摘要

注册 Agnes AI，获取免费 API Key，直接把 Key 扔给 WorkBuddy，它自己完成配置。

## 正文

昨天看到一条消息，Agnes AI 开放了免费 API 额度，支持文本、图片、视频生成。

本着"有羊毛不薅就是亏"的原则，我点进去看了一眼。

注册 5 分钟，拿到 API Key，接进 WorkBuddy，直接能用。最爽的是——不用手改配置文件，把 Key 扔给 WorkBuddy，它自己配好了。

下面是我踩过的全流程，跟着走就行。

第一步：打开 Agnes AI 官网

地址：https://agnes-ai.com

首页很干净，直接能看到三大模型：Agnes-2.0-Flash（对话）、Agnes-Image-2.1-Flash（生图）、Agnes-Video（视频）。

点那个蓝色的 "Try it now at platform.agnes-ai.com" 按钮。

第二步：注册账号

会跳转到 platform.agnes-ai.com，直接支持 Google 或 GitHub 登录，不用填邮箱验证码那一套。

我选的是 Google，点一下弹窗选账号就进去了，全程 30 秒。

第三步：选择 Google 账号登录

弹窗里选你要用的 Google 账号，确认授权就行。

第四步：进入后台，找到 API Keys

登录成功之后，点左侧菜单的 Settings → API Keys。

这里点 "Create new secret key" 按钮。

第五步：命名并生成 Key

弹窗里给 Key 起个名字，我写的是 zgedu，好记。然后点 Save。

第六步：复制 API Key（⚠️ 只显示一次）

Key 生成后弹出来，格式是 sk-xxxxxxxx。

重点：点右边那个复制图标，把 Key 存好。 页面一关就再也看不到了，丢了只能重新生成。

第七步：把 Key 扔给 WorkBuddy，它自己配

这一步最爽——你只需要把 API Key 直接发给 WorkBuddy 就行。

它会先显示一条提示："API 需要鉴权才能列出模型。用你提供的 key 来查一下支持的模型列表。"

然后自动执行 curl -s https://apihub.agnes-ai.com/v1/models，用你的 Bearer Token 调接口查模型。

过一会儿返回结果："API key 验证通过！这个 API 支持以下模型："

接着弹出一个多选题让你勾选：

-
A. agnes-2.0-flash — 最新对话模型，速度快

-
B. agnes-1.5-flash — 上一代对话模型，稳定

-
C. 全部对话模型 — 一键全选所有对话模型

-
D. 输入你的答案... — 也可以手动填其他模型 ID

我选了 A（agnes-2.0-flash），点"完成"，WorkBuddy 自己就把 ~/.workbuddy/models.json 写好了。

完全不用手改配置文件、不用管 baseUrl 怎么填、不用管 provider 是什么——WorkBuddy 全搞定。

第八步：重启 WorkBuddy，切换模型

保存配置后重启 WorkBuddy。

对话窗口里点模型下拉菜单，就能看到刚配置的 "Agnes 2.0 Flash:agnes-2.0-flash" 了。

直接切过去用，跟内置模型完全一样。

第九步：测试一下

切换到 Agnes 模型后，我直接问了一句："你是什么模型？"

它秒回："我是 Agnes-2.0-Flash，由 Sapiens AI 开发。"

通了！免费 API 接入成功，响应速度和回答质量都在线。

我试了几轮对话、写代码、改 Bug，流畅度在线，免费额度完全够日常用。

几个注意点

-
API Key 别泄露，models.json 里有你的 Key，别上传到公开仓库

-
免费额度用完会限速，不是封号，正常使用完全够

-
三个模型互不影响，需要生图时切换 Image 模型，需要视频时切换 Video 模型

-
Key 只显示一次，创建的时候务必复制保存

这是 WorkBuddy 100种用法第 64 篇，持续日更，每篇都是真实场景。

关注我，一起探索 WorkBuddy 的更多玩法。

#WorkBuddy #AgnesAI #免费API #自定义模型 #AI效率 #程序员工具 #提示工程 #AIGC #工具分享 #效率神器

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRNXicec4w7heMibPPRuRLYueWR0lGUibIWJkKQVqjCwPFmvDoIBWEibtGxxVVWm41I7Aibl12ZB4R9wX51UceGibzqCicnRX8JR2lkc6s/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRP39DNek1GSF9MKBPBZfVm1EsjdibMzr7J8b8VgugjKQoEnCMibCYoj4Wh5PnaJ3f5sTSMSatSAxRnWX35RRiboT8AW17UYiaia912I/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPQbjEhmOC241mTADJ5r5QI1Z3HiazBEQXfZGWOomP7IEyTNUYdDb00jkP0Wkic3AKG78F6ELxRUULo4x6YibpgZ4JPbP1fHxUeyU/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP6P9HZSaoyukpKcnUWDSuibCMNKo9vwmFeicaEtzA1tgH5Vy9eVgjaCUhOUVVuqBAYt8yLBxibZLvhuPE6WTnmvGf1aVmkuCgQ8E/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPicLSRWIsvjiaHDzzWAFexW0AepSSibyWjibcmv0oHHSt3XMgeDEEFBJoYnn6z2iaK6diaxuRf9nf4LXJBb2SeQicgH1MFNLicpqCfzq0/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO3y0BeBWbLiar6Lia7kElwISibpTL6fW79ibibf77j7Z1pBhou2Oh0GlRPxhrBtI19NqyQs5dicnw9PTyAIVSAqa1KBv9as0Nugia22E/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMuWLgQNL1yicPQt0j60lmOL4V9Z7yWAsGIbPbcN7wEDI2wHsr41m7OFiagqMLz2pKvNK5XgiacO5vX4PFad9rKmD47eIldw5AZB4/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP2eLGNe2aMo4Iib2Syu9ibftdgoglqYrh5nTuvLMGFB9KJzz6l3ia309JKRrCiblNCQEyicMON21GVUZO8xjeQy6NJANibQoUpicbm28/640?wx_fmt=png
