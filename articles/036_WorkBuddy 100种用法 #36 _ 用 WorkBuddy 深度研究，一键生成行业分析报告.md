# WorkBuddy 100种用法 #36 | 用 WorkBuddy 深度研究，一键生成行业分析报告

- 合集序号：36
- 公众号：我与ai的那些事
- 发布日期：2026-05-06
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328747&idx=1&sn=410e127de726b3424920ab30c0d98f5d&chksm=883032ecbf47bbfae62221ab22c574e5be79d155c2bf860063bc6431bf50e1e011264f9d8008#rd
- 正文字数：2412
- 正文图片：6

## 摘要

WorkBuddy 100种用法 #36 | 用 WorkBuddy 深度研究，一键生成行业分析报告\x0d\x0a导语

## 正文

新升级的WorkBuddy 新上线了的探索模块，里面有很多现成的模块供大家直接使用，其中的「深度研究」，能自动搜索多路来源、交叉比对、生成结构化报告。本文复盘一次真实使用：分析 AI Coding 行业 2023-2026 年的商业模式演变，从提问到出报告全程实录。

问题场景

前几天想系统理解 AI Coding 行业的商业模式演变，不只是"有哪些工具"，而是：

-
2023 年到现在，商业模式经历了哪几个阶段？

-
关键转折点是什么？谁驱动的？

-
国内外差异在哪？未来怎么走？

如果自己查，要打开十几个网页，摘数据、理时间线，非常耗时。

于是我打开了 WorkBuddy，用了一句 prompt：

@"深度研究" 分析 AI Coding 行业的商业模式演变，从 2023 年到现在，找出关键转折点和驱动因素。

解决过程

第一步：自动多路搜索

WorkBuddy 接收到指令后，自动并行搜索了多个维度：

-
英文关键词：AI coding assistant business model evolution 2023 2024 2025

-
中文关键词：AI编程助手 商业模式 演变 2023 2024 2025 关键点 转折点

-
厂商定价关键词：Cursor Replit GitHub Copilot pricing strategy business model

搜索结果中识别到几个高质量来源，自动抓取全文。

第二步：抓取并提取核心内容

WorkBuddy 自动访问了以下页面并提取结构化信息：

来源

核心内容

CSDN 博客

2023-2026 三阶段演变框架、厂商定价时间线

Qubittool 定价经济学

推理成本分析、Agent 模式 Token 消耗数据

EastonDev 全景盘点

2026 年市场格局、工具阵营分类、选型指南

第三步：生成结构化 Markdown 报告

提取完成后，WorkBuddy 自动生成了一份完整报告，包含：

-
摘要 — 四大核心结论

-
第一章 — 行业背景与市场规模（含数据表格）

-
第二章 — 商业模式演变三阶段

-
第三章 — 三大关键转折点深度分析

-
第四章 — 驱动因素（技术/市场/生态）

-
第五章 — 代表性公司策略对比

-
第六章 — 国内外商业模式差异

-
第七章 — 未来趋势预测（2026-2028）

-
第八章 — 结论与建议

-
附录 — 主要厂商定价一览表

第四步：转换为图文并茂的 HTML

Markdown 报告生成后，继续要求：

把完整报告处理成 HTML 格式

WorkBuddy 生成了一个单文件 HTML，内联 CSS，无外部依赖，系统字体栈，适配移动端。

完整地址：https://panda.yaniw.com/coding

关键发现（报告精选）

三大关键转折点

转折点一：2023 年下半年 — 中国厂商集体入局

阿里通义灵码（2023.10）、百度文心快码（2023.11）、讯飞星火编程（2023.12）三个月内相继发布，中国市场从"微软一家独大"变为"全球混战"。

转折点二：2024 年 8 月 — Trae 完全免费策略

字节跳动 Trae 以"不限次数、不限额量"完全免费入场，直接颠覆行业定价逻辑。用户数：2024.10 破 100 万，2025.03 破 500 万。

转折点三：2025 年 — Agent 模式商业化

Claude Code、GitHub Copilot Agent Mode、OpenAI Codex 相继推出。核心冲击是推理成本爆炸：

模式

Token 消耗量（单次）

估算成本

代码自动补全

100-1000

< $0.001

智能对话生成

5,000-20,000

$0.01-0.05

