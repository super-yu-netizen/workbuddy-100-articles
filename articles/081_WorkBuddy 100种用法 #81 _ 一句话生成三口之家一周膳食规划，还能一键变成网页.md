# WorkBuddy 100种用法 #81 | 一句话生成三口之家一周膳食规划，还能一键变成网页

- 合集序号：81
- 公众号：我与ai的那些事
- 发布日期：2026-06-20
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329830&idx=1&sn=20ab8ff8c435676aaff3ec878c965b5e&chksm=883036a1bf47bfb7aa2759e0e436b4db00e8536168dabe821788ad673a16068f4de392cbf171#rd
- 正文字数：2583
- 正文图片：11

## 摘要

逛WorkBuddy灵感页，点了一下「每周膳食规划表」的开同款，需求提示词自动填好，发送后瞬间生成三口之家一周膳食Excel——7天21餐含热量营养数据、采购清单、预算汇总。再一句话变精美网页，一键部署上线。零代码，三步完成。

## 正文

今天在逛 WorkBuddy 的「灵感」页面时，看到了一个有意思的东西

就是这个「每周膳食规划表」的效果卡片。

我当时也没多想，顺手点了下方的「开同款」——

你看，整个需求提示词就已经自动填好了，连格式都排好了：

请为一个三口之家（两位成人 + 一位 8 岁儿童）设计一份完整的一周膳食规划 Excel。

要求：

-
1. Sheet 1 周餐计划：周一到周日共 7 天、每天早 / 午 / 晚 3 餐；以中式家常菜为主、荤素搭配合理；每餐含菜名、主要食材、估算热量（kcal/人均）、准备时间；每天底部汇总人均热量、蛋白质、碳水、脂肪

-
2. Sheet 2 采购清单：按蔬菜 / 肉蛋 / 乳制品 / 主食 / 调味品分类汇总全周食材，含预估用量、参考单价、小计，底部汇总全周总预算

-
3. Sheet 3 营养摘要：7 天每日热量与三大营养素汇总、周均值，并与中国居民膳食指南推荐量对比

不同颜色区分早 / 午 / 晚餐，热量超标 / 达标分别标色。输出为 Excel 文件。

我一个字都没改，直接点了发送。

就这么简单——逛灵感 → 点开同款 → 发送，三步搞定。

第一步：Excel 出来了

它调用了Excel处理技能，用Python的openpyxl库生成了一个完整的Excel文件。Sheet1长这样——

周一到周日，每天早中晚三餐，每顿都有菜名、主要食材、人均热量(kcal)、蛋白质、碳水、脂肪(g)，还有准备时间(分钟)。每天底部有一行汇总公式(SUM)，自动把三顿的热量和营养素加起来。最后一行全周汇总用的是AVERAGE公式，算出七天的平均值。

Sheet2是采购清单，按蔬菜/肉蛋/乳制品/主食/调味品五大类分类。每项有预估用量、单位、参考单价、小计(用量×单价的公式)。每个分类有小计，最底部汇总出全周总预算：¥586.70。算下来人均日均食材成本不到28块。

Sheet3是营养摘要——把7天的数据拉成一张表，周均值直接对标《中国居民膳食指南(2022)》推荐量，偏差百分比自动计算，达标还是需要调整一目了然。

整个过程不到两分钟。

但说实话，拿到Excel之后我觉得还不够好。为什么？因为Excel这东西太"静态"了——你得有Office才能打开，发给别人还得传文件，手机上看体验也很差。

第二步：Excel → 精美网页

于是我又补了一句：

"帮我把这个规划做成HTML格式的。"

这次它换了一个技能——前端设计。把Excel里的所有数据提取出来，重新设计了一套交互式网页。

你们看这个效果——暖奶油色做底色，陶土色做点缀，标题用了手写体，看起来就像一本精致的家庭食谱。顶部写着"两位成人 + 一位8岁儿童"，下面三个Tab可以切换。

周餐计划Tab里面，七天都是卡片式布局，每天点一下标题栏就能展开/折叠。每顿饭前面有个彩色badge区分餐次：🟠 早餐浅橙、🔵 午餐浅蓝、🟢 晚餐浅绿。每道菜显示菜名和食材，右边是热量和三大营养素数据，准备时间也标出来了。每天的日汇总条显示当天总热量数据。最底下深色卡片展示全周均值。

采购清单Tab更直观——顶部彩色预算柱状图，一眼看出肉蛋占了46%是最大的开销（红色那段）。下面五个分类手风琴，蔬菜23种、肉蛋11种、乳制品3种、主食13种、调味品12种，全部可以展开收起查看明细。底部大字标着总预算¥586.70。

营养摘要Tab是我最喜欢的部分——数据表 + 四维度对比卡 + 可视化进度条，一应俱全。

那些进度条很直观：热量1809kcal vs 推荐2000kcal，差了9.6%但在达标范围内（绿色）；蛋白质85.3g超出推荐量31%（红色警告）；碳水197.4g偏低29.5%（黄色）；脂肪70.4g略高17.4%（橙色）。全部对标中国居民膳食指南。

下面还有四张评价卡，给出具体的改进建议："蛋白质偏高，以动物蛋白为主""碳水偏低可适当增加主食比例""脂肪偏高建议减少煎炸增加蒸煮"。

