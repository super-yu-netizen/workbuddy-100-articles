# WorkBuddy 100种用法 #82 | AI帮我分析热点案件，报告还直接上线了

- 合集序号：82
- 公众号：我与ai的那些事
- 发布日期：2026-06-21
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329856&idx=1&sn=7153fb46408449b321431c2bd2ef88d3&chksm=88303647bf47bf5147e7826fd2124b77a29b47b5d7348b9242c37735055785455a4f8c717093#rd
- 正文字数：2273
- 正文图片：11

## 摘要

重庆遇见小面起诉河南夫妻店渝见小面商标侵权，舆论哗然。我用WorkBuddy调用法律AI数据库，自动生成专业案件分析报告，还把报告做成了可视化网页直接上线——全程只说了几句话。

## 正文

前两天刷到个新闻，差点把我看乐了。

重庆的"遇见小面"，跑去河南南阳，把一个叫"渝见小面"的夫妻店给告了——说人家商标侵权。

我第一反应是：这也能告？"渝"是重庆的地名，"小面"是重庆小面的通用名称，这俩字凑一起，也能构成侵权？

但光靠直觉不行，我决定用 WorkBuddy 正儿八经分析一下这个案子。

先找个专业工具

正好前几天在刷公众号的时候，看到有人介绍了一个叫「案件分析报告（法律关系分析法Plus）」的 Skill——作者是浙江金道律师事务所的龚家勇律师。这个 Skill 能用法律关系分析法（三段论 + 五步骤框架）做案件分析，而且会自动调用一个叫华宇元典的法律数据库。我就先问了下workBuddy，这个skill有什么作用？

听起来很对路。但要用这个 Skill，得先装上华宇元典的 MCP 连接器。华宇元典是什么？简单说就是法律界的"事实闸门"——它能让 AI 检索真实的法律条文、类案、最高法答问，而不是靠"记忆"瞎编法条和案号。

安装华宇元典 MCP

整个过程大概5分钟，我截图记录了一下：

第一步：找到连接器

在 WorkBuddy 左侧点「连接器」，列表里翻一下就能看到「Huayu Yuandian Legal Data」：

第二步：点击连接

点那个 + 号，弹出连接弹窗，再点「连接」：

第三步：扫码登录/注册

跳转到华宇元典的页面，微信扫个码就行（新用户需要先注册）：

第四步：同意协议

勾选同意，点「同意并继续」：

第五步：确认授权

最后一步，确认给 WorkBuddy 授权调用元典的数据接口：

搞定。回到 WorkBuddy，状态显示「已连接」。

然后我又让 WorkBuddy 帮我把那个案件分析 Skill 从 SkillHub 装上，整个准备工作就完成了。

接下来我说了一句：

"帮我分析下案件，网上前两天的遇见小面状告河南夫妻店渝见小面事件。"

AI开始破案

接下来发生的事情，说实话有点超出我预期。

WorkBuddy 先是自己去网上把案件材料扒了下来——原告、被告、事实经过、索赔金额，全都有。

然后它调用了华宇元典 MCP，干了这几件事：

-
• 检索商标侵权的相关法律条文（《商标法》第五十七条、第五十九条）

-
• 查找"商标近似判断"的类案

-
• 重点搜索"地名正当使用"的判例

出来的报告，是按法律关系分析法走的：

第一阶段：发现案件事实

-
• 原告：遇见小面（重庆品牌，估值10亿）

-
• 被告：渝见小面（河南南阳夫妻店，面积不到100平）

-
• 索赔：3万元

-
• 反转：原告起诉后引发舆论反弹，火速撤诉

第二阶段：法律分析（五步骤）

争议焦点有四个，我挑最关键的说：

"渝见"和"遇见"是否构成近似商标？

结论：不构成。字形不同（渝 vs 遇）、含义不同（渝=重庆 vs 遇见=碰面）、仅有读音相同——不符合"音形义"综合比对标准。

"渝"字的使用是否正当？

结论：属于地名正当使用。《商标法》第五十九条明确规定，注册商标中含有的地名，他人正当使用的不构成侵权。被告是重庆人，"渝"是用来指示菜品地域特色的，不是拿来碰瓷的。

最狠的是，WorkBuddy 还找到了最高法的类案——"（2024）最高法民申1374号"，太平豆腐案，跟这个案子几乎一模一样，确立了"地名正当使用不构成侵权"的裁判规则。

报告出来了，但我想让它更好看

分析做完，WorkBuddy 给我生成了一份 Markdown 格式的案件分析报告，结构很完整，但……长得比较朴素。

我说，能不能把它做成 HTML，弄得像那么回事？

于是我用了另一个 Skill：frontend-design。

我跟它说，要"司法墨韵"风格——宣纸底色、朱砂红点缀、衬线字体，还得有侧边导航、时间线、法条引用卡片。

