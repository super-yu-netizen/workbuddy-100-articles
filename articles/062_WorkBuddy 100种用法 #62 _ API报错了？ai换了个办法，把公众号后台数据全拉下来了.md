# WorkBuddy 100种用法 #62 | API报错了？ai换了个办法，把公众号后台数据全拉下来了

- 合集序号：62
- 公众号：我与ai的那些事
- 发布日期：2026-06-01
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329286&idx=1&sn=07fb491d3f9073c930ec05aa6653256c&chksm=88303481bf47bd97e9d212e0211ca373eb784efcf1c228a8e26a3656eab6aabcc81c13d515ea#rd
- 正文字数：1630
- 正文图片：4

## 摘要

订阅号无数据API权限，让WorkBuddy用playwright模拟登录后台，抓取63篇文章阅读数据，再写脚本解析成JSON，任意维度随便查。

## 正文

昨天我想看看最近公众号的阅读数据——日更了两个多月，到底哪些文章受欢迎？哪篇爆了？每天阅读量是涨还是跌？

微信后台不是有「内容分析」嘛，我满心以为应该有接口可以直接拉。

结果让workBuddy一查——订阅号没有数据接口权限。

微信开放平台的 getarticletotal，只有服务号才能用。订阅号只配肉眼翻页。

行吧。那我换条路走。

正门不让进，那就走窗户

思路很简单：既然后台页面上有数据，那就让 WorkBuddy 打开浏览器，模拟我登录进去，把数据抓下来。

WorkBuddy 用 playwright 打开微信公众平台后台：

扫码登录之后，WorkBuddy 自动跳转到「已发布」内容列表页——每篇文章的标题、日期、阅读量、分享数、收藏数，都明明白白列在那里。

一页 20 条，我发了 63 篇，得翻 4 页。

WorkBuddy 一页一页翻，一条一条记。几分钟不到，63篇文章的全部数据拉下来了。

数据拿到了，但还乱着

抓下来的原始数据长这样——标题和数字混在一起，日期格式也不统一：

昨天 14:57 | WorkBuddy 100种用法 #61 | ... | 342 | 10 | 25
星期六 18:26 | ChatGPT Plus / Codex 账号注册协助服务 | 172 | 3 | 5
05月25日 | WorkBuddy 100种用法 #55 | ... | 350 | 13 | 51

这种格式没法直接分析。 WorkBuddy 写了个 Python 脚本，把每篇文章解析成结构化 JSON：自动识别日期格式（「昨天」「星期X」「MM月DD日」全兼容），自动提取系列编号，把阅读量、分享数、收藏数整理干净。

写这种解析脚本要是纯手写，光是日期匹配的 if-else 就能写十来行。WorkBuddy 一秒生成，跑一下，63 篇文章整整齐齐放进 JSON 里了。

想怎么查就怎么查

数据结构化之后，就随便玩了。

我先让 WorkBuddy 统计了 5 月 16 到 31 号的数据。但第一次跑完发现——怎么多出了两篇？一篇「AI实操交流群」，一篇「ChatGPT 注册协助服务」。这两篇不是 100 种用法系列的，不能算进去。

于是再加个过滤条件：只统计标题里带「100种用法」的。

结果出来了：

5 月 16~31 日，16 篇系列文章总阅读量：6,360 / 总分享：140日均阅读：398

我还顺便看了几个有意思的维度：

哪篇最火？ 第 48 期（用官方 Skill 让 WorkBuddy 接管微信读书），721 阅读，5 月 18 日发的。但放眼全系列，真正的爆款是第 18 期（Gemma 4 接入），16133 阅读——是平均水平的 13 倍。

哪篇最冷？ 第 57 期（腾讯问卷连接器），201 阅读。说实话我也有点意外，那篇内容不差，可能是标题弱了。

趋势如何？ 5 月上半月日均 455，下半月日均 340，下降了 25%。看着慌不慌？其实也不一定——5 月下半月开始发一些比较小众的玩法，数据波动正常。但这个趋势提醒我，选题还得再琢磨。

这次的经验

这件事教会我几个东西：

1. API 不给力的时候，浏览器就是最好的 API。 playwright skill 能直接操作网页、翻页、抓取内容，微信后台这种纯 HTML 页面，处理起来毫无压力。

2. 数据结构化是关键一步。 原始数据再完整，格式不统一就没法用。让 WorkBuddy 写解析脚本的时候，要把各种边界情况说清楚——比如这次日期格式就有三种（昨天、星期X、MM月DD日），不提前告诉它，解析就会漏。

3. 数据分析最重要的步骤：明确你要什么。 第一次跑出来包含了非系列文章，是因为我没说清楚过滤条件。第二次加了「只统计 100 种用法系列」的限制，结果就对了。AI 工具很能干，但指令得给清楚。

4. 一次搞定，以后随时用。 现在数据已经结构化好了，下次想看任意时间段、任意系列的数据，一句话就够了。

这是WorkBuddy 100种用法第62篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #公众号运营 #数据统计 #Playwright #Python爬虫 #浏览器自动化 #微信后台 #内容分析 #AI工具 #自媒体运营

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMbZVFeoh5WTyz6WFJAibey0P5dKibjZfhSk8nLXMQptAp8KEUialndvFfEI8WOxLoEnoRPG9Fa1NepibJQLekMYtlKYg2to9QuqQQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO5lYdcdCUZG2qsQhlXkgIUGtLQicMpkn0iayOWNIMNU6JHRxkzHB8B8Eh9ITfSAMQgTOaibrbiaGOFJwf8zKQ8s1G42Xjuwtl0Qiao/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMecvwvlDPljJUdWTNHxOSj07jOOlAg8d7VCArnsE6FqxeLwO6Br18sO5MddYwN2Z07TtsJfibbKq83TbxuGxdoiar2dtR00ZVS4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMpsXdrezok9bNq3I1DyRR07ibfXDJ09yIgic0uhjibkImgGdibA4I5nSFL1SetlP7mosuB1ArqO56crgk8gF7ibfdicOFdibhp261H3o/640?wx_fmt=png&from=appmsg
