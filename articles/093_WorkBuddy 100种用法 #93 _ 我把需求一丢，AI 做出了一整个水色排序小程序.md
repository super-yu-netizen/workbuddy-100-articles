# WorkBuddy 100种用法 #93 | 我把需求一丢，AI 做出了一整个水色排序小程序

- 合集序号：93
- 公众号：我与ai的那些事
- 发布日期：2026-07-02
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330063&idx=1&sn=e58af676e30a9b976e93a23c9891a7ca&chksm=88303788bf47be9eb4e7bc08946a3e3255a08d3021ea1e12acb80bf1c00c5e38ce508feeccf6#rd
- 正文字数：2826
- 正文图片：16

## 摘要

把一份详细需求文档丢给 AI，它竟独立做出一款完整可玩的微信小程序——水色排序游戏，还陪我打磨了十几轮细节。

## 正文

最近想做个微信小程序练练手。倒不是要搞什么大项目，就是想验证一件事：现在 AI 能不能独立做出一个完整的小程序，而不是只会写个函数、解释段代码那种。

想来想去，选了个经典品类——水色排序（Water Sort）。就是那种把试管里不同颜色的水倒来倒去，最后每根试管只剩一种颜色的益智小游戏。规则简单，但要做到"手感好"，其实挺难的。

我给 WorkBuddy 扔了一份需求文档。

我扔了什么

不是一句话需求，是一份正儿八经的需求文档，整整 10 大块：

-
• 核心玩法：倒水、合并同色、判胜

-
• 新手引导：强制 4 步教程，但只在第一关出现

-
• 关卡系统：3 个难度，3200 关

-
• 升级系统：LV1–LV30，经验值规则、解锁内容

-
• 金币经济

-
• 商店：3 件商品，看广告换道具

-
• 7 天签到

-
• 成就系统

-
• 好友排行榜

-
• 本地 + 云端存档

说白了，就是一个能上线的完整小程序该有的东西，全列出来了。

我就想知道一件事：AI 能不能照着这份文档，把整个东西做出来？

它真的做出来了

不一会儿，WorkBuddy 给我交付了一整个项目。

不是代码片段，是完整的、能跑的微信原生小程序工程：

-
• app.json、app.js、app.wxss 全套配置

-
• pages/ 下面 7 个页面：首页、游戏页、个人中心、商店、签到、设置、排行榜

-
• utils/ 下面一堆逻辑文件：游戏引擎、关卡系统、用户系统、广告……

-
• 甚至连 README 和数据表都写好了

最让我意外的是——游戏引擎里自带一个 DFS 求解器。

它会自动检查每一关是不是"可解"的。也就是说，生成的 3200 关，不会出现卡死解不出来的情况。

这一点我自己写代码的时候都经常忘，它会主动加上。

但真正有价值的是"改"

如果故事到这儿就结束，那就是一篇"AI 真厉害"的吹水文。

真正有意思的，是接下来十几轮的"挑刺—修复"。

做出来的第一版，能跑，但不好看。然后就是一轮一轮地改。我把几个典型的来回说说。

第一轮：颜色怎么这么细？

第一版跑起来，试管里的颜色细得像几条线，几乎看不见。

我：为什么试管里的颜色很细，几乎看不到？

WorkBuddy 查了一圈，发现是 CSS 高度塌陷——百分比高度需要一个明确的父级高度，而 .liquid 容器少了 top:0，导致算不出来高度。

改完，颜色正常了。

第二轮：倒水方向是反的

再跑，倒水动画有了，但是——杯子是"从底部"倒水的，看起来非常怪。

我：倒水的方向是错误的，不是应该从杯子口倒吗？怎么是底？

WorkBuddy 把旋转中心从"顶部"挪到了"中心"，又根据目标试管的左右位置判断倾斜方向。改完，水从杯口倒出来了。

第三轮：杯子里有条细线

方向对了，但倒水过程中，倒水的杯子里出现了一条小细线，很碍眼。

我：为什么倒水的过程中，杯子里有条小细线？

WorkBuddy 发现是水流元素放在了倾斜的杯子内部，跟着转就扭出来了。它把水流改成了一个独立的浮层，单独绘制，不跟着杯子转。细线消失了。

