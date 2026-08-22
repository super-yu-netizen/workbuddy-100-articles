# WorkBuddy 100种用法 #65 | 灵感里偶遇卡神，一句话AI日报自动上线

- 合集序号：65
- 公众号：我与ai的那些事
- 发布日期：2026-06-04
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329344&idx=1&sn=1fc8cbaec51a857dedca328db682b7ad&chksm=88303447bf47bd516d5fc5ce99fbcfa1afa388f2aa1ea5b912b25d443849962ca514c40b7814#rd
- 正文字数：1178
- 正文图片：4

## 摘要

逛 WorkBuddy 灵感页，偶遇卡神的「资讯速递专家」，一句话生成 AI 日报网页，顺手部署上线，全程不到 2 分钟。

## 正文

今天逛 WorkBuddy 的时候，随手点进了「更多」→「灵感」，想看看最近有什么新专家。

翻着翻着，在「数据智能」分类里看到了一个眼熟的名字——「资讯速递专家」，作者是「数字生命卡兹克」。

卡神啊，那必须召唤一下。

随口一问，整了个活

找到专家后，我随手发了条消息：

「今天 AI 圈有什么新动态？」

本来以为就是个普通的问答——结果这哥们直接搞了个大活。

WorkBuddy 调用了 aihot 技能，去 aihot.viractor.com 把最新的 AI 资讯全拉下来了，然后把26条内容整理成了一个精美的 HTML 简报页面。

页面长这样：

-
深色/浅色主题自适应（跟着系统走）

-
五大版块卡片式布局：模型发布、产品更新、行业动态、论文研究、技巧与观点

-
每条资讯都有可点击的标题、来源、相对时间、摘要

-
完全内联 CSS，零外部依赖，浏览器直接打开

我看到这个页面的时候有点懵——这真的是随口一句话搞出来的？

既然生成了，顺手上个线

都做到这份上了，不如直接部署出去。我说了句：

「把这个部署到线上去」

WorkBuddy 调用 cloudstudio-deploy 技能，三下五除二：

-
把 HTML 拷贝到部署目录

-
启动静态文件服务

-
返回可分享链接

✅ 部署成功！

分享链接：
https://7fb7c1efb9cc43fd8f7baad189ba1360.app.codebuddy.work

点开链接，完整页面就出来了，和在本地打开一模一样。

复盘一下，就两步

步骤

你说的话

WorkBuddy 做的事

1

「今天 AI 圈有什么新动态？」

调用 aihot 技能拉取最新26条资讯，生成精美 HTML 简报

2

「部署到线上去」

调用 cloudstudio-deploy，生成可分享链接

从召唤专家到拿到分享链接，全程不到2分钟。

能干嘛用？

-
快速刷 AI 圈动态——不用到处翻，一个页面搞定

-
团队内部分享——部署成链接发群里，同事点开就能看

-
日常存档——每天简报存下来，回顾的时候很有用

-
找选题——翻翻最近 AI 圈在热议什么，灵感说来就来

几个小提醒

-
aihot 数据每天北京时间 08:00 更新，早上8点前查会 fallback 到昨天日报

-
部署链接是临时的，CloudStudio 沙箱有时限，长期存建议保存 HTML 文件

-
简报是中文的，每条都保留原文链接，点标题跳原网页

小结

以前做这种事，我得自己：

-
找资讯源

-
手动整理

-
写 HTML/CSS

-
部署到服务器

现在？逛个灵感、召唤卡神、说句话，全搞定了。

AI 工具最爽的地方，不是它能做什么惊天动地的大事，而是把那些「你知道该做但一直懒得做」的事，变成逛着逛着就顺手完成的日常。

这是WorkBuddy 100种用法第65篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI工具 #AI资讯 #AI日报 #效率工具 #AI简报 #代码助手 #自动化 #AI圈 #WorkBuddy100种用法

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMP65CKg2pwZgzU2LVgicsA5P9WAHnaSdTu9TRrZ8ZoLzBPzYHwAddO4WspfDgXibzCdH7mN4pcnGib9kdqfhDo659123nAJ5bYLc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMCBdhn81eJQI0YAdGb9LWealniaDE90KeIibG43ObicDOhvnLFyj4cl8gIpa1hOpF0OfU2ch8dPJMHqaw4UJxbAzyoSkYDAiaexnM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPthmPYcD06CpKk2E53lfYvHah1icQ0oBIVpvFsonoYkricibtanZF6GhUzStHljSDIbwhia0zqy7KAicwDzHnH3JIBk7NTH3BvqpYY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNZgk7IZPUYyCvnkElafXrjPpxlibQawMWicqzl1UTbw7mF5OibicVMYEFDc5hYoicdo2Dq2Vfmgiao0N9oyRJcuXJkLoFnTOt3ru2Fs/640?wx_fmt=png&from=appmsg
