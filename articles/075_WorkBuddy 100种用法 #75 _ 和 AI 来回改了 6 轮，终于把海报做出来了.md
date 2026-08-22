# WorkBuddy 100种用法 #75 | 和 AI 来回改了 6 轮，终于把海报做出来了

- 合集序号：75
- 公众号：我与ai的那些事
- 发布日期：2026-06-14
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329663&idx=1&sn=4ea6d59769ce61c64ceb9a82a119aac3&chksm=88303578bf47bc6ea0d43c4dbdd309c09d7008eb7a58d10363122e71c92e70223f4e07efac06#rd
- 正文字数：2931
- 正文图片：14

## 摘要

用 WorkBuddy 创意设计做科技峰会海报，AI 第一版翻车，自己批评自己后重做，来回 6 轮才出成品。记录完整过程和踩过的坑。

## 正文

今天打开 WorkBuddy，看到有新版本更新——

v5.1.0，更新说明里有个「创意设计」，点进去看看，一排场景模板——网页、App、幻灯片、品牌视觉……还有一个「视觉海报」。

正好点了下【科技峰会海报】模板，直接就有一句话进去：

「设计一张科技峰会的活动海报，需要突出三位演讲嘉宾头像、活动时间地点和报名二维码」

第一版翻车（并不意外）

WorkBuddy 很快出了第一版。它自动选了一套赛博朋克暗色风格，Color 选了量子计算界面配色，字体 Space Grotesk + DM Sans。布局是左右分栏——左侧放标题和时间地点，右侧放三位嘉宾卡片。

打开一看，问题不少：

-
• 标题「全球科技峰会」断成两行了。 120px 字号在左栏 768px 宽度里放不下。

-
• 报名二维码只是个白色方块占位符。 根本没有真实二维码。

-
• 三位嘉宾没对齐。 陈思源的职位「AI 研究院首席科学家」字数多，文字换行了，卡片被撑得比旁边的都高。

-
• 第一个嘉宾的机构名「智源人工智能研究院」在卡片底部溢出了。

于是开始第一轮改。

第一轮修复：补二维码 + 对齐嘉宾

我跟 WorkBuddy 说：「报名二维码怎么没有的，还有三个人，怎么没对齐？」

它做了三件事：

1. 生成真二维码。 它直接调 Python，pip install qrcode[pil] 装好库，然后写了段代码生成二维码——青色 #00FFFF 模块 + 深色 #101823 底色，300×300 分辨率。生成后上传到画布替换了那个白色占位方块。

2. 对齐三张嘉宾卡。 把三张卡片的 counterAxisAlignItems 设为 CENTER，所有头像/姓名/职位水平对齐。

3. 给头像生成真实照片。 不是单纯的渐变色圆，而是调 AI 生成了三位嘉宾的专业肖像。

同时顺手加了装饰——左栏和右栏之间的渐变霓虹分隔线、标题的青色辉光效果。

二维码有了，嘉宾对齐了，看着比刚才好不少。但……标题还是断行，陈思源的机构名还是溢出。

第二轮修复：标题字号 + 卡片高度

我跟 WorkBuddy 说：「标题为什么换了一行，第一个人的介绍超出边框了？」

它把标题字号从 120px 降到 92px，行高 132→104，这下「全球科技峰会」稳稳一行了。三张卡片高度从 400 涨到 420px，机构名字号从 28 缩小到 26px，溢出问题也解决了。

改到这儿，第一版的所有功能性 bug 都修完了。标题一行，内容不溢出，三个嘉宾对齐，二维码是真的。

但看着这就是……不对味。

我让 AI 自己看看效果，它说了实话

我把截图丢给 WorkBuddy，直接问：「你自己看这个设计好看吗？」

它的回答让我服气——没有辩解，直接认了，而且说得挺到位：

不好看。问题不在细节对齐，而是整体设计方向就有根本性问题。

-
1. 这张海报看起来像个暗色模式后台管理面板，不像活动海报。

-
2. 背景完全空白——零氛围感。

-
3. 嘉宾卡片 = 默认 UI 组件。。