第四轮：同一个颜色怎么一段一段的？

颜色能显示了，但同一个颜色的液体被分成了好几段，中间有分隔线，看着像条形码。

我：一个杯子里，同一个颜色为什么要区分？看起来一段一段的，为什么不整合起来？

WorkBuddy 之前为了做出"水位上涨"的效果，给每一段都加了渐变和边框。问题是同色的时候，这些渐变和边框反而成了干扰。它把每段底部的边框去掉，改成整根试管统一加一层玻璃质感，同色自然就连成一片了。

第五轮：杯口和杯身是"贴"上去的

改完颜色，新问题来了：杯口和杯身之间有一道缝，看着像两个零件硬凑在一起。

我：液体和杯口之间处理还有问题，不是自然贴合。

WorkBuddy 把杯口重做成一个半透明的玻璃圈，往上盖住杯身顶部 15rpx，接缝就看不出来了。

连音效都是"造"出来的

中间还出了个事。

游戏需要倒水音效，但工程里没有这个文件，跑起来直接报错：

readFile:fail /assets/pour.mp3 not found

普通情况，我得去网上找素材、下载、处理格式。

我跟 WorkBuddy 说：你去想办法给我弄个 mp3，从网上搜索下载也行。

然后它干了件让我没想到的事——它没去找现成的音频，而是用代码合成了一段。

具体原理我就不展开了（大概是噪声经过滤波模拟水流声），反正最后它用 Python 跑了段脚本，直接生成了一个 pour.mp3 放进工程里。

倒水的时候，那个"哗啦哗啦"的声音就出来了。

说实话，这个细节让我挺感慨的——它不只是"知道"要去弄个音效，它是真的会动手造一个。

我做的是什么，它做的是什么

回过头看这十几轮，我做个统计：

谁做的

做了什么

我

写需求文档、发现问题、说"这里不对、那里不对"

WorkBuddy

写代码、查 bug、改样式、合成音效、反复调试

我做的，本质是"判断"——这个对不对、好不好看、手感对不对。

它做的，是"执行"——把我的判断变成具体的代码改动。

有意思的是，有些问题我根本说不清是"什么原因"，只知道"看着不对"。但 WorkBuddy 能从"看着不对"反推到具体的 CSS 属性、具体的渲染机制，然后修掉。

这就是好的搭档该有的样子——你负责感受，它负责实现。

最后做出来什么样

十几轮下来，一个完整的微信小程序成型了：

-
• 7 个页面，逻辑全通

-
• 3200 关，每关都能解

-
• 倒水动画顺滑，水从杯口倒出，同色连成一片

-
• 杯口圆润，颜色和玻璃质感自然贴合

-
• 倒水有"哗啦"声，不是难听的噪音

-
• 新手教程只在第一关出现

-
• 商店、签到、成就、排行榜一应俱全

从一份需求文档，到一个能玩的小程序。

我的几点感受

① 详细的需求，比什么都重要

如果我当初只说"做个水色排序游戏"，WorkBuddy 大概率做出来的是个简化版。正是那份 10 大块的需求文档，让它知道我要的是"完整"而不是"大概"。

需求越细，结果越接近你想要的。这点我在之前的文章里也说过，这次又验证了一遍。

② 反馈要具体

"颜色太细""方向反了""有条细线"——这些反馈都很具体。如果你只说"不好看"，AI 也很难改。

尽量描述你看到的、感受到的，而不是一个笼统的评价。

③ AI 能扛脏活

合成音效这种事，听起来跟"做游戏"没关系，但它就是会去做。查找报错原因、调 CSS、反复试——这些琐碎的、容易烦的脏活，它一点不嫌弃。

④ 迭代才是关键

第一版从来不是最终版。真正拉开差距的，是你愿不愿意花那十几轮去挑刺、去改。

AI 做出 90% 的骨架，剩下 10% 的手感，在你和它的来回里。

回到开头的问题

AI 能不能独立做出一个完整的微信小程序？

我的答案是：能做出 90%，剩下 10% 是你和它的来回。

而那 10%，恰恰是产品的手感——颜色够不够润、倒水够不够顺、声音够不够舒服。

