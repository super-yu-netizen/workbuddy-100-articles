# WorkBuddy 100种用法 #31｜一个电话，三个AI专家，从零搭出道路救援系统原型

- 合集序号：31
- 公众号：我与ai的那些事
- 发布日期：2026-04-30
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328609&idx=1&sn=39c9ceebd08e94b66475de922e75e072&chksm=88303166bf47b870ba931366d539563b6fd295a04631452069503c68a02d7552b11f607ec65c#rd
- 正文字数：3902
- 正文图片：22

## 摘要

WorkBuddy专家模式实战：一个电话触发道路救援系统原型搭建。架构师出蓝图、开发工程师出施工图、原型工程师出效果图，三步流水线协作，一个下午完成传统方式需3-4周的工作。真实记录操作过程与核心交付。

## 正文

昨天中午，我哥突然打了个电话过来。

他说："你看能不能搞个道路救援的 App？"

就这么一句话。没有需求文档，没有竞品分析，没有预算说明，甚至连"我要哪些功能"都没说清楚。

我当时正准备午休，第一反应是：这玩意儿涉及车主端、师傅端、管理后台，还要实时定位、智能派单、支付结算……一个正经项目，光写方案可能就要两三周。

但转念一想，我现在有 WorkBuddy 的专家模式，试试呗。

三位专家，流水线作业

WorkBuddy 的专家中心（App 左侧边栏 →「专家」入口）里有 100 多个领域专家。我这次选了三位：

专家

职责

交付物

架构师

设计系统整体架构

可扩展架构设计方案文档

高级开发工程师

制定开发计划和技术方案

完整开发方案（含数据库、API、里程碑）

快速原型工程师

搭建可交互的产品原型

HTML 交互原型页面

操作很简单：点进专家中心 → 按分类浏览或搜索关键词 → 进入对话 → 输入需求就行。每个专家都是专属对话窗口，上下文独立，所以可以同时开多个专家并行沟通，也可以像这次一样串行——上一步的产出文件直接传给下一步的专家。

我的策略很清楚：架构师出蓝图 → 开发工程师出施工图 → 原型工程师出效果图。三步走，每一步的输出都是下一步的输入。

第一步：请架构师出蓝图

在专家中心找到「软件架构师」，点击进入专属对话窗口。

我的需求描述很直接：

我们正在开发道路救援app,系统,需要整体架构设计和长期发展规划,请软件架构师帮我们设计可扩展的系统架构。

几分钟后，架构师交付了一份完整的可扩展架构设计方案。

文档里我比较在意的几个点：

① 四层架构，职责清晰

用户触点层 → 车主App / 师傅App / 运营后台
业务网关层 → API网关 / 认证鉴权 / 限流熔断
核心服务层 → 订单 / 派单 / 用户 / 支付 / 位置 / 评价
基础设施层 → MySQL / Redis / Kafka / ES / OSS / K8s

不是上来就微服务，而是模块化单体起步，预留拆分接口。这个思路很务实。

② 智能派单引擎的设计

这是整个系统最核心的部分。架构师给的方案是评分模型：

score = 0.4×距离 + 0.3×技能匹配 + 0.2×评分 + 0.1×负载

还有三种派单模式：系统派单（自动推最优）、抢单模式（广播抢）、人工调度（特殊场景兜底）。

③ 三阶段演进路线

阶段

时间

目标

Phase 1 (MVP)

0-6个月

模块化单体，1-2个城市，5-8人团队

Phase 2 (规模化)

6-18个月

微服务拆分，智能派单上线，多城市

Phase 3 (平台化)

18+个月

SaaS赋能，AI诊断，IoT接入

光这份文档就有 9 个章节：设计原则、架构总览、核心服务设计、技术选型、数据架构、非功能性设计、演进路线、风险应对、团队配置。

说实话，如果是以前，找架构师出这样的方案，至少需要两三天的沟通和产出时间。

第二步：请开发工程师出施工图

回到专家中心，找到「高级开发工程师」，开一个新的对话窗口。我把架构师刚才产出的文档直接 给他,让他根据架构设计产出开发方案：

