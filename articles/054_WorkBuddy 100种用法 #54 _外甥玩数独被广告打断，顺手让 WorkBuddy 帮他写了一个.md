# WorkBuddy 100种用法 #54 |外甥玩数独被广告打断，顺手让 WorkBuddy 帮他写了一个

- 合集序号：54
- 公众号：我与ai的那些事
- 发布日期：2026-05-24
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329123&idx=1&sn=3acd39b36d97de1eb6202ffcb34a4e5f&chksm=88303364bf47ba72483e3ca572117449e4d04374ed600a172aed6379a678db943e2cc509a87e#rd
- 正文字数：1874
- 正文图片：5

## 摘要

周末去看小外甥，发现他玩的iPad数独总弹广告，顺手打开WorkBuddy，10分钟写出一款无广告卡通儿童数独游戏，三端自适应直接在浏览器跑。

## 正文

周末去看小外甥，一进门他就拉着我看他 iPad 上玩的游戏。

这孩子今年7岁，最近迷上了数独——不知道从哪儿学来的，就是那种填数字的小方格游戏。我每次过去他都要拉我一起玩，大概是觉得我作为一个"搞电脑的"，应该很擅长这种事。

事实证明，他比我厉害多了。

他打开一款数独 App，玩得挺专注。我在旁边坐着，以为能安静待会儿。

然后广告来了。

就是这一下

全屏广告，还是那种要等15秒才能关的那种，中间偶尔还有个"跳过"按钮，但有时候点了没反应。

小孩最烦这个。他皱着眉头把iPad往桌上一放，说："舅舅，这个游戏有好多广告。"

我说："你等一下。"

然后打开了 WorkBuddy。

高级开发工程师，一把梭

在 WorkBuddy 的专家中心里，有一个叫「高级开发工程师」的专家。它跟普通对话不一样——它是一个专门做前端开发的全栈工程师，擅长 HTML+CSS+JS 一把梭，从设计到代码一条龙。

我先在专家中心点开它，然后在输入框里把整个需求一股脑打了进去——

我输入的需求大概是这样的：

帮我开发一款专为7岁儿童设计、浏览器直接运行的趣味数独闯关小游戏，需完美适配PC端、手机端、iPad端三端自适应，画面精美卡通、带背景音乐、完整激励奖励、等级关卡、新手引导，无广告……

我把具体的功能需求列得很细——分等级（4/6/9宫格）、分关卡（共35关）、音效类型、激励话术风格、错误提示方式、皮肤解锁、关卡进度保存……

需求越细，结果越接近你想要的。

回车之后，高级开发工程师就开始干活了。它会自己建任务清单、一步步分析需求、写代码。

中间我去倒了杯茶，回来的时候，一个完整的 sudoku-kids.html 文件已经躺在桌面上了。

WorkBuddy 做了什么

说实话，我自己如果要写这个，得花几个小时。

响应式布局、棋盘算法、关卡解锁、本地进度存储、Web Audio 生成音效……每一块单独拿出来都不简单，合在一起更麻烦。

而 WorkBuddy 一口气把这些全做了：

游戏规则层

-
• 4宫格（入门，10关）→ 6宫格（进阶，15关）→ 9宫格（高阶，10关），共35关

-
• 关卡解锁机制，通关才能进下一关，不能跳

-
• 填错有温和提示，不是那种"答错了！重来！"的打击感，是"再试试哦～"

激励系统

-
• 每关结束弹可爱动画，根据用时、错误次数发1-3颗星

-
• 累积星星可以解锁棋盘皮肤（森林、海洋、夕阳）

-
• 通关鼓励语随机出现，"太棒啦～"、"你真厉害！"、"继续加油，小天才！"

体验细节

-
• 背景音乐：Web Audio API 生成，轻快儿童风，右上角可一键开关

-
• 音效：点击格子、填对数字、填错、通关、用提示，每种操作都有不同音效

-
• 每关3次免费提示机会，只亮出格子的正确答案，不是直接给你全填完

-
• 新手引导：第一次进游戏弹出图文教程，配迷你演示棋盘讲规则

三端自适应

-
• PC：鼠标点击 + 键盘数字键 + 方向键移动格子

-
• 手机 / iPad：触屏操作，棋盘和按钮自动缩放，不拥挤

进度保存

-
• localStorage 本地存档，刷新浏览器不会丢进度

-
• 解锁的关卡、获得的星星、开启的皮肤全都记着

他玩了多久

我把链接在 iPad 上打开，递给他："你试试这个，没有广告。"

他玩了两个小时。

中间跑来问过我一次："舅舅，这个是你做的吗？"

我说："嗯，用 WorkBuddy 做的。"

他点点头，又跑回去玩了。

我觉得这是最好的验收标准——小孩不说话，专心玩，就是合格。

游戏已上线，可以直接玩

我把这个游戏部署到了服务器，浏览器打开就能玩，不用下载任何 App：

🎮 在线地址：panda.yaniw.com/sudoku-kids.html

PC、手机、iPad 三端都可以玩。有孩子的可以试试，或者自己玩也行，毕竟数独这东西，大人也容易上瘾。

高级开发工程师到底有多能打

这次让我印象很深的是——我几乎没有做任何二次调整。

一个完整的 HTML 文件，35 关，带音乐、带音效、带皮肤商店、带新手引导、带进度保存，一次性生成完成。没有报错，没有漏功能，打开就能跑。

这就是「高级开发工程师」这个专家的核心价值：它不是帮你写代码片段，它是帮你直接从需求到交付。

这种事不是第一次了。

上次我用 WorkBuddy 的探索模块帮朋友分析港股资金流向，三个 AI 分析师自动开了个圆桌；这次是周末给外甥临时造了个游戏。

同一个工具，不同的场景，不同的用法。

这就是为什么我要写这个"100种用法"系列——不是为了炫技，是为了让你看到 AI 工具在真实生活里能帮你干什么，而不只是在演示台上看起来很厉害。

这是WorkBuddy 100 种用法第54篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMYxywJtF20H2r6wPHBICEI7Cia52gyWQoCaMpBJAIbH794ERW6XyUjP1Z0eDuT2UGC17LbQmKjrHYTqu0f9ad3LjgwtzANNsm8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMRpbKAfYznBWVN63eFKOdAlQI1nJ45gpSVokURFCwvaALEvgUDW6Nw1pA4WNpRkBMFgpRSBBqtPkpUC6W0fbyXPz0Ekf5KG74/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM06JnTIwAdclxVBiaHsWTpiaEbQ43PgqfJgqzCB4LLdWn3xM3zUQaMfuUZbApicCrd3NP5ZTchy8u5lcyoA9iaa7qyic80lmynNUls/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMh8nHpGFwY8D9UyQm8RF7cEVV0xyN962coISKkkfiaAhria8cgJoeX8jt7N5usjjK1NORIEbtzHXSkUln6lVOo9TWP12fRKhl9Q/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMib1xuTJzC4P10UFL4QIKxPg0RIxzdibVwuCoXDBL4Z2PVUlYdLOcSaAiaJSwwHPuynnClYKibNfO7HFpcwZ87W52jGeCb75VKXlI/640?wx_fmt=png&from=appmsg
