# WorkBuddy 100种用法 #6 | 零代码！30分钟用AI做个MBTI测试网站，直接上线

- 合集序号：6
- 公众号：我与ai的那些事
- 发布日期：2026-04-05
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328064&idx=1&sn=a69a56f2eaf0dcdeb377fbd6e0f7dd72&chksm=88303f47bf47b65157d92ff3dd7a95964383ff1006e7dabbe7e9e7f2afc0daa57cdcce4b0b2d#rd
- 正文字数：2558
- 正文图片：7

## 摘要

实操展示用 WorkBuddy 从零搭建并迭代 MBTI 测试网站，30 分钟完成从需求到上线，零代码轻松搞定产品落地。

## 正文

昨天闲着没事，在 WorkBuddy 技能列表里看到有个叫「MBTI 人格诊断」的东西。

MBTI 我知道，就是那个测你是 INFP 还是 ENTJ 的人格测试。但这个 Skill 具体是干嘛的、怎么实现的，我完全不懂。

于是我对 WorkBuddy 说：你去研究下这个 Skill 是怎么回事。

这一问，就开启了一个从好奇到上线的完整过程。

第一步：让 AI 先搞清楚原理

我给 WorkBuddy 发的第一条消息是：

"MBTI 人格诊断这个 skill，你去学习下，这个是怎么实现的。"

过了几分钟，它回复我了，大概意思是：

这个测试基于一个叫 OEJTS 的开源量表，一共 32 道题，测 4 个维度，每道题选 1 到 5 分，最后算总分得出你的人格类型。所有计算在本地就能完成，不需要服务器，也不花钱。

我看懂了——就是个答题算分的工具，在线上就能跑。

然后我又问了一句："能使用这个 API 做一个线上的测试网站吗？里面的 API 调用有什么要求？要钱吗？"

WorkBuddy 回答说：这个 API 是免费开源的，没有调用限制，也不需要付费，直接用就行。

我说：那就帮我做一个。

它就开始了。

第二步：10 分钟后，一个完整网站出来了

大概过了 10 分钟，WorkBuddy 告诉我网站做好了。

我打开一看——还真不是个简陋的半成品。

首页长这样：

一个深色背景的页面，大标题写着"MBTI 人格测试"，下面列了三个特点："3 分钟完成""科学评估""详细分析"，底部一个大大的按钮"开始测试"。说实话，比我预想的好看。

答题页长这样：

每道题是一个滑块，左右两边各有一段描述，你滑动选择更符合自己的那个。页面顶部有进度条，能看到做到第几题了。一共 32 道题，我试了一下，几分钟就做完了。

结果页长这样：

做完之后会显示你的四字母人格类型（比如 INTP「逻辑学家」），每个维度的百分比分析，还有一段描述你性格的文字。最下面还有一段可以复制的分享文案。

我拿手机打开看了看——手机端也能正常显示，不用单独适配。

到这里为止，我只说了 3 句话，就得到了一个能用的完整网站。

第三步：提需求，让它改

网站能用，但给别人用的时候还是发现了不少问题。

接下来的过程，基本上就是：我发现问题 → 截图发给 WorkBuddy → 它改好。

问题 1：用户不知道怎么答题

我把网站发给朋友看，朋友说"这个滑块是干嘛的？"

我就截了个图给 WorkBuddy："用户看不懂怎么操作，加个文字提醒。"

它加上了：

-
首页提示："每道题选择两个描述中更符合你的一个"

-
答题页提示："左右滑动圆点，选择更符合你的描述"

问题 2：手机上结果页的排版挤在一起

我在手机上打开发现，维度分析那一块显示乱了。

WorkBuddy 改了一下布局，把横向排列改成了一张张卡片竖着堆叠，手机上立刻就正常了。

问题 3：想保存结果图片发朋友圈

我跟 WorkBuddy 说："用户做完测试，想保存一张图片发朋友圈，你帮我加上这个功能。"

这个需求折腾了好几轮：

第一版做出来，截图中把底部的"重新测试"按钮也截进去了——不行。

改好了，又发现人格类型的标题在截图里颜色显示不对——再改。

改好了，发现底部的公众号二维码在截图里不见了——又不行。

前前后后改了四五轮，它自己试了好几种方案，最后终于搞定了。测试结果能完整地保存为一张图片，标题清晰、二维码可见、按钮不乱入。

问题 4：微信里保存不了图片

网站上线后我特意在微信里打开试了一下——结果"保存图片"点了没反应。

我问 WorkBuddy 怎么回事，它说微信内置浏览器不支持直接下载文件。

