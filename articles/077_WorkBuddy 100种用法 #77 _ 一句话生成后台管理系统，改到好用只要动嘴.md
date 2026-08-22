# WorkBuddy 100种用法 #77 | 一句话生成后台管理系统，改到好用只要动嘴

- 合集序号：77
- 公众号：我与ai的那些事
- 发布日期：2026-06-16
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329697&idx=1&sn=ded2d2c92aaa874391ae0738b8557a79&chksm=88303526bf47bc3016bbc13ab345f8cf95b7b5b5fd11a1a39ca58b41aed4cc9d1a3f4f8b3438#rd
- 正文字数：2649
- 正文图片：7

## 摘要

一句话生成后台管理系统，从登录到看板到增删改查全搞定。遇到 5 个坑，动动嘴就修好了。

## 正文

大家有没有这种经历，脑子里有个想法，想做个小工具——比如管理笔记的后台系统，有登录、有看板、有列表、能增删改查。但你不会写前端，或者懒得搭环境、装依赖、写样式。

以前碰到这种情况，要么找开源项目改半天，要么花几百块找外包。现在？我随便点了几下，WorkBuddy 直接生成了一个完整的后台管理系统。

下面就是还原整个过程——包括生成后遇到的那些坑、怎么改、怎么调到好用。

事情是这样的。我今天在 WorkBuddy 里点了下【代码开发】——

再点下「网站开发」

再点了下【后台管理系统】，就自动出来了下面的提示词

帮我开发一个后台管理系统，用于管理笔记内容。要求：包含登录页、数据看板、列表管理、表单编辑功能，支持响应式布局。

点发送。WorkBuddy 开始动工。

WorkBuddy 用了不到一分钟，生成了一个单文件 HTML，零外部依赖，数据存浏览器 localStorage，刷新不丢。打开就是登录页——

-
• 登录页：账号 admin，密码 admin123，表单校验加错误提示

-
• 数据看板：笔记总数、总字数、分类分布柱状图、最近更新列表

-
• 笔记列表：搜索、分类筛选、分页（每页 6 条）

-
• 表单编辑：模态弹窗，标题+分类+内容三要素，字数实时统计

-
• 响应式：桌面端侧边栏，平板和手机自动折叠成汉堡菜单

暗色主题，琥珀色强调，整体是那种克制的数据面板感。内置了 7 条种子数据，覆盖技术笔记、读书笔记、工作日志、个人随笔几个分类，打开就能看到效果。

到这里，一句话生成一个能用的管理系统，已经成了。但重点在后面。

二、发现第一个问题：编辑不显示原来的内容

我开始试用。在笔记列表里点了编辑按钮，弹窗出来了，但——标题和内容是空的，没有回填原来的数据。

这就很奇怪。正常逻辑应该是：点编辑 → 弹窗里显示原来的标题和内容 → 我修改 → 保存。但现在弹出来是空白的。

我把这个问题反馈给 WorkBuddy。

它检查了代码之后，马上找到了原因：种子数据的 id 是用 Date.now() 生成的数字类型，但 HTML 里的 onclick="editNote('...')" 传过来的是字符串。JavaScript 的 === 严格匹配不上，find 返回空，表单自然不回填。

修复也很简单：把 id 比较的地方统一加上 String() 转换。改了三处——openEditor、saveNote、deleteNote——刷新就好了。

这就是 AI 写代码的一个典型问题：它写出来的东西逻辑是对的，但类型处理上容易出小纰漏。 不过好在你只需要反馈"这是空的"，它会自己去排查和修。

三、第二个问题：笔记列表页太空了

列表页能用了，但感觉不对——看板页面有统计卡片、有图表，视觉上很充实；笔记列表页就一个光秃秃的表格，显得很空旷。

我又跟 WorkBuddy 说：能不能让列表页也像看板那样，顶部有个统计条？

它在列表页顶部加了一条 4 格概览统计——总笔记数、总字数、分类数、最近更新时间——和看板页顶部那排卡片风格一致。

四、第三个问题：点击标题的行为不对

接着试。我在列表里点了一条笔记的标题，弹出来的是编辑窗口——这不太对。正常逻辑应该是：点标题看详情，点编辑按钮才编辑。

反馈给 WorkBuddy 之后，它改了两件事：

-
1. 点击标题 → 打开只读详情弹窗，显示分类、字数、创建/更新时间、完整内容

-
2. 详情弹窗底部有个「编辑此笔记」按钮，点它才进编辑模式

点遮罩层或按 Escape 关闭。逻辑修得很干净。

五、最头疼的问题：布局不居中

改了上面三个问题之后，我发现一个更基础的视觉问题：整个内容区域是靠右的，不是居中显示的。

