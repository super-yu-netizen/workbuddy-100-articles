# WorkBuddy 100种用法 #5 | 即梦 AI 接口，自动生成公众号封面图

- 合集序号：5
- 公众号：我与ai的那些事
- 发布日期：2026-04-04
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328039&idx=1&sn=c9e05c5ced16dcc5886df45c1bbbe43d&chksm=88303fa0bf47b6b6b7d7c88541f25a42f4675aed2f3b8300b8174682ba7774c9140143c52ba7#rd
- 正文字数：2319
- 正文图片：9

## 摘要

WorkBuddy 100 种用法第 5 篇，讲解如何开通即梦 AI 免费 API，由 WorkBuddy 自动完成技术对接，一句话生成公众号封面图，实现风格自由与效率提升。

## 正文

在这篇WorkBuddy 100种用法 #1｜公众号封面图，AI一秒给我5张选里，我们用 HTML+CSS 模板解决了公众号封面自动化生成的问题，但模板化的视觉风格始终不够灵活。 最近听闻群里的小伙伴说，即梦 AI 图片生成模型，有 200 张的免费生成额度，还能创造出无限种视觉风格 —— 只要让 WorkBuddy 对接上即梦 AI 的 API，就能让公众号封面从 “模板化” 升级为 “定制化”。 这篇就手把手教你：3 步搞定即梦 AI API 开通，让 WorkBuddy 帮你实现 “一句话生成高质量公众号封面”。

第一步：开通即梦 AI API 免费额度

1. 进入即梦 AI 官网，找到 API 入口

打开即梦官网（jimeng.jianying.com）并登录账号。 在左侧边栏最底部，找到「API」按钮，点击进入。

2. 跳转到火山引擎，点「立即开通」

点击 API 后会自动跳转到火山引擎即梦产品页（volcengine.com/product/jimeng）。 页面上有三个按钮：「立即开通」「产品文档」「业务咨询」，直接点击 立即开通。

3. 在模型广场找到「即梦AI-图片生成4.0」

进入火山引擎控制台，打开 模型广场 → 即梦AI。 在服务列表里找到 即梦AI-图片生成4.0系列，点击 开通服务。

4. 选择「免费试用」

弹窗会出现两个选项：「免费试用」和「正式调用」。 选择 免费试用，点击「去开通」。

“

免费试用包含 200 张图片生成额度，日常运营完全够用。

5. 确认开通

下一步会显示服务用量限额：生成量限额 200 张，开发额度 1，直接点击 确认开通。

6. 开通成功

页面提示「开通成功」，状态变为绿色「免费试用」，说明 API 服务已成功激活。

开通完成后，还需要去火山引擎「密钥管理」创建一对 API 密钥： Access Key ID + Secret Access Key，这是调用接口的身份凭证。

“

注意：Secret Access Key 只在创建时显示一次，务必立即复制保存，丢失后只能重置。

第二步：让 WorkBuddy 帮你搞定全部技术对接

这一步最省心，也是 WorkBuddy 最能体现价值的地方。

我只对它说了一句话： “帮我做一个即梦图片生成的 Skill。”

它立刻给出两个方案：

方案 A：做成 Skill（全局可用）

-
集成到 WorkBuddy，所有项目通用

-
支持对话触发、命令行调用

-
一次配置，长期使用

方案 B：做成项目脚本（当前项目可用）

-
仅当前目录生效

-
换项目需要重新拷贝

-
适合一次性使用

我选了 方案 A，全局可用最方便。

把密钥发给它之后，WorkBuddy 全自动完成：

-
查阅 API 文档 — 自动理解请求格式、签名方式、轮询机制

-
实现签名算法 — 火山引擎 HMAC-SHA256 签名全程自动处理

-
处理异步流程 — 提交任务 → 获取 task_id → 轮询结果 → 下载图片

-
本地保存文件 — 一键保存到本地目录

整个过程只聊了几轮，从提出需求到功能可用，不到半小时。

更省心的是：API 文档太长，我直接截图标注，它看图就能解析参数，我完全不用手动整理。

密钥存储也很安全： 保存在 ~/.workbuddy/config/jimeng.json，权限设为 600，仅本机可读，不会上传到任何服务器。

第三步：一句话生成公众号封面图

配置完成后，生成封面就变得极度简单。

我只需要说一句： “根据这篇文章生成公众号封面图。”

WorkBuddy 会自动完成一整套流程：

首先，生成背景图。 它先分析文章内容，自动生成一段高质量中文提示词：

“

一张干净的工作台，左侧是一台笔记本电脑屏幕显示着AI对话界面发出柔和的蓝光，右侧是一张精美的AI生成图片悬浮在桌面上方，两者之间有一条发光的数据流光带连接，背景是深蓝紫色渐变带有微弱的光点粒子，现代扁平插画风格，横版宽幅构图，明亮干净，电影级画质，不要任何文字和logo

