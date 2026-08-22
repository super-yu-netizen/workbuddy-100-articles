# WorkBuddy 100种用法 #91 | 扔一句话过去，AI给我搭了个博客还直接上线了

- 合集序号：91
- 公众号：我与ai的那些事
- 发布日期：2026-06-30
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330011&idx=1&sn=919300b0307b078991590097ad94fab3&chksm=883037dcbf47beca22c84e9488dd12042ff4df0f98bc82e5a6f8f314493599496f43be57e69c#rd
- 正文字数：1853
- 正文图片：8

## 摘要

一句话需求，AI 帮我搭好个人博客还直接上线了——含文章列表、标签分类、暗黑模式，零代码，30 秒部署，这就是 2026 年做内容创作者的爽感。

## 正文

下午突发奇想。我写公众号几个月了，文章越来越多，但都散在公众号后台。没有归档、没有标签检索、没有阅读体验好的文章页面。我就想：要不搭个个人博客？

但我对前端这一套不是很熟。要是以前，我得先找模板、改代码、配部署……半天起步。

这次我换了个思路。直接在 WorkBuddy 里打了一句话：

"帮我开发一个个人博客网站，主题是【我与AI的那些事】。要求：文章列表、文章详情、标签分类、关于页面，支持 Markdown 渲染。"

然后，我就看着它开工了。

30秒，它先定了个方案

WorkBuddy 没急着写代码。它先分析了一下需求，给我看了方案：

用纯 HTML/CSS/JS + SPA 架构，hash 路由，Markdown 用 marked.js 渲染，代码高亮用 highlight.js。不依赖任何框架，一个 index.html 搞定所有页面。

这个方案我一看就懂了——轻量、部署简单、不用装一堆依赖。

我说行，就这么搞。

然后它就开始写了

先写 HTML 结构——导航栏、主要内容区、页脚。然后写 CSS，我扫了一眼，品牌色直接用了我公众号封面的那个橙色（#FF6B35），自适应暗黑模式也有。

再然后是 6 篇示例文章——直接把我公众号最近写的内容变成 Markdown 写进去了，什么「IMA知识库搭AI客服」「AI拆65页PDF」「6个AI调研团队」……都是真实的文章素材。

最后写 JS 逻辑：路由跳转、文章渲染、标签筛选、全文搜索、阅读进度条。

全部一气呵成，零报错。

👆 首页效果。顶部是导航栏，中间是文章卡片列表，每篇有标题、日期、摘要、标签。点标签还能跳转筛选。

功能比我列的还多

我原本只说要四个页面。它做完之后我又多了一堆东西：

暗黑模式：右上角一个小月亮按钮，点一下全局切暗黑。偏好自动记住，下回打开不用重切。

全文搜索：顶部搜索框，实时过滤。搜「竞品」马上出「6个AI组了调研团队」那篇，搜「客服」出 IMA 那篇。

阅读进度条：打开文章，顶部一条橙色进度线跟着滚动走。读完的时候刚好到 100%，挺解压的。

上下篇导航：每篇文章底部自动链上一篇/下一篇，不用回首页找。

标签云：所有标签按文章数量排列，点哪个标签就列出该标签下的文章。

响应式：手机打开自动适配，导航变汉堡菜单，卡片排版变单列。

然后还写了个关于页面，里面自动把我的标签统计和系列介绍都放上去了。

然后我说了句：部署上线

就这么一句话。大概 30 秒，一个可访问的 HTTPS 链接就出来了。

🔗 https://74e7d628245849159e4c74ee18dbe858.app.codebuddy.work

点开一看，域名是 CodeBuddy 的沙箱环境，自动配了 HTTPS，直接能用。全站跑得很稳，文章、搜索、暗黑模式都没崩。

👆 部署后的线上效果，直接拿链接就能分享。

我的感受

说实话，半小时搭完一个博客网站，还直接部署上线，放一年前我是不信的。

以前搭网站这个事，光是选框架、配环境就能卡半天。现在对话里聊几分钟，一个完整可用的站就出来了。

而且不只是能用，是好看且好用的那种。品牌色、排版、动效、暗黑模式、响应式——这些细节以前要专门找设计师和前端配合，现在 AI 一口气全包了。

我脑子里突然冒出一个词：「想法即上线」。

你有一个想法，说出来，几分钟后它就在互联网上了。不是什么玩具 demo，是真能在线上跑、能分享给朋友看的完整产品。

经验总结

几点心得，给也想用 WorkBuddy 搭站的朋友：

1. 需求说清楚就行，不用给代码

我全程没写一行代码。说了要什么页面、什么功能，AI 自己设计方案、选技术栈、写代码。

2. 品牌色提前说好

因为我之前的项目记录里留了品牌色（#FF6B35），所以这次它直接用上了，整个网站调性统一。如果你是新项目，第一句话就把品牌色告诉它。

3. 部署就一句话的事

WorkBuddy 有内置的云部署能力。站搭好了，说「部署上线」，30 秒给链接。不需要自己搞服务器、配 Nginx、绑域名。

4. 文章数据和代码分离

这很关键。所有文章内容存在 js/articles.js 里，格式很清晰。以后发新文章，从公众号内容复制过来，稍微改一下格式就能上线。不需要每次改代码。

5. 可以随时迭代

上线之后不满意？在 WorkBuddy 里说「把导航栏颜色改一下」「加个回到顶部按钮」。它会基于现有代码改，不会从头来。

这是WorkBuddy 100种用法第91篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI建站 #个人博客 #AI编程 #内容创作 #公众号 #我与AI的那些事 #网站开发 #零代码 #效率工具

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRN7HMvjrkUR09zDK226YibzPaMotBLrzHaJjwOZV3yx9h0QWqYicrSwKUjIZibbNJWibjXRSoq8nNmgFIVwv26iakpcicYpFmibcibkT58/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRN02PSBAkPzcR85K2qbReNF4r2uUbsQEMxh6LUYDXjpODSPocibwhA3nOY4o4dLGC0DeiaibpE7ll4UrCUOkr3CeiaU5xQSxicYWiaVE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNsAjGHXLox0vjciaG5YtIVE1pia6fPhuwFb8XnMHRgGedBSsEvy9W9MyA6KH1QAIfzg5fbj31Mm5pVEAXicEm2d9o5ibr9Azugh7k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNkObO7UwfP5O8PzHNTiakwcDLsadYTpjPt6cvHhm3hRMUxd88FrtGJ88Jyic6nCQibZWkYAzibsdlGiaxYV0NKTYib42dgENNxkiaXEo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROichS6JDkU8ibX089uqlDga8vfibaDl6ia3WrZ4QGia93LAwQG9h3ic5bibESMUFvFL4Ytyia9Y2IicJnj2Nhv98lwuuYpgibJayuGNpOUY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP6KxXMyKbtq4u5iaCU4FpJ6oAPGblKO4e86suOMvVBcCKpJN6ZAGxcqpxiaqk8H8Qty4icDLhNPfhSia9UgplkPro9IddHBNAIElo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO2cxxR5QaP4Ol9rXZKBjjibkwK2Btg5TRZgibAETWbicDp5F6x1t2amBYxWcbNTtYrbXmwEcjEicjGRRhzXBeW98pWFgdER5ibPn54/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNA2RKA5LWrlcdNB0nG3c2iclJibkyxKxKs2dP0bvuQyVuF1wgRjBzkxtiafsUeAl0qTm0pBA0G21HFJhHmrgapH8XPZmhiaXhH4Gk/640?wx_fmt=png&from=appmsg
