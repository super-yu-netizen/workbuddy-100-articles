# WorkBuddy 100种用法 #43 | 5分钟把AI热点数据变成晨报看板

- 合集序号：43
- 公众号：我与ai的那些事
- 发布日期：2026-05-13
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328903&idx=1&sn=2f7b9e52c4d73848a6a09af3dffe52dc&chksm=88303200bf47bb163dd3f939cf7caaa3791886b3597575814c015da34eccdcd223a921e91a0d#rd
- 正文字数：1726
- 正文图片：5

## 摘要

通过 WorkBuddy 的 AI HOT skill，一句话生成橙红渐变风格的 AI 日报仪表盘，支持全局编号、分类导航、时间格式化，可本地单文件打开，定时任务还可搭建成资讯网站。

## 正文

昨天在翻 WorkBuddy 的「探索」模块，就是那个点开侧边栏能看到很多现成功能的地方。

翻到有个跟 AI 日报有关的 skill，我就想——能不能不光看日报文字，让它帮我把数据拉出来，做成一个好看的看板？

每天早上信息太多，刷完一圈眼睛都累。如果有个仪表盘，直接显示今天有几条新闻、分哪几类、每条点开就能看原文，那就省事多了。

于是我跟 WorkBuddy 说了我的想法，把要求一次性写清楚发过去：

@skill:"AI HOT" 我想要今天的 AI 日报，请生成一个单文件 HTML 晨报仪表盘。

请按以下要求整理：

-
调用 aihot skill 的日报接口拉数据；如果当日 08:00 前还没生成，自动回退到最近一期

-
按五个固定版块分组：模型发布/更新、产品发布/更新、行业动态、论文研究、技巧与观点

-
编号贯穿全文（不在每个版块内重新计数），让我能一眼数出今天总条数

-
页面风格：橙红渐变晨报风，顶部 Hero 展示日期、总条数、五个版块统计；中部提供锚点导航；正文用响应式卡片网格展示资讯

-
每条资讯卡片包含：全局序号、标题、来源 chip、60 字以内中文摘要、原文跳转按钮；链接使用 target="_blank" rel="noopener noreferrer"

-
时间转成北京时间人话格式（"2 小时前" / "今天上午 09:48"），不要直接展示 ISO 字符串

-
文末加一行小字标注总条数和数据源

-
技术要求：纯 HTML/CSS/JS 单文件，所有样式与脚本内联，禁止外部资源；使用系统字体栈、CSS 变量、响应式布局、滚动渐入动画

说完之后 WorkBuddy 开始动手了。

它先调了 AI HOT 的接口，今天刚好是早上 8 点前，日报还没生成，它自动回退到了昨天最新的一期。这个逻辑我没单独说，它自己判断的。

然后开始写 Python 脚本，把拉到的数据格式化，生成 HTML 文件。

中间卡了一下。Python 有个小陷阱：用 f-string 写 HTML 模板，CSS 里全是大括号 {}，Python 会以为那是变量占位符，直接报错。

它发现这个问题后换了个办法——CSS 单独存成一个普通字符串，HTML 模板里只引用一次，彻底绕开了这个冲突。

还有一个更隐蔽的 bug：导航栏的 HTML 里有个括号没合上，生成的页面导航数字显示不对。发现后一行就修完了。

跑完脚本，生成了一个 ai_daily_dashboard.html 文件，打开就是这个效果：

今天这期一共 28 条。模型发布 3 条、产品发布 8 条、行业动态 6 条、论文研究 3 条、技巧与观点 8 条。

整个过程我就发了一条消息，后面全是 WorkBuddy 自己在跑。

遇到报错它自己诊断、自己改，改完继续跑。我就等结果就行了。

最后拿到的是一个 28KB 的 HTML 单文件，本地打开不需要网络，不需要任何依赖，直接用。

如果你也想做类似的数据看板，有一个小技巧：

配色改起来很简单，文件开头有 3 个颜色变量，改掉就换了整体风格：

:root {
--orange: #ff6b35; /* 主色 */
--red: #e63946; /* 渐变色 */
--gold: #ffb703; /* 强调色 */
}

不用懂 CSS，把颜色值换成你喜欢的颜色就行。

还能这么玩：搭一个自己的 AI 资讯网站

这个看板不只能手动生成一次，还能设成定时任务，每天自动跑。

比如设置成每天早上 8 点自动执行，WorkBuddy 拉数据、生成 HTML，然后推送到 GitHub 仓库里。再配上 Cloudflare Pages，每次推送自动触发部署，一分钟上线。

这样你就有了一个自己的 AI 资讯网站，每天一期，历史记录自动归档，随时可以按日期回溯查看。一个月下来就是 30 期可搜索的历史资料库。

不用每天刷各个网站，WorkBuddy 帮你收集、整理、发布一条龙。

想搭一套自己的 AI 资讯站吗？评论区说说，下次帮你实现。

你有每天固定要追的数据吗？

股价、天气、产品更新日志……只要能拉到接口数据，让 WorkBuddy 帮你做个看板也就是一句话的事。

评论区说说你的场景，下期帮你实现。

这是WorkBuddy 100 种用法第43篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI工具 #效率工具 #AI日报 #晨报看板 #AI资讯 #定时任务 #自动化 #GitHub #Cloudflare

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPYXNA8pyyhHWibsI48ajI4OORVBibUmYHNjJfR0GxqpKI7h6FPLXCp5NnWZFqWs025OI5zwD5n3pdqxLZZh2EA8do1wbtvpq7Yw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNFDZCz1SAmVX1mrwoc4tXA4UkeoqorHppkF7XfRdTdRf7LxApMSJVmEIOtyRuP4srcb2jYfFtyB6rnIebA6hLAVMiaAfrMCk8Y/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPYSq0vcZC3jxDG7xXpstP9IpzNCicUAHat9f6Z8lUIaNRwXEtCic1lPibnZb5CQtyyLgyicC92URQ1TVicCm4tX0661TSQNnzuqeiaY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMUv26xS0icAwYUfQsiauuWyZ8o9kRq707STt2OOxDFrDQ2t6OUJNkib8zw4qIGAK1dxnQKKSQTuhO89fr7njfTRxyUlN986rWmL8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPP29dUrFva4yKBIrlaSUtbGR76mJV98rAZpRqTGp2uBwhFYaqInmu8ibXicRfullKZwwiciaia4KhzupVcvwHkxxfddDTqBM2GAjQ8/640?wx_fmt=png&from=appmsg
