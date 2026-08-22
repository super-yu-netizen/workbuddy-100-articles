# WorkBuddy 100种用法 #25 | 让 AI 当你的数据分析师：从一个链接到交互仪表板

- 合集序号：25
- 公众号：我与ai的那些事
- 发布日期：2026-04-25
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328402&idx=1&sn=efd41d91edbc539300ec0ceda708ae3c&chksm=88303015bf47b903e0b2c988b0b79043ad268387ce19cedbd3ae62c810b49b1566ec48f39609#rd
- 正文字数：3137
- 正文图片：7

## 摘要

用一句话触发，从一个 Excel 下载链接开始，2 分钟完成 3,144 个美国县的贫困数据分析——包括字段口径、分布统计、异常诊断、交互仪表板和多年数据管道设计。

## 正文

我不是数据分析师，但我花了 2 分钟，让 AI 帮我完成了一份涵盖 3,144 个美国县的贫困数据分析——从数据下载、字段解释、分布统计、异常诊断，到一个完整的交互仪表板，再到多年数据管道的架构设计。

一句话触发，全程不用写代码。

今天这篇，就把这个过程完整还原给你看。

原始需求就是这一段话：

根据 USDA ERS 的县级贫困估计（2023）Excel，请你做一次"贫困水平分布 + 异常县诊断 + 与失业/收入的联动假设"分析。要求：字段解释与口径确认、分布分析（全国/州内/离群县）、异常诊断 Top 20（贫困率高但失业率不高）、最小可用仪表板设计（4 KPI + 3 图 + 1 明细表）、多年数据管道表结构设计。数据下载地址：https://www.ers.usda.gov/.../poverty-estimates-...2023.xlsx

这是一个对任何人类分析师来说都要花至少半天的任务。

对 WorkBuddy，是 2 分钟。

WorkBuddy 是怎么做的？

它没有让我一步一步喂数据、选列、选图表类型——它直接规划了整个分析链路，然后自动执行。

这里把核心步骤拆开给你看：

Step 1：加载技能 → 自动规划任务清单

收到需求后，WorkBuddy 第一步是加载了 data-analysis-workflows 技能。这个技能是专门为数据分析场景设计的，覆盖了从数据探索到可视化到仪表板的完整流程。

加载完成后，它拆出了一个 6 步任务清单，从上到下依次推进，保证每步都有明确的交付物。

Step 2：下载数据 + 口径确认

用 curl 命令直接下载了 USDA ERS 官网的 Excel 文件（726KB），然后用 Python 解析了两个 Sheet：

-
• Poverty Data 2023：3,144 条县级数据，34 个字段

-
• Variable Descriptions：每个字段的完整口径说明

关键发现： 这个数据集有完整的 90% 置信区间（CI）字段——每个估计值都带了上下界。这意味着分析时不能只看点估计，CI 宽度本身就是信息。

口径梳理结果如下：

类型

代表字段

说明

点估计（人数）

POVALL_2023

贫困人口绝对数

比率（%）

PCTPOVALL_2023

贫困率

置信区间

CI90LB/UB*

90% 上下界，中位宽度 ±5.2pp

收入估计

MEDHHINC_2023

中位家庭收入

⚠️ 缺失

无失业率字段

需外补 BLS LAUS 数据

Step 3：全国 + 州内分布分析

4 个关键数字先出来：

-
• 🇺🇸 全国贫困率 12.5%（约 4,076 万人）

-
• 💰 中位家庭收入 $77,719（县级区间 $29K–$174K）

-
• ⚠️ 贫困率超 20% 的高贫困县：455 个，占全国 14.5%

-
• 👶 儿童贫困率 16.0%，高于总体 3.5pp

州级冠亚榜：

贫困率最高的是路易斯安那（18.9%）、密西西比（18.3%）、新墨西哥（16.9%），这三个州长期处于美国贫困带的核心区域。

贫困率最低的是新罕布什尔（7.3%）、犹他（9.0%）、明尼苏达（9.2%）。

全国 3,144 个县的分布呈明显右偏：

-
• 约 60% 集中在 10–20% 区间

-
• 54 个县贫困率超 30%

-
• 最高峰值落在 10–15% 段（共 1,277 个县）

Step 4：异常诊断——最有价值的一步

这一步是整个分析最有意思的地方。

需求里说要找「贫困率高但失业率不高的县」——但问题是，这个数据集根本没有失业率字段。

WorkBuddy 没有卡住，而是做了一个定义上的替换：

用中位家庭收入代理"非失业"，定义双分位阈值：

-
• 贫困率 ≥ P75（17.4%）

-
• 中位收入 ≥ P50（$62,862）

同时满足这两个条件 = "结构性贫困悖论县"

这个定义其实更准确——它抓住的是「收入水平不低，但贫困率依然很高」这个悖论现象。

共识别出 23 个异常县，逐一给出假说：

前三名揭示了三种完全不同的机制：

1. Montgomery County, VA（贫困率 23.8%，收入 $67,620）
Virginia Tech 在这里。大量低收入学生被统计为贫困人口，但教职工撑起了县级中位收入。「大学城效应」——数据准确，但结构特殊。

2. West Feliciana Parish, LA（贫困率 22.3%，收入 $74,368，CI 宽 11pp ⚠️）
Angola 州立监狱就在这里。被监禁人口算入贫困统计，但家庭收入由监狱职工主导。注意 CI 宽度高达 11pp，这个估计本身的不确定性很高。