几分钟后，HTML 出来了。

我真觉得挺好看的，左侧有圆点导航，法条引用有红色左边框，争议焦点分析卡片里还嵌了三段论结构（大前提/小前提/结论）。字体用的是 Noto Serif SC，很有法律文书的那味。

最后一步：直接部署上线

报告做完了，我不想只存在自己电脑里。

我说，帮我把这个 HTML 部署到线上，让所有人都能看到。

WorkBuddy 调了 cloudstudio-deploy 这个 Skill，几分钟后，一个分享链接出来了：

https://9a4e284c5f9a4e3a904f74b45c5cc452.app.codebuddy.work

整个流程复盘

从"看到新闻"到"报告上线"，我干了什么？

-
1. 在公众号文章里发现法律分析 Skill → 安装华宇元典 MCP → 装上 Skill

-
2. 跟 WorkBuddy 说了一句"帮我分析这个案件"

-
3. 等它生成报告

-
4. 说了一句"做成 HTML"

-
5. 说了一句"部署到线上"

真正的操作，就是这几句话。

背后的东西，AI 全干了：

-
• 去网上扒案件材料

-
• 调用法律数据库检索法条和类案

-
• 按专业框架生成结构化报告

-
• 写 HTML + CSS 做成可视化页面

-
• 部署到云端

最后说两句

这个案子本身，其实挺典型的。

大品牌告小店铺，在法律上不是不能告，但得告得有道理。遇见小面这个案子，舆论反弹之后火速撤诉，某种程度上也说明了——他们自己的律师，可能也觉得赢面不大。

但对我来说，更有意思的是这个过程本身。

以前要做一个案件分析，你得：会法律检索、会写分析报告、会前端、会部署。现在，这些事 AI 都能帮你干，你只需要会问问题。

这不算什么"法律科技革命"，但确实，门槛降了很多。

这是WorkBuddy 100种用法第82篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI法律分析 #案件分析报告 #遇见小面 #渝见小面 #商标侵权 #AI工具 #法律关系分析法 #华宇元典 #100种用法

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO3w9N7PvDO7OP6kPac145ITbM2LCnc9PKBI7XyiamRjuIoy4L6Qexv0eGf66amyHgiaWicwaNdGyDxBYc7C9YglDMMXgibbNLbstQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNkNsGcSevf4jFKlE2icG4Y0pgpnQyaic6CL6XmwNY5EexkNvQibZxicaCAegpoWyjF8bTvJTA8LbQ8lwo7UYST81ia8Xia3MtVAfjLM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPQox2BVjib5pA8Sezc4oTAxTIk0QekefAe8KG2GnLePVtKicbUguJKrQFSlJy0MHutCibViaUkcJCibxcuzWFlLRIoKialrAxruKIgI/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNu56LRmRmlOyb2Ff7mbJQXvibwOxhEN4BDJZAWRiaDVOD0I4Y6rFTLQ4MnKHk6Pn5ibfI29w4F7JWhUfFptfY7Iu8ZicaIk4pziaQI/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRPI4lnqEHeOiajGvxsebh5sfmgMzF8C9GnV0MyVL6r1YGRcQB2nwCpw0GlLGQLAm7duI4XT8sU9sp04B1SpFToB3X6CNnZ15qGg/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMYk1lUbvu9sTGYnibdFp4cRDHxRzO0nvXYwNS7eygQP3rvoiaPfY9IGARvuvwHDb6redCC8GUjfOeO9edgGYbpUECkdAgGKUsF0/640?from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROib3F1c5wYmEUjo2GvWb9CfjS3ibbibAVibYGLGJshJ3sYZU5ByzicnmQNpcw4WueZP7kNokibUibsvkicKZgHGRXBa6anKJ4ZMLbdmFE/640?from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNcUgVgEMVQAcOC2132qXwFW99ibLTxfGgaiaKwpibxyricFOfYHZv04orxheyicVo7O0DkWeTU3H5P8dn6wwl2THc7X098MBOh1ZrY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROZbbpicqhR2JLLGOP0MyJnp5c4C8lsZBSMV3mRjEpjwDnvtDJuaCJ5GtTYRfZdIXRjqD1nicaDLIHY3CujCVEAhCfZibRmu55W84/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNC1nlWqGugCG56CP87RL5LDLmgia4ahCVJpGXueSFG5UqlR6nabp0xoxDib3M5jqDL301kudSLfymuOEHkKZGC6j0wSy523mes0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPTJza4UJXnb71tYd9a0xGNfNrrv3ibQicnZonKlX83NpzX7QWGIoyuUV4me6Ix52ubT7c5tIssJKf64dzyYRM76lMiawuN5JwlSs/640?wx_fmt=png&from=appmsg