根据这个架构设计，给我出一份开发方案、

开发工程师看完后，交付了一份完整开发方案，细节程度远超预期。

① 项目结构已经定义好了

road-rescue/
├── rr-common/ # 通用模块
├── rr-gateway/ # API 网关
├── rr-service/ # 业务服务
│ ├── rr-user/ # 用户模块
│ ├── rr-order/ # 订单模块
│ ├── rr-dispatch/ # 派单模块
│ ├── rr-payment/ # 支付模块
│ ├── rr-location/ # 位置模块
│ └── rr-notification/# 通知模块
├── rr-admin/ # 管理后台
└── rr-app/ # 统一启动模块

MVP 阶段是模块化单体，按领域划包。将来拆微服务的时候，每个包直接拎出来就是。

② 数据库表结构全部设计好了

涉及 6 个模块共 11 张表，每张表都有完整的字段定义、类型、索引：

-
user 用户表 + driver_info 师傅扩展表 + vehicle 车辆表

-
rescue_order 订单主表 + order_event 事件流 + order_evaluation 评价表

-
dispatch_record 派单记录表

-
payment_record 支付记录表 + settlement_record 结算记录表

-
driver_location 位置表

连核心 SQL 索引都写好了：

CREATE INDEX idx_order_owner ON rescue_order(owner_id, status, created_at);
CREATE INDEX idx_order_driver ON rescue_order(driver_id, status, created_at);

③ API 接口清单全部列出来了

三个端（车主/师傅/管理后台）加起来 40+ 个接口，从认证登录到订单管理到结算统计，全部定义好了 RESTful 路径和方法。

④ Sprint 级别的开发里程碑

6 个月 MVP，拆成 12 个 Sprint（每个 2 周），每个 Sprint 有明确的任务分配和交付物：

Sprint

内容

核心交付

1-2

基础设施+骨架

可启动的空项目、CI/CD

3-4

用户体系+认证

三类用户注册登录

5-6

核心链路

订单创建+状态机+派单

7-8

支付+位置

微信/支付宝对接、GPS上报

9-10

联调优化

通知、评价、全链路联调

11-12

压测上线

性能测试、灰度发布

甚至连部署架构、服务器资源估算（约 8,000-12,000 元/月）、质量保障策略都写好了。

这份方案拿给任何一个 Java 开发团队，基本上可以直接开始干活了。

第三步：请原型工程师出效果图

这一步才是我觉得最惊艳的。

再次回到专家中心，找到「快速原型工程师」，进入对话。把架构文档和开发方案文档（架构方案 + 开发方案）一起发给它：

文件1架构设计方案 文件2开发方案 根据这两份文件，请快速原型工程师帮我们快速搭建产品原型。

然后，一个完整的可交互原型页面就出来了。

不是画个线框图，不是 Figma 里的静态页面，而是一个可以直接在浏览器里操作的 HTML 原型。

车主端

发单流程完整可走通：

选故障类型（爆胎/搭电/拖车/开锁/送油） → 地图定位 → 填写描述 → 费用预估（含夜间附加费） → 选支付方式 → 确认支付 → 看到订单进度条 → 实时追踪师傅位置

订单列表页也做了，进行中的订单有实时状态，已完成的可以评价（有星级+标签的评价弹窗）。

师傅端

新订单推送带实时倒计时，显示匹配评分和推荐理由。接单后卡片有滑出动画效果。

收入统计页有柱状图、收入构成分析、结算记录。

管理后台

管理后台做了 5 个子页面，侧边栏可以切换：

数据概览 — 核心指标卡片 + 24h 订单趋势 + 实时告警面板

智能调度中心 — 这个最硬核。有地图可视化（师傅分布+待救援点），旁边是派单评分引擎给出的 Top-3 推荐列表，每个师傅有详细的评分明细（距离分/技能分/评分/负载）。

订单管理 — 完整的订单列表，带状态筛选 师傅管理 — 师傅列表+资质审核操作 结算管理 — 日切结算批次+ GMV/平台费/师傅收入统计

整个原型用的是暗色紧急主题——深色背景配橙色强调色，很有专业救援的紧迫感。不用启动任何服务，直接浏览器打开 HTML 文件就能用。

