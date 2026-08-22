# WorkBuddy 100 种用法 #7｜定时任务收不到结果？邮件推送一键搞定

- 合集序号：7
- 公众号：我与ai的那些事
- 发布日期：2026-04-06
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328089&idx=1&sn=a5474a48ea529ae398e83933486b05cf&chksm=88303f5ebf47b6486f2553696417282b1f122a5917515a5244181bc71b73f88f7be79946dadb#rd
- 正文字数：1966
- 正文图片：10

## 摘要

本文分享 WorkBuddy 定时任务无微信通知的解决方案，通过配置邮件 Skill 实现任务结果自动推送，支持远程文件、自动化报告等场景。

## 正文

今天分享昨天一个我踩过的坑，以及最后的解决方案。

事情是这样的

昨天早上我用语音跟 WorkBuddy 说：

"帮我创建一个定时任务，每天早上播报兰州天气预报。"

WorkBuddy 说行，任务创建好了，9:42 执行。

到了 9:42，我问："推送的东西哪里去了？"

WorkBuddy 说任务执行了，但我收不到通知。

问题根源

原来 WorkBuddy 的定时任务只负责执行任务本身，它没有主动推送到微信的能力。

任务执行后的结果只是保存在本地，不会自动发到我微信。

这就尴尬了——任务做了，但我不知道结果。

寻找解决方案

我问 WorkBuddy：有没有类似的邮件收发 Skill？能不能给我写一个 Skill？

我不想要那个脚本，要常驻运行在电脑上，能自动收发邮件的。

WorkBuddy 说可以，然后给我设计了一个完整的邮件收发 Skill：

核心功能：

-
发送邮件（文本/文件到指定邮箱）

-
接收邮件（检查新邮件并解析指令）

-
指令执行（根据邮件内容执行对应任务）

-
结果反馈（把执行结果发回邮箱）

使用场景： 你发指令 → 电脑收到 → 执行任务 → 结果发回你邮箱

支持的指令：

指令

功能

查股价 股票代码

查询股价并邮件回复

查天气 城市名

查询天气并邮件回复

发送文件 文件路径

把电脑上的文件发给你

执行命令 命令内容

执行 shell 命令并返回结果

解决方案：邮件推送

WorkBuddy 给我出了个方案：用邮件接收任务结果。

思路很简单：

-
定时任务执行完，把结果发邮件给我

-
我打开邮箱就能看到

-
不用依赖微信推送

具体实现

我让 WorkBuddy 帮我创建这个邮件控制器 Skill。整个过程是：

1. 告诉 WorkBuddy 需求

-
邮箱：126 邮箱（xxxxxx@126.com[1]）

-
功能：发送邮件、接收指令

-
场景：微信触发任务，邮件接收结果

2. WorkBuddy 创建 Skill 框架

WorkBuddy 在 ~/.workbuddy/skills/email-controller/ 目录下创建了以下文件：

email-controller/
├── SKILL.md # 使用说明
├── config.json # 邮箱配置
├── requirements.txt # 依赖列表
└── scripts/
├── email_sender.py # 发送邮件
├── email_receiver.py # 接收邮件
├── command_executor.py # 指令执行
└── monitor.py # 持续监控

3. 配置邮箱授权码

126 邮箱需要用授权码（不是登录密码）才能被第三方程序调用。获取步骤：

第1步：进入设置 登录 126 邮箱网页版，点击顶部「设置」。

第2步：选择 POP3/SMTP/IMAP 在设置菜单中找到「POP3/SMTP/IMAP」选项。

第3步：开启服务 找到「IMAP/SMTP服务」，点击「开启」。

第4步：安全验证 弹出安全提示，点击「继续开启」。

第5步：手机验证 输入短信验证码，验证身份。

第6步：获取授权码 验证成功后，会显示授权码（一串16位左右的字符）。

⚠️ 重要：授权码只显示一次，务必复制保存！

4. 自动配置完成

我把授权码发给 WorkBuddy 后，它自动完成了所有配置：

-
填写 config.json（邮箱、授权码、服务器地址）

-
安装依赖（yagmail、imaplib2）

-
发送测试邮件

我只需要提供邮箱地址和授权码，其他都是 WorkBuddy 自动搞定的。

