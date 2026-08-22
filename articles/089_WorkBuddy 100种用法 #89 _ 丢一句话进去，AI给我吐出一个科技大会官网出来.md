# WorkBuddy 100种用法 #89 | 丢一句话进去，AI给我吐出一个科技大会官网出来

- 合集序号：89
- 公众号：我与ai的那些事
- 发布日期：2026-06-28
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329972&idx=1&sn=10e49d1561f15e314e7b1a5316e7b700&chksm=88303633bf47bf251e0e40276030027e57e70d2edb522848c0bbed7e2413773ae4d9415af31a#rd
- 正文字数：1663
- 正文图片：7

## 摘要

一句话生成完整科技大会官网，Hero倒计时、演讲阵容、日程报名全齐，1363行零依赖，一键上线。

## 正文

周末晚上闲着没事，我突然想测试一个事情。

如果我只用一句话，能不能让 WorkBuddy 帮我做出一个完整的、可以直接上线的大会官网？

不是那种套模板的简陋页面。我要的是有 Hero 大标题、实时倒计时、演讲者阵容、时间线日程、数字滚动动画、带校验的报名表单、Footer 社交图标——一个真正的 AI 科技大会落地页。

风格要 Apple + Mistral 那种极简风，大量留白，高端科技感。

就一句话。

然后我就看着它开始写了。

说实话我做好了心理准备——可能得来回改几轮，或者某些模块会缺斤少两。毕竟这么多东西，一个 HTML 就搞完，还不让用外部依赖，不现实吧？

结果它唰唰唰写完了。

1363 行。单文件。内联 CSS。零 CDN。全部原生 JS。

我直接在浏览器里打开，看到的效果是这样的：

顶部导航是毛玻璃效果，滚动以后自动出现模糊背景。

Hero 区域，大标题「AI Frontier 2026」，副标题「探索 AI 的下一个前沿」，日期、地点、两个 CTA 按钮。下面有一个实时倒计时——它自己设的目标日期是 2026 年 9 月 18 日，天、时、分、秒，逐秒跳动。

继续往下滚。

演讲者阵容，6 位嘉宾，用了一个 grid 网格布局。每个卡片有姓名、职位、公司，还有一个领域标签。hover 上去背景微微变色——Apple 风格那种克制的交互。

日程这里用了时间线布局。三天，Tab 切换。每天分上午/下午，每个环节用一条竖线串起来，圆点在线上。

而且每个环节有分类标签：Keynote、Workshop、圆桌、休息——用了不同颜色的 badge。这个细节我根本没在提示里说，它自己判断出来的。

再下面是数字亮点模块。黑底白字，整块反白。

四个数字：2000+ 参会者、30+ 演讲、12 个 Workshop、50+ 合作伙伴。

数字不是直接显示的——滚到可视区域的时候，数字会从 0 滚动到目标值。用的 ease-out cubic 缓动，看着非常舒服。

报名表单这边也挺讲究。四个字段：姓名、邮箱、公司、职位。每个都有校验——邮箱正则、必填提示。提交以后会显示 loading 动画（三个跳动的小圆点），然后切到成功状态。

这些交互逻辑全在一个 HTML 里，没有任何后端。

Footer 也很完整。品牌名、导览链接、社交图标（X、LinkedIn、微信、GitHub）——全是 SVG 手绘的，没用任何图标库。

到这我已经觉得这活干得不错了。

但我还想看看它能不能直接部署上线。

我说了一句「使用cloudstudio-deploy 部署上线」，WorkBuddy 调了 CloudStudio 的部署能力，把文件上传到沙箱，几秒钟给了我一个公网链接 https://e7c1ef3d214b4f99941659c29977905e.app.codebuddy.work。

你可以直接打开：一个完整的 AI 科技大会落地页，就这么上线了。

我复盘了一下

整个过程，我只做了三件事：

-
1. 丢了一个需求描述给它

-
2. 确认效果

-
3. 说「部署上线」

它做了多少呢？完整的工作包括：

-
• 设计系统：黑白主色 + accent warm 点缀，字体系统，圆角体系，CSS 变量统一管理

-
• 所有模块的布局和交互

-
• 倒计时的 JavaScript 逻辑

-
• 滚动渐入动画（IntersectionObserver）

-
• 数字递增动画（ease-out cubic）

-
• 表单校验和提交状态机

-
• 日程三天 Tab 切换

-
• 所有 SVG 图标手绘（没用图标库）

-
• 移动端响应式（两个断点）

-
• 无障碍：aria-label、role、prefers-reduced-motion 全都配了

-
• 顶部进度条、回到顶部按钮、导航吸顶磨砂

全是它自己干的。

我想说的是：现在这个阶段的 AI，已经不是「帮忙写一小段代码」的工具了。它能作为一个完整的前端开发者，从设计到实现到部署，一条龙完成。

这是WorkBuddy 100种用法第89篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI编程 #前端开发 #大会官网 #AI落地页 #一次性生成 #零代码部署 #CloudStudio #效率工具 #公众号运营

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROY0UpHwFHdkjtQxmKxcL9YI92K8ADyNu7R1ibUqqhAok9vicL0TJFia6XMCW5BYa0gQAJQ88WqY1tAnknSibyN1fhOrhvic4xic7vhg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNHVXx5h1icHR401QdzYaKiasf2aaJPypMr3b1L1rUmCccd8d2EwPsqOjhYicKQ002lb34wZZq9DgVpS3vJiaXGkqNqn7SxdyJR0p8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP45TjtQbUYzfpQXjbfhc5l9cTFzDPFoWdVxT0ibxmhAe7kWs1qhLkVAptB4ejaiccyNA2tsgTV3NGyDpaQLSqicTY9UNQOSK7Vr8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROMHePKRFYwxOXdYJ6uAQwuq4CGXNicickLs9Fl8ictic1J6ZqQCFGULczDUsZSPTW2J3XsSnjodWxfhwDTmtyrApMTaSN16TYjL5M/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROeQohloZKT1MLicZrNIplvwgzYmKu8wmqGzrJMWIiad3gsztFRvTsoAqjCiaSw5SLFhibQWE92ibz0eh6BbJSAiaTpbMK7gibPwJQOw4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRN49bsOXbsiaqGOibCeg5iaYzW7LgC4BuAUibBF9snhNTwLshibmzZMicjNCp12ngBk6IYjmCdPYBqDUrTJBHIt9N8ysX4xhlQ1zOH7U/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNpjeic71WHgnfDWYbTFWkehCKgkgHq4UNXBgXvzocLaOicWyCRIeSJzZJyHXBzYicERciaoicT3Lr6bUWUYFtGmR7Ot8oTbuGujzBc/640?wx_fmt=png&from=appmsg
