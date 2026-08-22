# WorkBuddy 100种用法 #55 | 写完网页不会部署？Cloudflare 技能一键搞定

- 合集序号：55
- 公众号：我与ai的那些事
- 发布日期：2026-05-25
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329140&idx=1&sn=9cc0de3ccad7784f62eaaa9599fe4083&chksm=88303373bf47ba651740ceafe3364096979b6aa93fcd3806b347a9907de4953aa9865bcc7b93#rd
- 正文字数：2509
- 正文图片：7

## 摘要

你有没有过这种经历——用 AI 花了半天写好了一个漂亮的网页，然后发现不会部署？

## 正文

你有没有过这种经历——用 AI 花了半天写好了一个漂亮的网页，然后发现不会部署？

买个服务器？配置域名？搞 Nginx？光想想就头大。

我之前也是这样。直到我发现 WorkBuddy 里面有个 Cloudflare 技能，直接把部署这件事降维成了"说一句话"。

今天用一个真实案例带你走完全流程：从零写一个产品展示页，到部署上线，全程不到 5 分钟。

起因：我想做一个产品展示页

我最近在测试一个想法——一款叫 WriteFlow 的 AI 写作工具的产品介绍页。

需求很简单：一个滚动叙事的长页面，要有视差背景、打字机效果、数字跳动计数这些花哨的动画。纯 HTML/CSS/JS，不依赖任何外部库。

需求丢给 WorkBuddy，大概 30 秒它就生成了一个完整的单文件页面。

效果很惊艳——6 个区块全部做了滚动动画，靛蓝到紫到粉的渐变配色，看起来很专业。

但问题来了：这个页面只在本地，怎么放到网上让别人看？

以前我会怎么搞？

如果按传统流程，大概是这样的：

-
1. 注册一个云服务器（阿里云/腾讯云）

-
2. 配置安全组、开放端口

-
3. 装 Nginx

-
4. 上传文件

-
5. 配置域名解析

-
6. 申请 SSL 证书

保守估计，至少 30 分钟，还得花不少钱。

而用 WorkBuddy 的 Cloudflare 技能，整个过程是这样的——

前置准备：安装 Cloudflare 技能

Cloudflare 技能不是 WorkBuddy 内置的，需要先安装。操作很简单：

-
1. 打开 WorkBuddy 左侧边栏，点击「技能」（Skills）

-
2. 在技能市场搜索 Cloudflare

-
3. 找到后点击安装

安装完成后，就能在任何对话里用 @Cloudflare 调用它了。

安装完之后，部署只需要两步

第一步：说一句话

我在对话里直接输入：

"@Cloudflare 帮我把这个页面部署到网上"

WorkBuddy 立刻识别到这是一个部署需求，自动加载了 Cloudflare 技能。

第二步：登录 + 确认

WorkBuddy 检查了一下环境：

-
• ✅ Wrangler（Cloudflare 的命令行工具）已安装

-
• ❌ 还没登录 Cloudflare 账号

它弹出一个选项让我选：

方案

说明

登录 Cloudflare 部署

用浏览器登录授权，部署到 Cloudflare Pages

用 CloudStudio 沙箱部署

不需要登录，但链接有时效

我选了第一个。然后它自动执行了 wrangler login，浏览器弹出 Cloudflare 的授权页面，我点了一下"允许"，就登录成功了。

登录完成后，WorkBuddy 自动执行了三步操作：

# 1. 创建项目
wrangler pages project create writeflow

# 2. 部署文件
wrangler pages deploy . --project-name writeflow --branch main

# 3. 部署完成，返回链接

整个过程全自动，我不需要手动输入任何命令。

结果：秒上线

几秒钟后，页面就上线了：

项目

信息

生产域名

writeflow-4lw.pages.dev

部署耗时

约 3 秒

费用

0 元

没错，Cloudflare Pages 免费套餐就能用，无需信用卡，无需绑定域名，自带 HTTPS 和全球 CDN。

Cloudflare 技能还能做什么？

Cloudflare 技能覆盖的能力远不止"部署静态页面"。我翻了一下它的技能说明，发现它其实是一个完整的 Cloudflare 平台操作指南：

计算类

能力

说明

Workers

边缘函数，在全球节点运行你的代码

Pages

静态网站部署，支持 Git 自动部署

Durable Objects