然后它自己想了个办法：检测到用户是在微信里打开的，就弹出一个全屏的图片展示页面，提示"长按图片即可保存到相册"。

这个细节说实话我根本想不到，但它自动处理了。

第四步：部署上线

到这里，网站本身已经没什么问题了。

我给 WorkBuddy 发了消息："把这个网站部署上线。"

结果它问我：部署到哪里？

我当时愣了一下——它之前帮我部署过一个小游戏，我记得是部署到 panda.yaniw.com 这个网站上的，就直接跟它说：跟上次一样，部署到之前的那个地方。

然后我就看着它自己去翻了之前的记录文件，找到了仓库地址和部署方式，接着一顿操作——推代码、配置、上线，全自己搞定了。

过了一会儿它告诉我"已经上线了"，我打开链接一看，真的能用了。

从我说"部署"到网站能访问，我只多说了一句提醒，剩下的全是它自己查资料、自己动手的。

上线之后我第一个就去测了一遍，这是我的测试结果：

整个过程，从第一句话到网站上线，大概不到 30 分钟。

后来我又让它做了几件事

网站上线之后，我又提了几个小需求，也都一一实现了：

-
加了网站图标：打开页面时浏览器标签上会显示一个 🧠 的小图标

-
加了访问统计：能看到每天有多少人打开这个测试

-
加了公众号二维码：用户保存的图片底部，会自动带上公众号的二维码和引导关注文案

每张被分享出去的测试结果图，都变成了一个引流入口。

回顾整个过程

我做了什么

花了多少时间

让它研究 MBTI 原理

说 1 句话

让它做网站

说 1 句话

发现问题，提修改意见

说 5 次反馈

让它部署上线

说 1 句话

总计

不到 30 分钟

我不用写代码，也不用懂部署。

我只需要说"我要什么"，WorkBuddy 负责"怎么实现"。

中间遇到了二维码不显示、微信里保存不了图片这些我听都没听过的问题，它自己查资料、自己试方案、自己绕弯路，最后给我一个能用的结果。

这才是我觉得 AI 工具真正有价值的地方：不是让你变成技术人员，而是让你不用成为技术人员，也能把想法变成现实。

最后

这是「WorkBuddy的100种用法」系列的第 6 篇。

这系列会一直更新下去，记录 WorkBuddy 在公众号运营、内容创作、网站开发、效率提升等各种场景下的真实用法。

想测测自己是什么人格类型、生成专属画像？关注「我与ai的那些事」，回复「MBTI」获取测试链接，3 分钟出结果。

如果你也在用 WorkBuddy，或者对 AI 工具提升效率感兴趣，关注「我与ai的那些事」，后续内容不会错过。

#AI工具 #WorkBuddy #MBTI人格测试 #在线网站开发 #前端开发 #零基础建站 #微信兼容 #部署上线 #效率提升 #自动化

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

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROPwiaQLKQCqOgBdasPW0JgrEu9ltlgrJz9Tk9FJB45tDq6147StvvdOYq1rc2n2M4CibQxibg0E5Qb6Dt2HhtvCU2brfyTR52fAQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbROZhyOrd6p0yDDowt49Hk2TibaQ5ibQicUpWkjQPxnqibwNwTfcvumW3aHbKXMDiavEbMFxR8h2JbRZUWOIa7qHsfPblEWC8ia4o4iad4/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRPoyQibKicmWibXO0mw2PHtw1s0aLpjpBriaRB7WMhljfVrOibibO92B015je8ibPDXasW3bD8C29sQAtvqXg34ibP7HUhkttH5uQ15y5I/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRNKnNVBO1bia1eicKqPI1J7ANXvXHDoCXqxkTPuLEXfkOyv8ia71ZpSdRKEx3c2ich423yZN26uD3VHLsiaLs9bBib0QLSVIzwvoTkTo/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRNiaLfEtBDmicadfZ0UQ9hwb2D9miaX6mudItyYpC99tHchia61LsxvicDodJF7suxnicc1ZQ1wicKFZIJHSJocXn6mKuKfrp0gXURyjg/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRNsyejRXCRNLOQSeud9cB1rJlicr0zaBynPCBP6dbVctdYkPeUuA7CL1qardZibEeNjHB1TVorNCNV8xfc4G1JH0sAkf2VMec7Bg/640?wx_fmt=jpeg&from=appmsg
- http://mmbiz.qpic.cn/sz_mmbiz_png/JvRAOtGGLJtAxia0Gjbls2as6IvpOJj4ovOaYKdNic2PcAj0u875xVN8h1Kk5AlQ23PgDTAjqMI7xPXDPPd0D0yQ/0?wx_fmt=png