而且整个页面支持暗色模式切换，手机上看也没问题，响应式布局自动适配。

第三步：一键部署上线

做到这里已经很好了，但我想再往前推一步——既然是网页了，能不能让别人也能直接打开看？不用传文件，不用装软件？

我又说了第三句话：

"帮我把这个页面使用cloudstudio-deploy，部署到线上。"

几秒钟后它返回了一个链接。打开就是这个膳食规划网页的在线版本，任何人都能访问。

👉 在线预览地址：https://d75772c3b49a4cf7a72b5cf1af093e0c.app.codebuddy.work

这意味着什么？你点开这个链接，就能直接看到这篇讲的一周膳食规划完整网页——三Tab切换、营养对比、采购清单，全部在线可见。以后我每周更新一次内容，这个链接都不用换。

回顾一下整条链路

从开始到结束，整个过程是这样的：

搜灵感 → 说需求 → 拿到Excel
↓
再说一句 → 变成精美网页
↓
又说一句 → 在线可访问

三次对话，三种不同形态的结果。

背后其实是四个不同的能力在工作：

-
1. 数据处理——识别需求是Excel任务，调用openpyxl生成结构化表格，21餐×7个字段 + 62项采购食材 + 营养对比数据，全部带公式。

-
2. 前端设计——把表格数据重新组织成响应式网页，配色、字体、动画、暗色模式，AI自主决定设计方案。

-
3. 云端部署——上传静态文件到沙箱环境，启动HTTP服务，生成公开访问链接。

-
4. 技能串联——最关键的不是单个技能有多强，而是它能判断什么时候该用什么技能，然后串起来。

以前这种活儿怎么干？打开Excel手动建表→查营养数据→算热量→排版→如果要做网页还得学CSS→想分享得传文件……搞一天都不一定搞定。

现在变成了不停地说话，每次等几十秒就拿结果。

说点真心话

以前遇到"做个XX"的需求，第一反应是"我不会啊"。现在第一反应变成了"让WorkBuddy试试"。这不是偷懒，这是工具该有的样子——你描述你想要的，它帮你把中间的路走通。

特别是对于不擅长技术的人来说，这种"对话即产出"的方式，门槛真的几乎为零。你不需要知道什么是openpyxl，不需要懂CSS Grid怎么写，不需要了解云服务器是怎么回事。

你只需要知道自己想要什么。然后说出来就行。

这是WorkBuddy 100种用法第81篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI工具 #效率提升 #膳食规划 #Excel技巧 #前端设计 #自动化办公 #生活管理 #AI实战 #100种用法

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO7CCTxmASR64iary8Rjew7s6QZTCDRDggH6huemCAGDeEqS4TXeBHCxkwJ8QxHNaQO00NCicQ4496Re7Y3SicZI2Lha4Opok2h8A/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPspEDO6g9iaqeZbrOYsz9ica22IHX6UBJmr6zNjz7iaqwxXe6Wb2ZQlrYqAribQsQkVficiaibKrVlSauT72u44LGxx5O2jlNPME8elc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMPia3oLgPpDKaWbXmvIQCwVLrGwHs264TCG811PibFKC485FTLL5Z3zUd81W5E38IcNQeatLJOeukgKovEOtwXwY4Q5K4Micbg3o/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMJN5cibVzIDGQDZ4pWHMUnibQtK88F3X6NDRzIdQk0oKDaLW2PHxSJ1iaZpKEScAI9xicoUI8KZaxEg5Vic9awNBgJwF5QOCWWia5Og/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMq5mUoGRQORfCvqEnLibp6gkd7PiaA2jx1NGqTQra1VzypQSsBlKrW4pgniaA8zMQrVGicTk21tyibt9glVmIrRo51oyFpfdHmPyOc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMzbKW4k9SoKJDuEFichVJk2icTP6InTElVmdQUBAEljV1fofPN0Feauc1c9WPtN6Ia5ZXTxyvAfht1F2THm7Wq28JfPfvFSPstc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROmiaibicnR9kDG4HRkWhpg06tNRCRTcLjxVwJR1txc4pJv0gJn7c1l1ImnWTicF2Tu7UfP4Jiag0icFRic16gccdJmJdhlbLuUSCaEia4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROuFfaMiaqlYT2Lwvg2Uf1viau8CtHOkHCSS4ovicxyhedgaso1IPO0vxnfnGQ1FXHeVuBHiaLiasNanS1M62nxaIyuqcToQuLvBKUU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMbmmeVzGIibNaKGjuQG8ftcUnRgWEiceFYw80yWHlUWRWhRKUPeMQuTX2QnSXA3mqicpEjobVVWMTJoMQDBvIj2ibmRWbFwdheibp4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPG86qgFOC8IfdPxoNQeW6FHciamicPcaFlTUXarqu0gicVazyOwtnW7CRoiboErx3c1cDZmeYrCwR1vC1UzmwsR0nbDblx1e4ccvI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNwqGLR3HbLPXTE4p25TElcwh3zfuYXoehkKx60qw55x1xkw0w9hsdtwlbfmJEqgO5F3d79eODKzZ40uked60MxL5k1asiaxrdU/640?wx_fmt=png&from=appmsg
