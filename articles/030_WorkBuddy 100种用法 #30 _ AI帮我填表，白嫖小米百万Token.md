# WorkBuddy 100种用法 #30 | AI帮我填表，白嫖小米百万Token

- 合集序号：30
- 公众号：我与ai的那些事
- 发布日期：2026-04-29
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328574&idx=1&sn=5de321d399048605a9de2462bacf167f&chksm=883031b9bf47b8af6b2cb198875d46bf015fd589a07f5ae7f4fdc858cb9ef71ece42aa5524fb#rd
- 正文字数：1639
- 正文图片：5

## 摘要

小米免费送100万亿Token，AI帮你自动填表全程没碰键盘。从找活动信息到填完表单，WorkBuddy接管浏览器自动操作，只在验证码时需要你动一下手指。

## 正文

最近小米AI开放平台推出了"MiMo百万Token激励计划"，免费送100万亿Token。从找到活动信息、到填完表单，全程靠这个skill处理。

下面记录下整个过程，顺便聊聊这个skill的更多用法。

我随口问了一句：

小米的免费Token如何领取？

它连搜索框都没打开，直接给我整理好了：

-
• 活动主页：https://100t.xiaomimo.com/

-
• API平台：https://platform.xiaomimo.com/

-
• 活动时间：4月28日 - 5月28日（赠完即止）

-
• 怎么领：填申请表单 → 等3个工作日 → 收到邮件 → Token到账

不需要我翻网页、逐字抄，一问一答，信息全齐了。

02 能不能帮我填表？

活动页有一张复杂的申请表单，需要邮箱、AI工具、底层模型、项目描述……

我直接问它：

你能帮我填写吗？

它二话不说，用 playwright-cli 技能接管了我的浏览器。

它先问我要了邮箱

这是最让我意外的一点——它没有瞎填，而是先问：

你的邮箱地址是什么？

我告诉它：wwwczgedu@126.com

确认身份后，它开始批量填写所有字段：AI工具选了Claude Code、Cursor、OpenClaw，底层模型勾了Claude、DeepSeek、GPT，项目描述自动生成了近300字，还附上了GitHub链接。

整个过程，我只提供了我的邮箱。

03 验证码这道坎，绕不过去

第一次：卡在滑块验证

填完提交，系统弹出了滑块验证。

AI脚本直接卡死——它能填表，但过不了验证码。这很正常：验证码本来就是用来区分人机的。

我让它把浏览器打开给我看

我让它切换到可见模式，让我亲眼看到它在操作：

你能不能打开浏览器，填写，让我看到？

它立刻把Chrome窗口弹出来，我能亲眼看到它逐字段填写、勾选选项、敲入文本。

第二次：提交时又弹验证码

更离谱的是——提交时又弹了一次验证码。

这次它直接告诉我：验证码又弹出了，你自己在浏览器里完成滑块验证然后提交吧。

04 手动滑动，提交成功

最后一步是我自己滑动验证，然后点击提交。

成功了。

现在坐等邮件通知。通过后用 wwwczgedu@126.com 登录平台领Token。

这个Skill还能用在哪里？

playwright-cli 的本质是让AI控制你的浏览器。围绕这个思路，所有需要操作网页的场景都可以自动化。

1. 填表场景（最常用）

-
• 求职申请表：批量填写，一套简历投100家公司

-
• 活动报名：抢名额时自动填，省去反复复制粘贴

-
• 测试账号注册：开发阶段批量注册测试账号

-
• 网站备案：工信部等需要大量字段的场景

2. 内容抓取场景

-
• 竞品价格监控：定期抓取竞品官网数据

-
• 股票盯盘：价格到目标位时自动提醒

-
• 文献搜集：按关键词自动搜索并下载论文

-
• 舆情收集：监控特定话题的最新报道

3. 自动化操作场景

-
• 批量上传文件到网盘、图床

-
• 定时签到、积分任务

-
• 批量发邮件、批量回复

-
• 社交媒体定时发布

4. 网页测试场景

-
• UI自动化测试：验证表单、按钮、交互是否正常

-
• 截图存档：定期保存网页状态，用于对比

-
• Bug复现：还原用户遇到问题的操作路径

5. 企业内部场景

-
• ERP/ OA/ CRM批量数据录入

-
• 内部报表自动下载整理

-
• 重复性工单批量处理

写在最后

验证码是AI永远过不去的坎——但这恰恰是它的价值所在。

如果AI能100%自动过验证码，那验证码本身也就没有意义了。验证码的存在，天然划定了AI和人的边界：AI做它擅长的（理解、填写、批量），人做人擅长的（验证、确认、最终决策）。

这次填表，AI完成了90%的工作，我只需要动一下手指滑动验证码。

最好的协作不是替代，是分工。

这是「WorkBuddy 100种用法」系列的第30篇。

持续日更，每天解锁WorkBuddy的一个新玩法。

如果你觉得有用，转发给身边需要的朋友，欢迎关注，第一时间收到更新。

#WorkBuddy #小米Token #AI自动填表 #playwrightcli #网页自动化 #AI工具实操 #MiMo激励计划 #表单自动填写 #浏览器自动化 #AI效率办公

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN7ib6kicrHSKYyFACIBeUF3EJusNzFnCdwfzoicYacqDicSjwbCOT6Xu1EFrGiaSH42tSX9o3neEhzyAzxcIXYy4mFzFn8CbUwIvLY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPDKWe860hAPvfZeB6yhyK22rL3c6XNa0fbM3UWNXnPd2ejXEKtdES7uI89sk1T0kL0U71CByiaLbbSicibZUnZ9cLrjNGBq5Xk2w/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROCCnS1Fu51qia8dbqLsGGve3DyTxyboK3HQuzQuCnEhZoHsd8AnLvBe8hoNVooOibQe401y1HMfIKuPjvTRe5WoGVTjZoJTfHFo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPAts1yiagmFQOXK8viabx1dth9cyboUPT6Mh64k0DTntjkUZjYrLcC6RgFOvQKurnIicMzRxb4yiaz7tUt90RMNFmCy2sqasn7DxU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM6R4rd6fQibIOu8VnDXcZJU4mT5Ytm9v4icicgSwm9ADAB5mMqV0pFuhXkiaE4tZdMbFiaBoNGzVnMfKGUt06nLOZnXLXAlFwKXfN0/640?wx_fmt=png&from=appmsg