你没看错——侧边栏占了左边 240px，剩下的内容区域理论上应该在剩余空间里居中，但它贴在了左边。

我提了这个问题。WorkBuddy 改了第一次：加 max-width、margin auto。不行。

我说"还是不行"。它又改了第二次，说之前 max-width 太大了。不行。

我有点火了，说"你到底会不会布局，这是居中吗？你懂不懂前端啊"。这次它终于找到了真正的问题——

.main-content 只有 margin-left: 240px 没有显式的 width。 一个 block 元素默认 width: auto 填充父级，但子元素的 margin: 0 auto 因为没有明确的父级宽度锚点，居中计算会失效。

最终方案：

-
• .main-content 设置 width: calc(100% - 240px)

-
• .content-area 设置 max-width: 1100px; margin: 0 auto

问题解决。但也暴露了一个事实：AI 写 CSS 布局的时候，复杂嵌套关系下的居中逻辑容易翻车。 这时候你要做的不是放弃，是截图+描述问题，让它自己排查。

六、意外发现：笔记消失了

所有功能都调顺了，开始正经用。加了几条笔记，切出去再切回来——笔记没了，只剩 7 条种子数据。

我跟 WorkBuddy 说"我添加的笔记怎么没有在里面？"

它检查了一圈，发现了一个很隐蔽的问题：HTTP 服务器挂了。

因为我在开发过程中反复修改文件、重启预览，原本跑在 8898 端口的服务器不知道什么时候停了，页面自动切到了另一个端口 8899 上加载。但 localStorage 是按「域名+端口」隔离的——之前保存在 8898 的数据，在 8899 上读不到。

重启服务器，修好。顺便给 saveNotes 加了 try/catch 和失败提示，不再静默保存失败。

这个教训是：AI 工具开发的应用，底层还是靠浏览器机制跑的——端口、缓存、localStorage 隔离这些坑，AI 不会主动告诉你，但你遇到的时候它能帮你排查。

七、这次对话的收获

整个对话下来，我最大的感受是：WorkBuddy 真正的能力不是"一次性生成一个系统"，而是"生成之后，你能跟它对话来改"。

刚生成出来的东西只是「能用」，离「好用」还差几步。但这几步不是靠你打开 VS Code 一行行调的——而是你指哪儿，它改哪儿。

回顾一下整个过程中修复的问题：

问题

原因

怎么修的

编辑不回填

id 类型不匹配

统一 String() 转换

列表页太空

缺统计条

加 4 格概览统计

标题点进编辑

行为逻辑不对

改成先看详情

布局不居中

CSS 居中锚点缺失

设 explicit width

笔记消失

服务器端口切换

重启+错误处理

五个问题，全是对着聊天框反馈然后自动修好的，一行代码都没自己写。

这才是 WorkBuddy 做开发的正确定位：它不是取代你的，它是帮你省掉繁琐的。你有专业判断，它有执行能力。

这是WorkBuddy 100种用法第77篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMnwEBt1QTicKVPPbbP8ZPCrqP37Dfh8ibyH5aDrcdfyrKW7vOVeA0s6iaWsWb7wgsLMXS5B2H4pE9V5eJEtsL1KWUhlCiafKuDtjo/640?from=appmsg&wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNFGfgk26H7BSt7gvMOE9FqvJPVZSl05WGxFNDbA74zSvvtp3x0pTJR2GRpZyxOwT045iczFPMIYyia2fGouDGHbxbWEIfWeSmRU/640?from=appmsg&wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMPSaq9CaIJbUuhVZRGn9U3EB64QYfCThAJBIzDicBWRrGgOPFSQrrwXjPxWYZibiaTLU8gmAvq9HljtMNgu54A7M5OiazdX9VjqBA/640?from=appmsg&wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROpOJeqXPCw9nczum5wWljME2ffOFQLvoRliaJx8JTBaGMaqDTSsfCOb2EhYIt1XdIyRoAC61h3nyh2Z0GV5CJobickcRHEWM414/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNdvUSazZWnOhTibRiboBatictYotQSdjic70TRxLEIS6BHLtRmN7NUl0BA750ZNhc3MMgAyOMHxYHp8ZK5yjwHGnJW6sJic9wZP4ag/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROYQ9569PK7MImCPtCHrksyOBrmticIkYWicj84opN0jq5wliaqTUicib1shlsSsibibh5yDhMxm5rXvjRAyt8icz3ibBpibnqWicibqiaLVFpc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMcLTvjm7lOMdUiaWYf7m5bbab84REQkDVfib1XfV3sRUgWOwWH7icy0S21RKpsgGuicqOuNjNf3puwyBrGNsNicwh5cCbjWFy9bymU/640?wx_fmt=png&from=appmsg