这 10%，不是 AI 单方面能给你的。是你一次次说"不对，再改改"，它一次次调整，磨出来的。

工具越强，你的品味和耐心越值钱。

这是WorkBuddy 100种用法第93篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #微信小程序 #水色排序 #AI做游戏 #AI开发 #效率工具 #AI实战 #小程序开发

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP73xE8vTFjAH6NBnPlyQV7nKUExtvK1JdvNOF7e2hXcah35fW4l9Cv9cYzTticSYyia7dkYxeWonBuI9h30h1ABiaQclxtE7iayHg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROYKfvf5ghnc2k4t5RaZNma1E1v4xxAcg3jp1K2Kn9SaEGicgUiaJIg2WR9kJwt73FeI9eJ7ErwlKxrSqLFsOI4rasENevqsxTEk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPoEqweCTR077XZbqHPl4EhAWo84XtRJzR7ibWGpRrgUw47JzicurkZtYM6iaJ0bvGnPDCyhgbTzgibnicBY2fFezGjGhoKt8ib0n2PA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNVf39fmfuCW4L3yHcqkZp6tMr7GMD9zPMJg7sCKCZRpFNiaSOUXXLfN1unT7o2mzBSEBzC0jLT4KoBNIwWTnEfD0lk0Gumt0P4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMjicpFic3wQS4kvMic9MUejAw2RJhuaDqKZFMfyp7TSZl8Oicibge5pCetG9fk4Cz22jdZmg4AXZy3o9NmbiasuLK5NAkjiafKPJymVg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROp9kpEv0Wo5JRYTFPVvic81OFnNqvs25lKI58QsoYgiatB8EZYGcfdcsYMt0icf1hRHMXsK84ng75EwHcB5OchNGQyU1fC5wBlXg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMHZxlJVIMz9dWMltRhWG3ely1WS8zhk5HrOcZ24agSOurglPdeadxIrM5LoO4d01fpLXyR8gYibKT3MzKfRHCVMJXIVVa0DMM0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMZ6icIFBj5cmH8kv26wOxJ7oVKA3ficJmtkFibPTsb81I0W3RIPlTrhbqu1R5D2ibRbjCvJhdtqq30qeoictk8goNRzV7wMicKibah84/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMIte1jVL4tpIZ7nW1DEEGpw0l2LSDJXldCjfiaSs46oichIqviawttjfHkwqtxlN5RthBRBW6bLJNfvUkLzcWhHc7IFSRnXZ3rVk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPJ86E2afz9zxbibs07uslLN8x1K70OZXhIaO2wwkdPrT2ibxOp5DgFyQOYIyVwdLgZiayW8ib6LibR1liaqXN9gg42BCJZkobSwlzmk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPrn7XV7vKP8yuLQuuEtSUrJMXnq060xiccxw70e9t0136w8TWyTLLkaSfQVHRHqRUyJwUmH9GGdiaWn3j5MiaTAJMrSb4eeBAsA4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNQfPFYUdG1NIiaVG0W0KG3ELT48ESjurhyIOeF5mADRI2ZKnZuvh3erYg6nP8a9ibQWmjMdbiagw7RTC4VYQ7jpBSYibGcuqF81KA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP52kERT5YbdV5ORcL3XgRG6Vrnaea4zo1gibkB13VMkjtXxwtyfQa4nyx8wjrb3escYpvQm2LYmQoZsXjVJqONFvpDCOnvlgbM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM0cpt9CZvKyiaVMK5qichfxXovRJkPpeBLBt2tAWPZJ5QrofPBiawaoScicc5zVqpQrXiaA2ogqzN4RtXfNYWltIzpksPeBpjgR3Po/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPzjG6pJMKcB4icqyYWzwicFgyMibibhJ5ibNMbEvk6wNicuD6RMamSFCf28NL2N7UzV6JRtSbd8u7F2dQe9JwVhuRPbHXiatLMwJB1uQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNJ6a7CuScRYcVSB6rIMo6MSZRToWChHMtibTtCwMBULPHdQx8AiceKH6kcficG3gsrrveS9tkLUpVeozq5OoO2tBWauKMUEdfXQ0/640?wx_fmt=png&from=appmsg
