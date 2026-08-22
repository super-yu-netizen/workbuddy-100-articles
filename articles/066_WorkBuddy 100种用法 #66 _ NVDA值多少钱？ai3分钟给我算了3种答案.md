# WorkBuddy 100种用法 #66 | NVDA值多少钱？ai3分钟给我算了3种答案

- 合集序号：66
- 公众号：我与ai的那些事
- 发布日期：2026-06-05
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329355&idx=1&sn=e0b7771931a00602176a81c711d266e3&chksm=8830344cbf47bd5a7dc884029593fba96358478eb13c6f09a83345172fa2e3d7271daebe2a66#rd
- 正文字数：1250
- 正文图片：5

## 摘要

一句话让WorkBuddy搭建英伟达DCF估值模型：三情景假设、WACC与终值敏感性分析，3分钟输出完整Excel。

## 正文

昨天下午，我突发奇想跟 WorkBuddy 说了一句话：

"帮我给 NVIDIA 做一个完整的 DCF 估值，考虑 AI 芯片需求的 Bear/Base/Bull 三种情景。"

然后就去做别的事了。三分钟后回来，桌面上多了个 Excel 文件。

打开一看，好家伙——不是随便丢几个数字那种敷衍，是正经八百的投行级 DCF 模型。

先看数据

WorkBuddy 第一步是查 NVIDIA 的最新财务数据。

FY2025 全年营收 1304.5 亿美元，毛利率 75%，净利润 728.8 亿。当前市值大概 3.4 万亿，股价 218 美元左右。账上净现金 329 亿，现金流非常健康。

这些基础数据它自动从市场拉取，不用我手动填任何东西。

三个情景，一键生成

然后是关键部分——情景假设。

它自己设了三套逻辑自洽的假设：

Base Case（基准）：未来 5 年营收 CAGR 25%，WACC 12%，终端增长率 3%。假设 AI 芯片需求持续强劲，但竞争也在加剧。

Bear Case（悲观）：CAGR 降到 15%，WACC 提到 13%，终端增长率 2.5%。假设 ASIC 替代加速、大客户自研芯片冲击现有格局。

Bull Case（乐观）：CAGR 飙到 36%，WACC 降到 10.5%，终端增长率 3.5%。假设 NVIDIA 继续保持 AI 训练和推理的垄断地位。

三种情景的营收预测、FCF 折现、终值计算，全都给了出来。

两个敏感性分析表

这是我觉得最爽的部分。

WorkBuddy 不只给了三种固定情景，还做了两张敏感性分析表：

WACC 敏感性：WACC 从 9% 到 15%，终端增长率从 2% 到 4%，交叉出来每股内在价值。一眼就能看出哪个区间最敏感。

终端价值敏感性：终值乘数从 15x 到 35x，永续增长率从 2% 到 4%，又是一张交叉表。

两张表各有 25 个数据点，假设值不同，表格联动的是真实的 DCF 公式，不是贴死的数。

Excel 本身呢？

我看了下表的结构，两个 Sheet：

-
DCF Sheet：市场数据、历史财务、情景假设、利润表预测、自由现金流、DCF 估值、三张敏感性表

-
WACC Sheet：CAPM 模型、债务成本、资本结构、WACC 完整推导

总共 311 个公式，75 个敏感性分析公式。所有公式都是原生的，修改任意假设，结果自动联动。

这事儿的爽点在哪

说实话，我自己手动搭一个 DCF 模型，调研数据半小时，搭框架一小时，情境分析再来半小时，加起来小两个小时。

WorkBuddy 三分钟。

不是说你不用懂财务了——你得知道 WACC 是什么意思，得能判断它的参数给得合不合理，得会看结果。只是把「从零到一的体力活」变成了「审阅和调整」的脑力活。

这种感觉就跟你从手写代码变成让 Copilot 补全一样，但有质的区别：它不是补一两个函数，是干完了一整件活儿。

我觉得这才是 WorkBuddy 真正好用的地方：不是陪你聊天，是真做事。

这是 WorkBuddy 100种用法第66篇，持续日更，每篇都是真实场景。

关注我，一起探索 WorkBuddy 的更多玩法。

#WorkBuddy #DCF估值 #NVIDIA #英伟达 #财务建模 #AI工具 #效率工具 #投资分析 #公众号写作 #100种用法

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNvWHN3ZZaTLaYF7A12KmejnXWJgPHvTHFZX59DVNfG1jicJj57MRFjicIcSibrUWrwicuDuCBpBNVR4yWdEfRs3qOPiayTYYRdQBEE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPWQmXiauYxumWSFcnpw7C6FrlWLibOax8rx2Wia4ZCXiaaTmJo6MNu8CAWQJRntdNnotqvXRmj8DXBVjbxJvTyOmGfibjhYcPVOOYM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMkDL4yse1Ribk9nMTQUr6Pvic8IGkkGJwofO1KvnJnISsvhCN3ia5NC38O9Pvl9YWub3XgyAAoANH5QXlX1J2IS2M3C9lT0ib0ickI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM2meTYcpgrOZlp22hFefAMveLVES9Cfd0NO7ANibfhoCibSiczEkjd9c9zXfQE2BsSfAsvcopWtPxWjGhumDR9tsXdKjlnZqOeDY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPdfqkePoV1360zeFxvLVbk5RFUxfzVBPhHrb2amYyCgh7dBMXzpiax6UBibRLU2yFxiauJKEKbmBAic81r7LicybRKn9OQXXHgjbicc/640?wx_fmt=png&from=appmsg
