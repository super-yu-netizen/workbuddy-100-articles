# WorkBuddy 100种用法 #87 | 写了3个月流水账，让AI帮我看了一眼后台数据

- 合集序号：87
- 公众号：我与ai的那些事
- 发布日期：2026-06-26
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329947&idx=1&sn=f2f91ce3812bde306f200bef4fcd80a3&chksm=8830361cbf47bf0af5ec6e9b71658b253b42dbf547e87361aaa97c3465b4d089311a6ad77999#rd
- 正文字数：2489
- 正文图片：11

## 摘要

写了3个月公众号，让AI爬了后台86篇文章全部数据。看完发现日常就600阅读，篇均1000+是被两篇爆款拉高的。顺手封装成Skill，以后一句话统计。

## 正文

写公众号快3，4个月了，100多篇堆在那儿，心里还是想大概知道一下：整体阅读量什么水平？每个月波动大不大？哪些方向的选题读者更愿意点开看？

不需要多精细——就像月底看一眼银行卡余额那种感觉，心里有个数就行。

问题是微信公众号后台没有这种全局视图，只能一篇一篇点进去看，100多篇点完手都酸了。

所以我想：让WorkBuddy直接帮我把后台数据全爬出来不就行了。

扫码登录，自动翻页

一开始我以为很简单，跟WorkBuddy说了一句："你能统计我的公众号文章阅读情况，并做简单的分析吗？"

它立刻问我：数据怎么来？

这就是问题所在——微信公众号后台没有开放API给普通用户，不能像调接口一样直接拿数据。WorkBuddy提出了三种方案：扫码登录、手动导出Excel、用AppID/AppSecret调API。

我选了第一个——扫码登录，它自动抓。

然后桌面弹出来一个Chromium窗口，里面是微信公众平台的登录二维码。用微信扫了一下，确认登录，浏览器就进后台了。

接下来WorkBuddy开始自己翻页。

它去的是「内容管理 → 发表记录」这个页面——这里有全部已发布文章的原始数据：阅读、分享、点赞、留言、划线、赞赏全都有。它一页一页地把数据拉下来，194条记录，跑了大概两三分钟全拿到了。

然后我拿到了原始JSON——每篇文章一条记录，字段包括：

-
read_num：阅读数

-
share_num：分享数

-
old_like_num：真实点赞数（这里有个坑，真实点赞藏在 old_like_num 字段，不是 like_num）

-
comment_num：留言数

-
line_info.line_count：划线数

-
reward_money：赞赏金额

数据结果一览

WorkBuddy按我要求，只筛选「WorkBuddy 100种用法」系列的文章，86篇，然后算了这些数据：

指标

数值

系列文章

86 篇（#1 ~ #86，无缺失）

总阅读

92000

总分享

10,500

总点赞

1,499

篇均阅读

1,074

阅读中位数

607

篇均1,074，中位数607——差了将近一倍，说明少数几篇拉高了整体。翻一下明细就知道是哪几篇了。

TOP 10 爆款

先看这张图：

TOP 3 出来的时候我有点意外。

第一名 #18《接入Gemma 4》，16,679阅读、2,339分享。当时只是随手写的一篇测评，没想到跑这么远。第二名 #15《豆包Seed生视频》 13,251阅读，同样是模型测评类。

第三名 #34《股票研究专家》 4,526阅读，很实用主义的选题。

从数据看，模型接入类内容（#18、#15、#27、#10）和股票金融类（#34、#13）的阅读表现明显更好。写的时候没刻意选方向，回头看数据才发现规律。

月度趋势：一条向下的线

再看这张图：

趋势很直白。

4月篇均2,036阅读，刚开号时两篇大爆款把数据拉得很高。

5月篇均794阅读，掉了一半多。

6月篇均526阅读，继续走低——而且6月我已经开始日更了，写得越多，单篇反而越淡。

这不意外。日更稀释了单篇的曝光窗口，公众号的推荐机制本来就更偏向间歇性爆款而非稳定输出。对记录号来说这个趋势很正常，知道就行了，不用焦虑。

阅读量的真实分布

最后这张图：

69% 的文章阅读量在 300–800 之间，这是我的日常水位。

超过1,200阅读的只有12篇，超过3,000的5篇。

这里有两个数字值得记住：

-
篇均阅读1,148 —— 被两篇爆款平均后的数字

-
中位数615 —— 一半文章在此之下

看后台时很容易盯着篇均1,000+，以为每篇都差不多。实际跑一遍数据才发现，日常就是600上下，那两篇万级阅读是例外而不是常态。

有数据的好处就在这儿——不用猜，不用自我怀疑，数字摆在那里一目了然。

封装成Skill，下次一句话搞定

数据拿到了、图表也画了，但工作还没完——

整个过程其实非常曲折。前面提到的那一堆坑：HttpOnly Cookie怎么拿、分页怎么处理、publish_page 字段要二次JSON解析、真实点赞藏在哪个字段……如果在脚本里硬写死，下次再跑可能又得改。