-
4. 标题存在感不够强。

-
5. 信息层级扁平。

然后它主动提了重新设计的方案——全画幅沉浸式布局、标题做大做满、背景加科技纹理、嘉宾横向排列融入构图、底部收拢信息。

我说：「重新做一版看看。」

重制版：从零开始，思路完全不同

它没有在旧文件上打补丁，而是直接建了一个新文件。整个过程我观察到的关键是它先选了不同的设计基础：

-
• 布局不走左右分栏，走居中沉浸式

-
• Color 选 Gaming 不是 Quantum Computing Interface（偏游戏化的配色，层次更丰富）

-
• 标题直接提到 160px，是原来的将近两倍

生成完大概长这样：

这一版的核心变化：

项目

第一版

重制版

布局

左右分栏 Dashboard

居中沉浸式海报

背景

两块纯色平涂

AI 生成赛博朋克粒子光效 + 电路纹理

标题

92px，两行风险

160px，五层霓虹青色辉光

嘉宾

方形卡片堆叠

圆形头像 + 姓名直排，各自发光描边

信息

散落在左栏底部

底部半透明暗带统一收拢：时间 · 地点 · 二维码

背景是 WorkBuddy 调 AI 生成的——暗蓝紫渐变 + 粒子光效 + 电路板纹理，不需要我自己找素材。标题加了五层不同半径的青色辉光（从 80px 到 3px），在深色背景上有很强的霓虹效果。

还有一个配色问题

但重制版也不完美。第一位陈思源的机构名「智源研究院」和第三位林若曦的「字节跳动」用的还是青色 #00FFFF，跟背景的蓝色粒子纹理完全重叠在一起，根本看不清。

我跟 WorkBuddy 说：「第一位和第三位的公司所用的字体，和背景的颜色有重叠，看不清楚，字体配色优化下。」

它把两个机构名的颜色从青色 #00FFFF 改成暖金色 #FFD166。暖金色在冷色调（蓝/紫/青）背景上对比度最高，一眼就能看见，也不破坏科技感。

我觉得还可以了，它自己还在挑毛病

改完这轮，我看着觉得能用了。WorkBuddy 问我要不要再改，我说：「我不懂啊，我看着这样就可以了。」

它的反应很有意思——没有说「好的完成了」，而是自己又总结了一下这版还有什么可改进的：

做得好的：标题霓虹辉光、嘉宾圆形头像、底部信息栏收拢
还不够的：背景虽然有了渐变，但缺少真正的科技纹理层次、颜色层次略单调、留白偏大

我心想：行了，差不多得了。就说「你觉得可以就可以」，然后它帮我把最终的海报导出到了桌面——2x 高清 PNG，3840×2160，直接能用。

几点感受

-
1. 第一版几乎都是翻车的，这很正常。 不是 AI 不行，是文字描述和视觉结果之间有天然的信息损耗。你脑子里想的「科技峰会海报」和 AI 理解的「科技峰会海报」差着十万八千里。AI 需要你给反馈才能校准方向。

-
2. 让 AI 自己看截图、自己批评自己的设计 —— 这个操作太值了。 我把第一版的截图丢回去问「好看吗」，它列了 5 个结构性问题，每个都说到点上。这不是「态度好」，是它真的能看懂自己的设计有什么问题。

-
3. 改了 6 轮才出最终版： 第一轮修二维码和对齐，第二轮修字体和溢出，第三轮 AI 自己否掉第一版，第四轮从零重制，第五轮修配色，第六轮确认收工。真正的设计过程就是这样——不是一句话出成品，而是一轮轮的反馈迭代。

-
4. 配色在复杂背景上需要特别注意。 青色 #00FFFF 看起来很酷，放在蓝色粒子背景上就是灾难。暖金色之类的高对比度颜色才是复杂背景上文字的正确选择。

-
5. AI 生成海报背景是真实可用的。 不需要自己找图、不需要处理版权，WorkBuddy 直接调 AI 生成了赛博朋克粒子光效背景，跟整体风格完美融合。