回头看整个过程

从接到那个电话，到拿到三份交付物，整个过程大概是这样的：

电话："能不能搞个道路救援App？"
↓
找架构师 → 架构设计方案（9章节，含技术选型+演进路线）
↓
找开发工程师 → 开发方案（数据库+API+12个Sprint+部署方案）
↓
找原型工程师 → 可交互原型（3端5页面，浏览器直接打开）

三个专家，各自的领域深耕，每一步的输出自然成为下一步的输入。

架构师解决"怎么设计"，开发工程师解决"怎么开发"，原型工程师解决"长什么样"。

如果用传统方式：请架构师出方案（1-2周）→ 技术评审 → 开发团队写技术方案（1周）→ UI 设计师画原型（1-2周）→ 评审迭代。

整个过程可能需要3-4周，还不算中间的沟通成本和等待时间。

用 WorkBuddy 的专家模式，一个下午搞定蓝图 + 施工图 + 效果图。

几点真实感受

① 专家模式的核心价值不是"快"，是"专业"

单纯快没有意义，如果出来的方案不专业，后边返工更浪费时间。三位专家各自领域的深度——架构师对高可用/渐进演进的把控、开发工程师对数据库索引和 Spring 状态机的理解、原型工程师对交互细节的打磨——这些是省不掉的专业能力。

② 文件传递是关键

很多人用 AI 是一问一答，没有把上一步的产出传递给下一步。这次三个专家之间通过文件衔接，信息不丢失、不扭曲，这才是流水线式协作能跑通的原因。

③ 原型最大的价值是"对齐认知"

以前做项目，产品、开发、设计三方开完会，脑子里想的其实是三个不同的东西。一个可交互的原型，能让所有人看到的是同一个东西。我哥看完原型之后说："哦，原来长这样，行，我觉得可以。“这就够了。

明天再给我哥打个电话，把原型链接发给他。

让他自己点一点，比我说一万句都管用。

写在最后

这就是 WorkBuddy 的100种用法 第31篇。

这个系列从第1篇开始，每天都在更新。不贩卖焦虑，不讲空泛概念，只记录真实的使用场景和操作过程——今天遇到什么问题，用什么方式解决，结果如何。可以理解为一份持续更新的"AI工具实操日记"。

如果你也在用 WorkBuddy，或者对 AI 工具有兴趣但不知道从哪下手，欢迎关注这个系列。30篇下来，覆盖的场景已经不少了：内容创作、代码开发、数据分析、原型搭建……后面还会继续探索更多新的玩法。

关注公众号「我与AI的那些事」，每天一个真实使用案例，带你把 AI 工具真正用起来。

有想了解的场景，评论区留言，我来实测。