所以我干脆让WorkBuddy把这个能力封装成一个Skill。

什么意思呢？就是把这次踩完坑的完整流程——从扫码登录、翻页抓数据、字段解析、到输出JSON/CSV/HTML——打包成一个可重复调用的技能包。

封装完之后，我以后要统计数据，只需要一句话：

"统计公众号数据，最近30天的"

或者指定标题：

"统计 #50 到 #86 的数据"

或者指定日期区间：

"统计4月1号到6月25号的"

Skill自己会判断有没有登录态，没有就弹出浏览器让我扫码；有就直接抓。支持按日期、标题、系列筛选，输出JSON原始数据 + CSV明细 + HTML可视化报告三件套。

从两三个小时的折腾，变成了10秒对话。 这才是Skill真正的价值——不是让AI替你干一件事，而是让它把这件事的能力沉淀下来，以后再也不用从头来过。

带设计感的可视化报告

WorkBuddy最后还把这些数据生成了一个HTML报告，KPI卡片、TOP榜单、月度趋势柱状图、完整明细表都有。原始版本比较朴素，我让它用暖调编辑风格重新设计了一版：

暖奶油底色、焦橙主色、纸纹质感，数据展示变成了数据杂志的样子。

这次实践的收获

几个实实在在的结论：

-

日常阅读水位600左右，篇均1,000+是爆款效应。知道真实基线，心里有底。

-

模型接入类和股票金融类更受关注，写的时候没刻意选，回头数据帮我看清了。

-

日更的阅读量会走低是正常的，但它带来另外两个东西：搜索引擎的持续收录、读者的阅读习惯。这是记录号的长期价值，不急于一时的数字。

-

微信后台没有开放API，但WorkBuddy的浏览器自动化可以解决。下次想看数据，一句话就行，不用再手动翻页。

还有一个技术小细节：真实点赞藏在 old_like_num 字段里，不是 like_num。下次写类似脚本的时候省得踩坑。

这是WorkBuddy 100种用法第87篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI工具 #公众号运营 #数据分析 #微信公众号 #AI效率工具 #自动化 #公众号数据 #内容创作 #AI实战

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMTmAmic0QkMD55n2wVpT2n59MkBW7EIQn7wtRfk9bCoqbmibcXAG5tqvuuv3yicW5ibnS6WtTF51DzbcOuMAMq63VAISDnKziboP7g/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO5vicVTYxEoP4CBxlQcX0UZANakSdhcWYEHvic2icCWSclxM38g41GGyw7L0aTcnoUiclTiag9EuDlS6Ria13H0Of4c7zrF05IEhV1w/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROuIdm1ia4JzW2jiaaTNFse0GCbMwZmvI8wnTpM8rfljOVZckFUmKlChpnGIzIZHhVHzQAXy9CIQLgibIlYic52ShrEC8bjDBeCy7k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMdtA4fAAbJZZicelFiaI18I68UVy0XQIfAQBNQysRIFsiabwHGYcAfl7Jujn5e5ofv6iaD1cEupSRgI7MibUSX1LWMdkWUcBGymcTc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMnkLojjtxcUxTpBn9wicOELY5a3K1U4sYOpy6eVTjK02mcEKyiarn87JRKFjjbKoeXGxCb1Vrpvkm4jyEO1QZ4xXWHndfWHjkCs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPxIYggQ9yYSDcvNAZalQeYDKPt4x2TlPG6kiaaX4AL6JU3xbYpY6NC63cKmOj67GSTWVSZiczhwOpaXlNGEHiaK03p9hoj7R0T1I/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMJoT54znhxTLPSLxlibTamvdrIovyZ3icKuUPsObMmExC61FDlSbg9fD2Iq836yWk7Xe07u5CSb7E4b48RINERS3nryQG5Dx2xQ/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPicyAddTG3jd8TmdIpkqv0NOzsBWN8qVYducNOiaCCuEkUnGic5WicxQ1ug0IuicoJlcJ6XibZLwANJCPlFnUKjbyhbNKpVuhmDn63k/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROetv8ibbboSpFeaM4vsTH8uZwCTNM9g1cQNlITsjU7oON6uSGbrDDeicWhYrjlcV23MvvITiaHB3ziaSsxvgamQAWSRbQAicpcAl78/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPKvh66evMQbOMupibMghT7dg7J2iaibSm3uotAFSOsubhNvGibCIuOHtkpQXEq0sj9LuMlFl8mEqOLEToSbCLfDPVA2x1TANY6jlg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROpiahxHr8ZKV0TugiciclIO0YOdtYuFX6Y6IQOFR9xSx5BL8wl4TEaOjqxsGWia8CegNzKNNIvC286kFmRTIaWWZWW32CLlQTSXLQ/640?wx_fmt=png&from=appmsg