-
6. 导出是成品。 2x 高清 PNG，3840×2160，不是设计稿截图，是直接能用的海报文件。投屏、打印、发朋友圈都没问题。

这个功能还在持续迭代，但已经能打出真实可用的海报了。如果你也有做活动海报、宣传物料的场景，不妨去 WorkBuddy 的「创意设计」里试试。记住：别指望一句话出成品，和它多聊几轮，效果会好很多。

这是WorkBuddy 100种用法第75篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI设计 #海报设计 #科技峰会 #创意设计 #AI工具 #设计迭代 #WorkBuddy100种用法

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

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPcYfTOrt4OFcnsRYKdH3Qaa3JLaCdjXyym5wGBEa7MU3WTAAA1hjeK6kIqD6tO32Ta9rib2mzuXy53CmmAvDfBmJ6SwDVicnzGs/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMSOPaOAOSNsTTtztL0FPOwLmG6SrvsxclLK6AgYnOJicB2QkAhkvFtu7ibYXuejWYMFF0FyljWoLT7wIhrI0wkVqrey0ZgRAasY/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNeINNwCSW6xianCic0VWuqwr5Yvdb1HHZF1natHWccNPBO6uQVdcezVH8Ovd2hj2dMWMk7kRGzosdT3tNaGA9WTqVxkwTM1gbp8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMsp8z3JX2XKPSRiaz0CfSLeSM9nn3ib9iaFQdCt63hYiasibrfellNmhQ8T6jX4TNd7uyzfJfmibiaiad2LJsiaF9lmZkLiaL2lc0Objd7c/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNBJ2ibW0P4bh9Kiclr27XCiciaAHHsKkH6u9Y1bBjOJ0NEvu7H7k6icy0DQ4GRJOSOQZLmaibzJo7WWItCQX9nZIoLbzeyOT6h7TriaM/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO0jkJNodyeXhQ51ibOxRm3icicF6YXWAUdE7E9Ug2167UIBJS29f7bsFFQr4rlmlOwsH7F6A7t0uIogAzWdVF8fEX6h9Isce9Yug/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNxbOGr9Lxv7sN8kKOqLEHkgLOu24HEkzD8b7UneafulIYHXBwYKgaCxVVB2xRygVfGrk1U2Kbic31fibUEuZRh2Ct1WmJ7V5cDA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNa34lB8kiao42M9INA7gAqwWQwBn0JTXdoMhDB3D1KybY1jRZdECxT6ibzOLwKciaGwBCNHiaNuSMcIDYJg4qyYVc1WK8gxvGhsrI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNCXDuS4NE9Ra5Lvt9aicHtwU1WjtPvL5OiaWzmtqLdlgmIkC1SHNic9Kibe8z09picGxBQ1HIp7F71SwgfbbOcekHnKibDUE9iben0icU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROUaKjsgIDYfSSWUib8SRKbuxxghGKFUVLiaPI7mCjcUShqnn6ic3DcLa9NlzIicNDGMJRvHaEDWaw0oRKUEz7rS9q0ibHdy0sSOrEg/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROAbCocswGdtbGxba9v47rSzKAgEEnTI97gXBvvLFwIeJFYdGbxr2XpicvASlibly7PFlToQcsD3RbXHYshT38EqibXUTiaIIVPpRM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRNoS08VLjk0hUTD8iaFQmmnKBP0j26yTuykUWzYVodl26KnXj8OVRl44gaxUUTZSNKDcEicfd7d3nz2cVXTUw23lNRmmfZSc7hHw/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNiaCp8cibbmItibjXh4KtTYygCmz2aiaxPYY2wqT5fhxjZHnnvNwzoHcQHzxkKibc6EiaE3y0CEcCQ0OYxMFuicGiaLrZnBLPqvoJdSjY/640?wx_fmt=png&from=appmsg
- http://mmbiz.qpic.cn/sz_mmbiz_png/JvRAOtGGLJtAxia0Gjbls2as6IvpOJj4ovOaYKdNic2PcAj0u875xVN8h1Kk5AlQ23PgDTAjqMI7xPXDPPd0D0yQ/0?wx_fmt=png
