# WorkBuddy 100种用法 #88 | 我说要清内存，它却给我画了一套系统设计稿

- 合集序号：88
- 公众号：我与ai的那些事
- 发布日期：2026-06-27
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329960&idx=1&sn=df8bd8bc2bcd3eece0bb3e6c1c14a57f&chksm=8830362fbf47bf398fc88bf98543bba3cca5802c235e7caf0dadcc27f14c9f743a0565cfb990#rd
- 正文字数：1376
- 正文图片：8

## 摘要

电脑存储不足想清理，结果阴差阳错让AI画了一套六页存储分析系统的设计稿。从仪表盘到智能清理、文件浏览、扫描历史全齐了。原来最好的AI产出，往往是个美丽的意外。

## 正文

事情是这样的。我的 Mac 又弹「存储空间不足」了。256G 的硬盘，系统数据占了 80G，各种项目文件、截图、视频素材堆在一起，根本不知道哪些能删、哪些不能动。

我想起 WorkBuddy 有卡神的存储分析的skill，就打开来试了一下，说了句【存储分析】结果——可能是我点错了？然后它开始干活了。

一个意外的设计稿

几秒钟后，屏幕上出现的东西不是清理建议，不是空间报告。而是一个设计稿。

一个存储分析仪表盘的设计稿。

我当时愣了一下。心里想「存储分析」，你给我画 UI 干嘛？

但仔细一看……这设计还挺像样的。Bento 风格的卡片布局，左侧是存储总览的环形图，右边是分类占比的进度条，底下还有一张大文件列表。配色是那种偏紫的蓝色（后来我知道它叫 Stripe Purple），字体清爽，排版干净。

我本来想关掉重来的。但犹豫了三秒——这看着不比大多数 SaaS 后台差啊。

于是我做了一个决定：不关了，让它把整个系统都画出来。

从一页到六页

我说：「你帮我把这个设计做完啊，这只是一个页面。」

然后它开始干活了。不是随便糊弄几张图，而是结结实实给我搭了一套六页的完整系统：

第二页：存储管理

卷概览卡 + 磁盘健康 SMART 表。每个卷的容量、已用空间、健康状态一目了然。磁盘温度、通电时间、坏道数这些硬核参数都列出来了——IT 运维看到会感动的那种。

第三页：文件浏览

左侧文件夹树 + 右侧文件列表，双栏布局。可以按目录一层层往下钻，每个文件的大小、类型、修改时间都清清楚楚。比 Finder 好用。

第四页：智能清理

这是最实用的页面。自动识别出可以清理的项目：临时文件、缓存、重复文件、大文件、下载文件夹。每类旁边标了可释放的空间量，勾选后右侧实时显示预览。一键清理——当然它不会真的清理，但设计上是这么走的。

第五页：扫描历史

存储趋势折线图，可以看到过去一段时间空间是怎么被吃掉的。下面是每次扫描的记录表，时间、释放量、操作类型都有。

第六页：设置

扫描计划、通知偏好、清理策略。那一排 toggle 开关做得有模有样，细节到位。

这让我重新思考了一个问题

以前我觉得 AI 设计工具就是「你说什么它画什么」。给一句 prompt，出来一张图。改一改，调一调。

但这次经历让我意识到，最好的 AI 产出往往是「阴差阳错」来的。

你本来想要 A，它给了你 B。B 看起来还不错，你顺势说「继续」，然后它就一发不可收拾。

这个存储分析系统，我自己是不可能从头设计出来的——没那个时间，也没那个 UI 水平。但如果我不用画，只需要「看」和「点头」呢？那门槛就完全不同了。

六个页面，从概念到设计稿，从你意识到「这玩意还能这样」到说「再来一页」，整个过程十来分钟。

所以 WorkBuddy 在这一轮里做了什么

不是「听指令画图」。而是：

-
1. 理解了一个模糊的需求（清内存）

-
2. 给出了一个超出预期的方向（设计存储分析系统而不是清理文件）

-
3. 保持了一致的设计语言（六页之间配色、字体、间距、圆角全部统一）

-
4. 考虑了真实的产品逻辑（不只是视觉好看，页面之间的导航、状态切换都合理）

说实话，这个设计稿拿给产品经理当原型评审，完全够用了。

这是WorkBuddy 100种用法第88篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI设计 #存储分析 #UI设计 #Bento设计 #效率工具 #产品原型 #智能清理 #AIGC #数字搭子

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROcibPFxKUWaYp5n3D5Dia19qeCgNys4HO4BoyovDkTm5wQbDlVSpksqUibPibOZjTSRbR1pRzS7LSpcIXAXb0eTaIny4haN1w80hY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPVP56kibaUX2Rmiafq0vIUIlI9yg1TZFicOwApte5C1komVtsM9CBQHYu50xVUUJHbWyCDvM1DBvSrNYgUwYP6DKibmeRUhVTyECk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNdRwJ4Kjv8VcFOHHXnu2yDZyoe4h5k9LSQLOOQlUwzg3Y5DnZkNRf2rVKzBZJFacnWdDDH7HAR9jSIerZSvjDm7rNLeXxQ5nY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROhQMqBalAibNEmvtx5fOTicWBkzgDgib3PrzWOGfIDaV0o6NEDwd63IPNVjRnnqYGIIdWTydgCKItIRZ6Eu20R7CQY7gRhlusgow/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROlRjQ4IbA3Z4AiaGicbrs8Odg9Zn7yE1XoxW30e25ZSmkbibGaic2WJA1KtQz3BSuicRRTSW6BA2Yx1ougg3NHrBGnlv1qlE0dib0kY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPWv1DAR8CqxNmyvn7bJXaF2DT01ELFrGOCE0cmDfW8TY4DpYlJ9NCtiaD2sIk0fJqznF3d9pjsdocZtDFFLpThWGpL38thN3y0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROCVjChiaWjVUI9ukNiasib49ljkyLboBWpJRa9BLicEJDbnGIqEtsTj04SoqtaE6AHF9XfbssHypsfLz7Ma6OOyoer9kcicyUfQ8xU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMzY6oovGRGGWQovXZ3v7gBO9T7yuQHwsgQTsQ753vPvmL6HlwxHp9OlL7ibhw6jiblP4QZYbib8QiccEfdzXBfRlrnmjrTwTjzaz4/640?wx_fmt=png&from=appmsg