3. Kings County, NY（贫困率 19.1%，收入 $76,353）
布鲁克林。超富和超穷共存，中位数被「中间化」，掩盖了极端分化。需要看基尼系数才能真正理解这里发生了什么。

Step 5：完整交互仪表板上线

所有分析结果汇聚成一个 HTML 仪表板，在本地直接打开就能用：

仪表板包含：

-
• 4 个 KPI 卡（全国贫困率、中位收入、高贫困县比、儿童贫困率）

-
• 频率分布直方图（区间 × 县数）

-
• Top10 高/低贫困州对比（含全国均值参考线）

-
• 贫困率 × 中位收入散点图（异常象限橙色高亮，可悬停查看县名）

-
• 异常县 Top20 明细表（含 CI 宽度、假说标注、城乡类型）

Step 6：多年数据管道架构设计

分析完当下，WorkBuddy 还给出了把这份数据升级成多年纵向数据库的完整方案：

事实表 fact_county_poverty（主键：fips_code + year）：存所有贫困率、CI、收入字段，按年堆叠。

维度表 dim_geography：存县名、州、城乡分类（RUCC），用 SCD2 追踪城乡分类变化。

ETL 5 步：USDA 页面监控 → openpyxl 解析（跳过4行注释头）→ 数据质量校验 → UPSERT 加载 → 刷新仪表板。

扩充建议：补 BLS LAUS 失业率 + Census PEP 人口字段，才能真正做贫困-失业-收入三维联动。

我从这次分析里学到了什么？

几个值得记录下来的点：

1. CI 宽度是信号，不是装饰

很多分析师看数据只看点估计。但这次 West Feliciana Parish 的 CI 宽度超 11pp——这意味着真实值在 ±5.5pp 的范围内游动，做决策前必须先稳定这个估计。

2. 字段缺失不是终止信号，是定义机会

失业率字段没有，但 WorkBuddy 没有卡住。它用中位收入重新定义了「正常经济活跃」的代理指标，反而得到了一个更精准的异常定义。

3. 异常的背后都有结构原因

「贫困率高 × 收入不低」这 23 个县，每一个背后都有独特的结构解释：大学城、监狱、农业季节工、原住民聚居、收入极化。统计上的异常，往往对应现实里的制度性安排。

这次用到了哪些 WorkBuddy 能力？

能力

这次具体用法

技能加载（Skill）

自动识别任务类型，加载 data-analysis-workflows

命令行执行

curl 下载外部数据，python3 脚本直接运行

数据分析

pandas 全量统计、IQR 离群检测、双分位异常识别

可视化

Chart.js 仪表板，含散点图交互 + 自定义象限高亮插件

Playwright 截图

仪表板分区自动截图，供文章使用

架构设计

事实表/维度表设计 + ETL 5步骤 + SCD2 说明

任务管理

Todo 清单全程追踪，6 步全部完成 ✅

一句话总结

如果你手边有一个公开数据集想搞清楚，不需要会 Python，不需要会 SQL，不需要会数据可视化。

给 WorkBuddy 一个链接，说清楚你想知道什么——它会帮你把整条链路跑完。

你只需要看结果、做判断。

📢 这是「WorkBuddy 的 100 种用法」系列第 25 篇

日更中，每篇真实记录一次 WorkBuddy 的实操使用场景。

如果你觉得这系列有用，可以：

① 点一下右上角「关注"我与ai的那些事"（历史文章都在这里）

② 留言告诉我：你下一个想用 WorkBuddy 解决什么问题？ 我来帮你跑通。

#WorkBuddy #AI数据分析 #数据可视化 #USDA贫困数据 #异常诊断 #数据管道 #自动化分析 #仪表板 #公开数据 #人工智能工具

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMMYSjOtACPFtgKzcsIkvO3lGbInvUtLy7qxWAehnYIN000SQSNI5OloJd5QmQlHfibHPXS0OjKF8oXVu7OF2BGaphWS26Fnicow/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROwTejvibMMJ0HKRfWL6S74eMvCcbppZMNDy6b3FIWcnXpibz7MdeSbaRoWwmIjMPclMvrRyiaLxM1UGjZRibj2fBwo6rwAfDP6Cac/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM3Pg4kIDeOtyuENsUpCBWuwcrwm6E3L6RDdHzFGXwXAw0kPQLPq7K6g6xLrdcU9icpWM2VV4CUSGIVyicibfFCeDIdCl0tdXbKHk/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROCOYErjOZTZyD88p6uHoHloKtwliaibozYEAoKmrysEJ6WtU6gFFo5eb5ibynTAOfc4axGxJ5k87icEO6IzDLHgEjzcibwIOxnxQ1w/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMgW7Yk5PETseJq8EEU7sdnLnxaBib9OmO68Lsl6VvVktJ08Mia9Y3icLicNwMmJd8evTNyFwtcXFuiaqh3QafY4l1Z2SXzPobp26Kc/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROfUdCz4nxut7MDdmAX2vbRoKjkrAhNJe3eXEKecvndfmqxBBhSibbpu5Au3JUtaFUicP9o9qMcw0IYibCg4FGnfLticOy565iaLs2Y/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPejZJu1K0p4Xnu0mP6dcnruGPhRSnBfAH5H2U4XibHVsrxaagaw6FwbjHHRJMXb4eVYZMdIKgYPiaAyVBkD8OHpVaVEjUAhcTXU/640?wx_fmt=png