确认提示词后，调用即梦 API 生成高清背景图。

然后，用 HTML 叠加标题文字。 因为 AI 直接生成文字容易乱码或错位，WorkBuddy 用了更稳妥的方案： 即梦负责画背景，HTML 负责渲染文字，最后用 Playwright 截图输出 900×383 标准封面。

就是你现在看到的这张：

整个过程不到 1 分钟，我只确认一次提示词，剩下全部自动化完成。

“

小提示：即梦 API 对图片分辨率有要求，公众号封面 900×383 不满足最小尺寸。WorkBuddy 会先生成 2K 大图（2304×976），再自动缩放到标准尺寸，这些细节它全部自动处理。

和第一篇方案的对比

第一篇：HTML+CSS

第五篇：即梦 AI

封面风格

预设模板，风格有限

AI 生成，无限可能

操作步骤

选风格 → 自动截图

确认提示词 → 生成

视觉效果

代码绘制，简洁干净

AI 绘图，画面精致

使用成本

完全免费

每月免费 200 张

技术难度

低

极低（WorkBuddy 全包）

两套方案互补，可按需灵活使用：

-
想要极简文字风 → 用 HTML+CSS

-
想要高级氛围感 → 用即梦 AI

这件事给我的启发

WorkBuddy 不只是一个聊天助手，更像一个7×24 小时在线的技术合伙人。

以前接入一个新 API，我需要：

-
啃几十页文档

-
搞懂鉴权、签名、加密

-
写代码、调试、处理异常

-
至少大半天

现在只需要：

-
把密钥给它

-
告诉它你要实现什么

-
剩下的交给 AI

这就是 AI 时代真正的效率：不是替你思考，而是替你搬砖。

最后

这是「WorkBuddy 的 100 种用法」系列的 第 5 篇。

如果你也在用 WorkBuddy，或想用 AI 工具提升效率，欢迎关注我。这个系列会持续更新，解锁workBuddy的更多使用场景。

另外，我把本次配置好的 即梦 AI Skill 文件 整理好了。 关注后回复关键词：即梦，直接领取。

拿到后只需填入你的 API 密钥，一行代码不用写，直接使用。

#AI工具 #WorkBuddy #即梦AI #公众号运营 #技能开发 #API接入 #效率提升 #自动化 #封面图生成 #AI绘图

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPVXyfYaO3ibORqV7YHxd55KCn4vMlkvg6IvuEhhFbrYvXumo9upUiacG8zo7y8dibM132wDmk63YgSBZGpNLibdqr7PibW0O8la2fo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNsXicqhS2Cl27PLpmLvSZFNxRQ8hfcm9tPIu4A7icw89YL4V8GDgoUBgn5nYIblE7GlW5guIQb7wSOVgNFvEfM2ygoG0B1xeNUw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROBbbdNKvawTEpS59Mf9FmxPRFIVKmVeibwcycU0gPO0R0liaIKSTvT7zLpRJYjacW0wYvtukiaGibYLBE0MYHUpRoBRe3ebA1pfQs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPafvzS9yzC00lOlWtNt8O9RnP29V2J5Z0KYzEZ5pOaf5oKvFCia8cW73ic7TnVToEw1NRrwkiasiaMQ9rHbPTXwlk8iciab7aqs466w/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMCIUYK2chib8JWJeEqJwr3N45MU4SjVcdPTwAk61yNeUOOzqYvU8YjAmBZ3XBG1RY8xROhGX0jYfNHJC4tCEr7F1ZsCJNZnAug/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP9ZRYtXzQvlYwnXluWTV4U4tR2gaWGdrUqMZRaAzbPfpSSYGUrCHfONCDMKVQ0dDVFpLicxKFyIuk3gsto2ZUWwHj2HYhYCUdI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPd0YMUS89yWJiafq06eM57Y9VqkO22tdQx1x281AiaMvd5COO7iaykrMCOqsGBSLpf7lJicLQjWianBsLIkIW9QdTOic41Hic0X3CnYQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP6byHIcIVFicku0ib7ic5IOUsCHZ8vWxDUk7ibb6UicdTRYzMgA54JlLwBqdjPIsuWRPhhGl0V15JET9c1fBCNfsLLmJgq6T1tHJxw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMibxgEUTMdt9QuvHEBpI05cmsXP8Eicx74mSic2lhdvyMCk9ibVuLvtFTwM1lMnfRfGhZkEZcjZ0TRcDPVB3NuXEnSQ4xiaWAKNvlE/640?wx_fmt=png&from=appmsg
