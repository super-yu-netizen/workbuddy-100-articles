# WorkBuddy 100种用法 #42 | 一句话生成专业数据清洗Excel报告

- 合集序号：42
- 公众号：我与ai的那些事
- 发布日期：2026-05-12
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328893&idx=1&sn=e4505c6e61d65df21427e50897a637eb&chksm=8830327abf47bb6c1a68553584494e3e1723b278363be09c1b6a94c0411349d743aed14498c3#rd
- 正文字数：1519
- 正文图片：7

## 摘要

用WorkBuddy处理电商数据，一句话生成专业数据清洗报告。自动识别重复、缺失、格式错误等问题，输出5个Sheet的Excel文件，清洗前后评分从72分提升到97分，全程无需手动调整。

## 正文

有个做电商的朋友，昨天找我吐槽。

客户给了一份交易数据让他出分析报告，结果打开一看——1000 行数据，各种脏：重复的、缺失的、日期格式三四种混着写、金额还有负数……

他说光整理这批数据就得两天，心态快崩了。

我让他把需求发我，然后打开了 WorkBuddy。

在「探索」里翻了一下，看到有个 CSV 数据清洗分析报告 的功能，正好对症。

点进去，把朋友描述的问题直接粘贴进去，发。

20 分钟后，我给他发了一个 .xlsx 文件。

他打开沉默了很久，然后回了一句：就这？

具体是什么问题呢，他那份数据里有：

-
几十条完全重复的记录

-
几十 个缺失值（客户邮箱、手机号、金额）

-
几十 条日期格式不统一（2024/01/15、2024-01-15、2024.01.15 混着写）

-
多 条金额明显异常（负数或超大值）

-
多 条邮箱格式错误

-
多 条手机号格式错误

-
商品分类名称还有 3 类写法不一致（「数码」「数码产品」「数码类」）

正常来说，这种数据要手工标记问题 → 写清洗日志 → 统计汇总 → 出报告，没两天搞不定。

WorkBuddy 生成的那个文件，打开是 5 个 Sheet：

Sheet1 · 原始数据

1050 行（含重复），问题单元格全部颜色标记：

-
浅红 = 重复记录

-
浅黄 = 缺失值

-
浅橙 = 格式错误

-
浅紫 = 异常值

拿到这份表，哪些数据有问题一眼就能看出来。

Sheet2 · 清洗日志

每一步操作都有记录：问题类型、影响行数、处理方法、处理结果。不是随便写写"已处理"，是真正能交给客户看的日志。

Sheet3 · 数据质量评分

清洗前后对比，用 Excel 公式自动算的，不是填死的数字：

维度

清洗前

清洗后

完整性

92%

100%

一致性

85%

100%

准确性

87%

97%

综合评分

72 分

97 分

Sheet4 · 统计汇总

按商品分类 + 按月份两张汇总表，含销售额、订单量、客单价，清洗完直接能拿去分析。

Sheet5 · 清洗后数据

1000 行干净数据，交给客户没问题。

朋友问我怎么这么快，我说我就是在 WorkBuddy 探索里找了个对应的功能，把你的需求粘进去就完了。

"Excel 文件处理根据这个文件origin_data.xlsx 帮我生成一份完整的 CSV 数据清洗分析报告 Excel，

具体要求如下： **业务背景**：我们是一家电商平台，最近导出了一份包含 1000 条交易记录的 CSV 文件 ，数据存在大量质量问题需要系统性清洗和分析。

**Sheet 1「原始数据 Raw Data」**： - 展示前 所有 行原始数据样本 - 有问题的单元格用特殊底色标记：重复行用浅红色(FFCCCC)、缺失值用浅黄色(FFFFCC)、格式错误用浅橙色(FFE0CC)、异常值用浅紫色(E8CCFF) - 首行冻结，添加自动筛选

**Sheet 2「清洗日志 Cleaning Log」**： - 记录每一步清洗操作，字段：序号、问题类型、影响字段、问题描述、处理方法、等

没有反复沟通，没有手动调整，WorkBuddy 自己把细节全处理了——

它知道质量评分要用公式，知道清洗日志要记影响行数，知道颜色要分 4 种对应不同问题类型，知道 Sheet 名要中英双语……

这些我没说，它自己懂。

你身边有没有那种"数据太脏、不想动手"的时刻？

发给我，我让 WorkBuddy 帮你跑一遍。

这篇文章是 WorkBuddy 100种用法系列的第42篇，这个系列我会持续日更，每天分享一个 WorkBuddy 的实战玩法。

系列进度：#42/100

下期想看我用 AI 搞什么？评论区告诉我~

觉得有用？

-
点个「在看」，让更多人看到

-
关注公众号「我与AI那些事」，第一时间收到更新

-
转发给你身边对 AI 工具感兴趣的朋友

每天一篇，坚持日更，我们下篇见 👋

#WorkBuddy #AI数据分析 #数据清洗 #Excel #效率工具 #电商数据 #自动化报告 #数据质量 #电商运营 #AI办公

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROVeUk0JNFKIicdcdhWE5XxUuI7Dngic2sCPtmqXfZqOPy7Azm9kQHc04L2pxNF862N7Ud8Fibunr3oRwibk8iaSwyvjZAWwrdNiaB0Y/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROuCic65mMw3icM3sH0m5w6KOnAV4Jdlk9tvjyLn1IrynsWmw8icxwcI9JhyiadK65WPV9QdQUiaeqCIbWsXq903xecJG7QDBelUaRk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMOiae8L99vRmhnuw2dpaa7f0noQ0GWHYWRulG1o3kwicJbZAh0HzoLI1e6wy70hO1WrDibKzqhHLnzeAMFhwiaAozLPNX4uic9ooYc/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRODeiaUeEN8uYr8GQia7SVCaFySH6yY1Q7ibEWL3sRaX7ADvqpa1ibZYnmJRXGT7Ru9YY71PrYatQXPoWDdiaER7IBQ5vSlSqBQVK5k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMFcY1hic1RvHzBNicpcTlQVDmicqYdQ8cibd02hvHpXGoohdxb3nYWetOgrMUg7sOfA9dxpblk3CChichf4IQicACMl1LJzOoCtx0hc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM2BNKLEpfOsdXjYSKw9STQt0tE5NtkEJMw7CEdS6iaUvdPI1SF7M4ibVeHLeKPCaA6XeXcDhicM0PP19D3t3ScDpSgB4tSg14FNQ/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPiaD2O7Y2py9sPhsHUS4iawf3VEwFL41ZgBvLCCOudjTEUwn10bCyE68lcsjqJn9XfoSYflgQ98GKW6XZm03VATfZjTiaib9aBslQ/640?wx_fmt=png