#WorkBuddy #AI架构师 #快速原型 #App开发 #道路救援 #专家模式 #AI工具 #产品原型 #技术方案 #项目管理 #持续日更 #workBuddy100种用法

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROuC1kia3dG26H9iajWpVYnjM50ttjQ5r3ibQacjnWiaNYlrLr8hee5fKh5rBzyXvBeXgMfR9a9W3MzjNJBZBRSQibrqIdJJdqNu6W8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROYgrzQQpnhIvazmM1kiavsiboXN6YLfxVSmCSAVcucd8gNH9epvcpRekTT3poibUOjOHoEmnoE2JAboc7Zee8ZjibATicSz2Tu8KXg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNmSveS4PRXia0oURUtNXWEfFD7fIlwEianq3sWXibJYUE0WezCFk8rnv9NcWBBxLoRKewzKlsXceOMmAgTSMtTiboyTWMjQq4KjwA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRN6UibqibcibnnfHft55jHkgegcIe2PibLnicFl8hSViaNvEVPDYgwJEytO4ia7HF7kQLP45EYPuB6U9XJI1A7M9ptNTicDia0g8ndILa3o/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROg3PpD3nUNzYziaS9TGrOTYoTb9r8k7IllQUADDU6Wlfv9X6gzyVDAAnljY2gvQEGTA7nok442ib4F7LkI1WrzUpIqtH2unZRVM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROQfIrIqsAZ4uf7LCmj2gUxvum6UhQtlxK5tYcIibiahib02MsXxdbg4U8pGrgIWNQlTFMQNDcjniaIichtrTrib8LzQMIqlqr5MbH2A/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN2AHRf5zyQqibcV4e4ibBYNicLXt3JgDfKbAfA8ibjJe2r9ichKI0ucYqJ1adiaomLsQjJRSRFwruBNKnJztJS1M8j75XJNgJThiaQCM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNvNibgpyFMrtiaDj1vVMN52gvMgdfjjzRFNN5C86IwfrdHtzkyWhGuk9ODRIBEXlACeke40zayPLJHKNRzReAZHDSE7ibiaFfuMVg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMslLbdAAJiatz1AeCvibXuHbLXK8fXg8huO3Qpa4Pj3K3hkp5cHLWCXtNZ2QmUV2Vv50HfA7qm0CHVhiavugZT9dvUZrk1A8nFYE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO4bqyS0eRnKHMoAqhYlexic5kf01dOicMgNmJUIvkIgLjicov5jDzsS7yQQVjqCicibbIpsUW1xDGHTT4egEr5EU3ibR29jBr5x5dlk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPYXoo0fOWwDCDprmBh8BvWwEAJ1cYcNCLbTWkJDCjPH8OS6g2vBIcQ1oGBtUzbTwXwDl3lszYDdictKAlYYVNptibSsrpyqNUI0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN2ibA7RibUVrl227afXIibbYV2Igtt9SicKP7YdtUXofmmibCReylicUtOqzq8OBNm8mE6V3UaEMVVjxVKicqP78zQLyYZ0WOp5vAZbE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP1flrzCNLHT6713qewluJ3xbibPhiamtnerJ8y2SrTgXkFOzJDjhicop9cdclq637JjIWDPel5HibIicwPVibR7kicGIuiaUPiaoItJicNM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRN1ZD7ByII9ibObiaic74cPXWCxqy3zdkZhbhPUNp9icpKR3gBZfwQRlFGafr7yOAWKoDCmlqw1sJLpnDBduSfank0WXCLrlW5Esd8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNfWq7PKGg8ueHBOLpT8iaARQYdHF4Y9BxJdkNjkiayTJNibOdF0fats20L707rM27MYhjX6ZrXxJYC6OWMQqicsvLFiawqHaWduslg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPZDXB9rHzGOd9G3lsc2EqzKKgLv2q43mmcYt7ULc24jWhZvzfTjKISWjX6lECwHReVbqicYPwUuBcg6ic4EiaFPdSshpWdntrvNM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPVfwkQGOOSPBhyCG1FjtUnic3F2q9JPUH0VxNE0OSzC1utYHKu9EIgGsNRzCrgBznKgBPAkSV0ibwZauvajTSt8IVG52RicWyMCU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROSJVywNa05q3MqxUF3A4ibQKGkrqQHUlm26jeuQITGx7pHNEfuauPsFL4ibIfDADjSBPqMXynnmg14Yiaxzg4rlyvxvk9Gc0b97Y/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNIeorTu9OibSvusF7CxEydkj1t5eXHQcwA3rWc7z4YKnI1UUJ9p4xqwQ1M8mmJZfhyY33OMOnRVk3m1ZXXVOq9xyaaw9z2oeIo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP24E1MMYy7o0jS3DKVclCMEt0cH0YnQkZ8Z0zFoxd9S2aeVStEehP0P5YhUibt5I9AA3HTXFjQpUjEQJeJdPZ4PzM4XV3x76MQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROjMicNZxYoGvn0HjjPNfJesDQypc9vfoia1Cymkan1EerXlr6mf0ffyJeJPYsNZQb27Bicobappc6JWDicUxAuiciaDMibZCAVuyCegc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP4v4XPBjyp8f6DUmFydoTvcmyI5mBicSyQFVCzFuXAcYhsIjh0tV1NmcBZAACZzHyNVBhp7KqA2zNd2nRojcY3TFpmUfqZyp4A/640?wx_fmt=png&from=appmsg