有状态的边缘计算

Workflows

多步骤任务编排

存储类

能力

说明

KV

键值存储，适合配置/缓存

D1

SQLite 数据库

R2

对象存储（兼容 S3）

Queues

消息队列

AI 类

能力

说明

Workers AI

边缘运行 AI 模型（LLM、图片生成等）

Vectorize

向量数据库，适合 RAG

AI Gateway

AI 网关，缓存/路由/限流

网络与安全

能力

说明

Tunnel

把本地服务暴露到公网

WAF

Web 应用防火墙

Turnstile

CAPTCHA 替代方案

也就是说，WorkBuddy 不仅能帮你写代码，还能帮你直接部署到 Cloudflare 的任何服务上。从写代码到上线，全在一个对话里完成。

如果部署出错了怎么办？

分享一个踩坑经历。

我第一次部署完成后，访问链接返回 404。排查了一下发现原因：我在对话里删除了部署用的临时目录，导致线上内容被清空了。

解决方法很简单——重新部署一次。WorkBuddy 直接执行了一行命令：

cp writeflow.html index.html && wrangler pages deploy . --project-name writeflow --branch main && rm index.html

3 秒搞定，页面立刻恢复正常。

这个命令的逻辑很清晰：把源文件复制为 index.html（Pages 默认入口）→ 部署 → 清理临时文件。

完整时间线

步骤

耗时

说明

写需求

30 秒

描述页面需求给 WorkBuddy

生成页面

~1 分钟

WorkBuddy 生成完整 HTML

触发部署

10 秒

@Cloudflare 技能

登录授权

15 秒

浏览器点一下

部署上线

3 秒

自动执行

合计

约 2 分钟

从需求到上线

对比传统方式（30 分钟 + 服务器费用），效率提升了 15 倍不止。

tip 💡

-
1. Wrangler 只需登录一次。登录成功后，后续部署不需要重复授权，直接用就行。

-
2. Cloudflare Pages 免费套餐每天 500 次构建、无限带宽，个人项目完全够用。

-
3. 如果想绑自己的域名，在 Cloudflare 控制台添加域名后，Pages 项目设置里可以一键绑定。

-
4. 每次更新只需一条命令：wrangler pages deploy . --project-name 你的项目名 --branch main，WorkBuddy 会帮你记住项目名。

-
5. 如果链接打不开，等 1-2 分钟让 DNS 生效，或者直接用部署时返回的预览链接访问。

互动时间 👇
你平时用什么方式部署网站？Vercel、Netlify、还是传统服务器？有没有被部署流程劝退过？评论区聊聊~

这是WorkBuddy 100 种用法第55篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROVuIpuS0UYwJGibbibbicGicaq15eDTQFuujYDePlVdWW5r41ektjvw5CygpEFAOvibmNK44syYFSGkv2NLUZj2iczJFk995MyCqWKI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROenBIAsftx0RjXdia9LHulzqiaibxnHOP73HGkia6MicFiaE4yWHoPFjK4kmibQ65ia3XaehiciaIbfQa64wWnUrc1ibwKL1pw6ekCdlphRg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNic1CUuwNQIBp0KmrrBBJGWs4KpX6ibv5kIzg5gZn7Bc8dMJr3v1Cv62AjhBJFrKAT5ic4ljZnzicxVNeI4yqqC6RcFcgyxK5H3CY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMglk6NXWg2ulcu9b56XaLfjAB3zBmkP5EyrjnEzQW7cPhBGoqea9BurKUokBMq6kgteAI12QZuhTrbGJAdP5khcHP3wvBzPI8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN27JNoT1c1jowAtpSJTK87kibPkibTfDEfDcianRHDuWDt6vgmTmIA7ciaQEn46p5m2lwTJo4R76fhq0svMTZic4I8kzdYxHnFpOPA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP3T91dEHvFf2ibEnUvFne7Ul40YXnWmUq6KqgeO35DkCBVricjuQHMoEZbHNooKhfSSGFR0J46NImhZlujtKGF7H43MIThogPxw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROVlSPduACTAIicWaw7ibfkTviaEdlf2u61fhnVibyWnWK2D8nTVYzbJq1Kcxj6lpugT1Kia8nFia5rvgiaX1jx4waVGv5uUlaD4rqBEc/640?wx_fmt=png&from=appmsg
