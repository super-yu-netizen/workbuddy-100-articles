# WorkBuddy100种用法 #9｜每天忘签到？AI写脚本自动签到领积分

- 合集序号：9
- 公众号：我与ai的那些事
- 发布日期：2026-04-08
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328131&idx=1&sn=e183dc0c426867ac2cb7b9fc68174420&chksm=88303f04bf47b612461cd52a455bd6df684b7bb9630ec4b4b5c6b4dfd0e957ec63037c332996#rd
- 正文字数：1883
- 正文图片：6

## 摘要

受群友启发，利用 WorkBuddy 编写自动签到脚本，解决日常忘签问题，本文记录实操流程、踩坑过程与最终稳定实现方案。

## 正文

前两天在群里看到有小伙伴用 WorkBuddy 写了自动签到脚本，给了我很大启发。
正好 WorkBuddy 有日常签到领积分活动：每天签到100积分，连续签到7天直接领1000积分，我平时一忙就容易忘签，断签很可惜。
于是昨天我也折腾了一下，全程让 WorkBuddy 辅助写脚本、调试、踩坑。
今天把完整实操过程、遇到的问题和最终方案，一次性讲清楚。

一、方案1：图像识别（失败）

我直接跟WorkBuddy说：帮我写一个自动签到的Python脚本。

它很快给出第一版，用pyautogui图像识别，通过截图找按钮、自动点击位置。
听起来很智能，但一跑就翻车：分辨率一变就失效，窗口一动就点歪，稳定性太差，没法长期用。

二、方案2：系统API定位（失败）

我让WorkBuddy换思路：能不能精准定位界面元素？
它尝试用macOS辅助功能API获取位置，结果发现WorkBuddy界面是自定义控件，层级太深，根本读不到，这条路也走不通。

三、方案3：手动测坐标（最后方案）

WorkBuddy给了一个最“土”但最稳的方案：用户自己测坐标，脚本直接点固定位置。

步骤超简单：

-
1. 让WorkBuddy先写一个测检测鼠标坐标的脚本

-
2. 执行脚本，打开WorkBuddy，把鼠标移到按钮上

-
3. 获取坐标，发给他

-
4. WorkBuddy生成最终签到脚本

坐标定位脚本（复制就能用）

import subprocess
import time

print("移动鼠标，按 Ctrl+C 退出")
while True:
result = subprocess.run(
["osascript", "-e", "tell application \"System Events\" to get position of (process \"WorkBuddy\"'s first window)"],
capture_output=True,
text=True
)
print(result.stdout)
time.sleep(0.1)

运行后，把鼠标移到对应按钮，记录坐标：

HEADSHOT_X = 140 # 头像位置
HEADSHOT_Y = 1010 # 头像位置
CHECKIN_CARD_X = 180 # 签到卡片
CHECKIN_CARD_Y = 550 # 签到卡片

把坐标发给WorkBuddy，它直接生成最终稳定版脚本。只要窗口位置不变，永远不失效。

四、配置定时任务：每天8点自动执行

脚本写完，直接让WorkBuddy帮我配置定时任务：每天早上8点，自动运行签到脚本。

它一键帮我填好：

-
• 任务名称

-
• 执行时间

-
• 执行命令

-
• 工作目录

保存即生效。

五、结果推送：微信实时提醒

执行成功/失败，直接推送到微信。
推送使用上篇这个WorkBuddy 100 种用法 #8｜定时任务直接推微信！PushPlus 秒通知方案，消息秒到。

六、完整流程总结

-
1. 让AI写脚本 → 图像识别方案不稳定

-
2. 换系统API → 读不到界面元素

-
3. 改用手动测坐标 → 最稳、最简单

-
4. AI生成最终脚本

-
5. 配置定时任务

-
6. 开启微信推送

不求最优雅，但求最能用。

七、避坑小贴士（必看）

-
1. 坐标失效怎么办？
重新测一次即可，建议把WorkBuddy窗口固定位置。

-
2. 脚本跑不起来？
打开Mac辅助功能权限：系统设置 → 隐私与安全性 → 终端打勾。

-
3. 定时任务不执行？
电脑必须开机，不能休眠；脚本路径要正确。

-
4. 必须先登录！
脚本只负责点击，不负责登录。

八、写在最后

这篇最值钱的不是代码，而是解决问题的思路。
AI给的方案不一定一次成功，但它能快速帮你试错、迭代、找到最优解。

自动签到虽小，但代表一种效率思维：
能让机器做的，绝不自己动手。

💬 今日互动

你平时最想自动化的小任务是什么？
是签到、打卡、还是重复点击？
评论区告诉我，下期我用WorkBuddy帮你写脚本搞定！

这里是 WorkBuddy 100种用法第⑨篇。
我正在持续更新这个系列，记录用WorkBuddy的各种实操玩法。
想围观更多玩法？点个关注不迷路。
每日更新，带你解锁WorkBuddy的各种隐藏技能。
一起用WorkBuddy，让效率飞起来。

#WorkBuddy #自动签到 #AI脚本 #自动化办公 #Mac效率工具 #100种用法 #WorkBuddy自动签到 #AI写Python脚本 #每天自动领积分 #pyautogui自动化 #AI编程过程 #解决问题思路 #数字搭子 #省时技巧

预览时标签不可点

微信扫一扫
关注该公众号

知道了

微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序

赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROUAtmvaC49IEe0iaLGVKPyvqCYYw0ewZoicPzuVtCX8HkkqKfR8QB9iawAT5WUN0U0ZpTGtvKSicb85hDTZaiar8nKcYhIv6S7vf9k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMliaMIFBLUC1RTHXfo8s865qHuia2wXwiacSP7loiaHwaSOKCy0d4RIbesauEibZPqHmteialJ0htib07W7vwKSuhPhoSZYAzuO3E6U4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROuFXx77mZv8PDicF976IBsHrE1r2I4yht4Ek4qoImcic2OY34GpKVcIWd4P7goEE60libcXIrJGJOZ9MNXhTSRLjeKXt9iahcdYO0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNhoupdjX6d61u0fQ7wQfEFibDtiaDVBTvNXq2QvNsa1ouJhCghVtF7RbrGccn1gfGGWrrTWpRUh2jQVx5uMsK5ZzWbtuYNxwteM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbROXic2npNvOTYmVtib4lyrx6YSZvsAzrWy2NNdCOo8WLGLv92F8fDJQQGnG50UQsdIz1LeMlJbPeickATyeom1XxsGBjJ6YDtVlR4/640?wx_fmt=jpeg&from=appmsg
- http://mmbiz.qpic.cn/sz_mmbiz_png/JvRAOtGGLJtAxia0Gjbls2as6IvpOJj4ovOaYKdNic2PcAj0u875xVN8h1Kk5AlQ23PgDTAjqMI7xPXDPPd0D0yQ/0?wx_fmt=png