Agent 多步任务

100,000-500,000+

$0.5-5+

一次复杂 Agent 任务的推理成本可能超过 ，而20/月订阅费仅能覆盖 4-5 次此类任务。

这直接催生了混合定价（订阅制 + 按量付费）成为 2025-2026 年的主流商业模式。

国内外商业模式本质差异

维度

国际市场

中国市场

个人版定价

$10-20/月

几乎全部免费

核心竞争手段

技术领先、产品体验

免费 + 云生态 + 私有化部署

主要变现路径

直接订阅费

生态引流 + 企业服务

根本原因：中国市场的 AI Coding 工具几乎全部由云计算厂商推出，工具本身是"生态入口"而非"利润中心"。

2026 年市场格局三大阵营

阵营

代表产品

核心特征

AI IDE

Cursor、Windsurf

AI 是核心功能，非外挂

代码助手（插件）

GitHub Copilot、Tabnine

无需换编辑器

编程智能体（Agent）

Claude Code、Gemini CLI

自主规划执行，2026 最火方向

Agent 模式普及率 2026 年已达 55%，预计年底达 70%+。

关键步骤

如果你想复现这个流程，按这个顺序操作：

-

用 @深度研究 触发深度研究模式

-
在 WorkBuddy 选择深度研究: 然后写你的问题

-
深度研究模式会自动多路搜索，不需要手动指定搜索关键词

-

提问要具体，包含时间范围和产出要求

-
好的提问：分析 XX 行业从 2023 年到现在的商业模式演变，找出关键转折点和驱动因素

-
避免：帮我研究一下 XX

-

报告生成后，要求输出为 HTML

-
追加一句：把完整报告处理成 HTML 格式

-
WorkBuddy 会生成单文件、内联 CSS、无外部依赖的 HTML

-

HTML 报告预览

-
生成后 WorkBuddy 会自动弹出预览

-
可以直接用于分享、归档，或作为公众号素材

使用 tip

深度研究模式适合有明确分析框架需求的问题，比如"演变阶段""转折点""驱动因素""竞争格局"。如果问题太开放（比如"AI 怎么样"），它会搜很多但提炼不出结构。提问时把分析维度写进去，输出质量会高很多。

结语

这次实测让我印象最深的不是"搜到了多少"，而是 WorkBuddy 能自动把多路来源的信息交叉比对、去重、按时间线重新组织，最终输出一份有摘要、有数据表、有结论的完整报告。

以前做类似的行业分析，至少要花半天。现在从提问到拿到 HTML 报告，不超过 10 分钟。

这是WorkBuddy 100 种用法系列的36篇，持续更新中。关注我，探索WorkBuddy更多好玩法！

如果你有有趣的 WorkBuddy 使用场景，欢迎留言，说不定下一篇就是你的用法。

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROVlCfFbcyHHuqnUsl8tUh9m9qB2Xic6hiazLvv49gXxzKcAT4LULuTUPocf2jpN7eBpRAic3Lic9QISiaYQYXLuMWRGZRYT7XGK7js/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPCNuNOrPEZSxPIQY4KvbtClKqp3s8MWXwjfTR9sTMQAA7icOHAUQn8mtRWKddIwuRbZrWbMKKWzIxcC87DylfvkSrKicEdUcvfU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNEXjnQgl8BTH4zYWBoQEQJWQkRicB5GCbOFLg0qat9LAIrhaMewBhvknOhN3J8zGLJ4rYdCPLsPuWtvuUQ2GFGaI2roibbDzfia0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMaq48kKpo6f8heqrwhlN0eEgTr3epwPicrB651ysXdqVaIAjFeIBQB8C1rXUsicuggc5rNxQor7btRJYmhP7yfH7sMdRLlLnE7s/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMnQic4wgr8t4CqoickX6iclC3dOPFUAJVHstBAmafibfrZa5Q7AbUqic4TvQE2OWC87VLBPYPvSppcx1TuO6icSGzLZ8ickVVQmGT1iaE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMcBUSsIFnytfU0lNAhO9eg5npKxicupay40e2I8qjXiapcJoibE7knFYv7HQSuKQp86Sb8RmMJk6tl825Fw4hP8YoQicMULZnHkeQ/640?wx_fmt=png&from=appmsg