测试效果

让WorkBuddy把电脑桌面上的png图片， 发送邮件到我的 126 邮箱。

我在手机上打开邮箱，成功收到了这封邮件：

测试成功！说明邮件 Skill 已经能正常工作了。

扩展应用场景

解决了定时任务推送问题后，这个方案还能用在更多地方：

场景1：远程取文件

人在外面，需要家里电脑上的文件。

微信上发指令："把桌面上 report.pdf 发到我邮箱"

WorkBuddy 执行后发邮件，附件就是我要的文件。

场景2：自动化报告推送

每天收盘后：

-
查询持仓股票数据

-
生成分析报告

-
自动发邮件给我

早上睁眼就能看到报告。

场景3：耗时任务完成通知

让 WorkBuddy 执行一个耗时任务（比如爬数据、分析文件），完成后发邮件通知，不用一直盯着。

优缺点

优点：

-
解决了定时任务/自动化结果推送的痛点

-
邮件支持大附件（126邮箱支持 50MB）

-
格式完整，PDF、Excel、图片都能发

-
有记录，邮箱里能随时查历史

缺点：

-
需要多一步看邮件

-
实时性不如微信（延迟几秒到几分钟）

-
需要配置邮箱授权码

最后

这里是 WorkBuddy 100种用法第7篇。

我正在持续更新这个系列，记录用 WorkBuddy 的各种骚操作。

想围观更多玩法？点个关注不迷路。

每日更新，带你解锁 WorkBuddy 的各种隐藏技能。

一起用 WorkBuddy，让效率飞起来。

#WorkBuddy #定时任务 #邮件推送 #任务通知 #自动化 #微信ClawBot #邮件Skill #100种用法 #效率工具 #任务结果推送

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRNdohRQ4ic0diaYMpqyiaFgqZRJK3y37WvCl3bwXvARGFHKOEKNh1PSxQW1BwR2Nq1ricZoRpbT6Ljv3dIaCK5AsXLmf7LGXYU7IAI/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMdU6FjU1DEy2LFNytC3GjVaVbJWFR8UpJGewHUuhmRkLqCYldkfjvmP7cjeLFLJUJchicdtQlaGXXgFhxricwicpiaySNId9GKlUc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPZo26fWobcwdZAZUeVoevLLqqKZiaohb0sPSI8iaCvF2xx7k0YGwS2on71Sbwzz24Vp2vRwoIbX2Kqf9g6s1hn0EUsHEjQFKtl4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM3Cb0hrUoVicTHLobfwF32jTHuBQIJzOWlUAwTdVqOCzQX7G2I9XIBWDQzSVd39mBBtShurNlzqMnnwrleUqrOFeAps2eFhcwU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNpgGU9gpzrDQHrgVd66jueAcFJD1Z2dEsqL3ef7fvGR5IV8PGicYiapcog7B1U1WW99GwlcMm60UTUmdyzSjOdA4AkkOO7hKAoo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMnoUUTSB8OQvky5oWq9aEPnUIEY713ZNEy3wLQaSEBd2HReQuicibYl3qOIQJpznOv2DulKz55rSw40qhicia1KrmDFHH5QOffPU8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMc6jKW9oLDr9ib29slhRPBV1zHzNXmibsK1zFxw7yNtI2231O1qze4iaBZicQnh7L6so7N2rXPlwefzXUtEdZNoYIo2IeHo3ee2jI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNRh8ux6xFicuyT9Mnicxx8xx2LnAEz4hCw3MF9q2exug8mx4haXjFeV6W1aPzicJInTdbicQLQK1IP72e2C322UbgI2ia9d7OXx1qs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO28bADxXN8BE5FFT7Kicl1Ll68xpEMGJ6ALN9HWTOV8G3w4RnAOEw8js0hEXzRXEVF9Orq6eibxiaCE87GaPHdh5dw2ICy3FR3Eg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROib4L8aEzXlibqjWCTvoc2qIWEWAmZrX3K9LhsH19gDRpsRBfKoJMQH7Vwnh9W7onRPOdSKIQ6iatUbjupFmJw5bx0GLu3KiazWoY/640?wx_fmt=png&from=appmsg
