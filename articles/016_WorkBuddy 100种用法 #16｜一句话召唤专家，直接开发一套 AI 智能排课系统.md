# WorkBuddy 100种用法 #16｜一句话召唤专家，直接开发一套 AI 智能排课系统

- 合集序号：16
- 公众号：我与ai的那些事
- 发布日期：2026-04-15
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328245&idx=1&sn=f939577691d764661b0aaab4654ed6ff&chksm=883030f2bf47b9e46f2ae29a908f1d4b2b92804bcf417f30803a592ef29508b16b90b951a2db#rd
- 正文字数：2222
- 正文图片：11

## 摘要

WorkBuddy 100 种用法 #16，用一句话召唤专家开发，快速搭建含遗传算法的 AI 排课系统，全程架构、代码、调试一站式完成，效率翻倍。

## 正文

谁懂啊！只是好奇点开WorkBuddy专家里新更名的吴八哥（原will）高级开发工程师，随口问了一句：可以帮我开发一套排课系统吗？

结果它真的从0到1，完整输出了一套可落地、可商用的AI智能排课系统。

这篇就带你们完整复盘：从需求→架构→代码→Debug→完成可用版本，全程AI驱动的开发全过程。

第一步：随口一问，AI先把需求问透

我只抛了一句话需求，WorkBuddy没有盲目写代码，先精准锁定3个核心：

-
适用场景：中小学/高校教务排课

-
技术方案：Vue3 + FastAPI 前后端分离

-
核心能力：AI自动排课（遗传算法）

确认后直接给出完整设计方案，不用反复沟通。

第二步：系统架构一步到位，专业度拉满

技术栈选型

层级

技术

说明

前端

Vue 3 + TypeScript

现代响应式界面

UI框架

Element Plus

成熟组件库

状态管理

Pinia

轻量级状态管理

后端

FastAPI (Python)

高性能API + 内置AI算法

数据库

SQLite/PostgreSQL

关系型数据

AI引擎

遗传算法 + 约束规划

经典排课算法组合

核心功能模块

-
基础数据管理（学校、班级、教师、科目、教室）

-
排课规则引擎（硬约束+软约束）

-
AI自动排课引擎（遗传算法迭代优化）

-
智能调整建议

-
多视图可视化（班级/教师/教室）

开发阶段划分

-
Phase 1：项目初始化 + 数据库设计 + 基础CRUD（1-2天）

-
Phase 2：排课规则引擎 + 约束系统（2-3天）

-
Phase 3：AI遗传算法实现 + 自动排课（3-4天）

-
Phase 4：前端界面开发 + 可视化（3-4天）

-
Phase 5：智能调整 + 优化建议（2天）

-
Phase 6：测试 + 部署（1-2天）

第三步：一键生成完整项目框架

确认开始后，直接输出可直接开发的目录结构：

scheduling-system/
├── backend/ # FastAPI后端
│ ├── api/ # API路由（6个）
│ ├── core/ # 核心配置
│ ├── models/ # 数据模型
│ ├── scheduler/ # AI排课引擎
│ │ ├── constraints.py # 约束定义
│ │ ├── genetic_algorithm.py # 遗传算法
│ │ └── engine.py # 调度引擎
│ └── services/ # 业务逻辑
├── frontend/ # Vue3前端
│ ├── src/
│ │ ├── api/ # API调用
│ │ ├── views/ # 8个页面
│ │ └── stores/ # Pinia状态
└── README.md

已实现功能：

-
✅ 学校管理（CRUD）

-
✅ 班级管理（CRUD + 筛选）

-
✅ 教师管理（CRUD + 科目关联）

-
✅ 科目管理（CRUD）

-
✅ 教室管理（CRUD + 类型）

-
✅ AI排课（遗传算法引擎）

-
✅ 课表可视化（彩色表格）

AI排课亮点：

-
遗传算法参数可配置（种群大小、变异率、交叉率）

-
硬约束：教师/班级/教室时间冲突检测

-
软约束：连续课时限制

-
进度可视化：实时显示迭代进度和最优分数

第四步：数据库 + API 全部配齐

后端核心

-
12张业务数据表

-
7组完整RESTful API

-
数据库支持SQLite/PostgreSQL

-
内置示例数据初始化脚本

前端核心

-
API统一封装

-
Pinia全局状态

-
排课页面实时进度展示

-
多条件筛选与管理

第五步：真实踩坑Debug（开发必看）

Bug 1：表格没铺满

原因：Vite缓存导致样式不生效

解决：清空缓存重启

pkill -f "vite"
rm -rf node_modules/.vite
npm run dev

Bug 2：年级筛选不显示 / 不生效

原因：前端用grade?.name，后端只返回grade_id

解决：加辅助函数映射名称

function getGradeName(gradeId) {
if (!gradeId) return '未分配'
const grade = grades.value.find(g => g.id === gradeId)
return grade?.name || '未分配'
}

Bug 3：编辑保存无效

原因：API 缺失update方法、模型缺字段、中英文未转换

解决：补全 API、补充 Schema、做字段映射

Bug 4：排课不分配教室

原因：引擎未生成room_id

解决：按科目类型智能分配教室

-
物理/化学/生物（含实验室标记）→ 实验室

-
计算机/信息技术 → 计算机教室

-
音乐 → 音乐教室

-
美术 → 美术教室

-
体育 → 体育馆

-
其他 → 普通教室

最终效果

这套系统已完成完整开发，界面流畅、逻辑完整，可直接用于教务场景。

功能

状态

基础CRUD

✅

年级筛选与回显

✅

教室自动分配

✅

冲突检测

✅

遗传算法优化

✅

总结

AI 不是只能写 demo，WorkBuddy 这次直接交出可商用的完整系统。

-
从零开发至少 3–5 天

-
用 WorkBuddy：2 小时搞定主体框架

AI 擅长搭架构、写标准代码，实现复杂算法；人工负责业务细节、字段校验、边界场景，效率直接拉满。

这就是AI 赋能开发的真实样子：不替代人，而是让人把时间花在更有价值的地方。

这里是 「WorkBuddy 的 100 种用法」 系列第 16 期，持续更新 AI 办公、AI 开发、效率提升实战技巧。

#AI排课 #WorkBuddy #智能排课 #遗传算法 #Vue3 #FastAPI #教务系统 #开发效率 #WorkBuddy100用法

预览时标签不可点

微信扫一扫
关注该公众号

知道了

微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序

赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM7JnibgC1U61zpQJF5gsLvvmGQTXQOeic6LKUSOsu0wmQHxau1E1d6BjjoKFlPfbSlOC7GQCtfqssgN9b2FU03HwCIS64U13qac/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNRIfo2kNpNl62DfJWOAAjHibAPK69T0Zt0KO4dnGdGrG1kJKZboEEIghlTYrRsCVA90gq8oym4dA9S5Zicq1qJQQHibjayrZHdicE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP10RvmHdRWQ9QIiccqa6I9WyXYhWAUeniaBMDuiaNGkFlfBpo8bAtftib4Ch7dia1cToTia1orIxBXOUXtcVHELxXXibZwGdhYKXiavW4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNXW6arauibYAibHtEg7XOsMtCzXHncEMbtBP1jZMd5h0mtguHdzicLnoZMWLk9zlHYrL6icrvEXCBc6HRftGgEJUImtnDwcYzQv7w/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMUic4A2mxcodVTw1uks8ZhMR2DMoqaTp0CGuUdibmicv14Ss1eIzTKE4QO3V6LQyaHc7tEUN5h4wPs0lHEoNJQmCKfnHae54VdX8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMq4yVwCpknlicrfJ8Ta3sf4fAS7yicSNpF2qHRrDUBqfGFnLza4vJW2CPZPZNJaicgRHbIZTLkOLFJq9dvklD9qDiaXkwibRotNROU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPsRSwwc7naiaWnVQMS60tcIBh6QR9ZsQGiaK6vXeU6PKPPWibzMaE5ewgBquZ5exF4B9eHREPKW4iclWefDXWOtaWKpU2X8PYFfcA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP9eAGz9oGffe5XpibON4reQFd6tpvNPb8oX2eGSNhv5ykZUBp12lDPs2unQxQjcINJhCR6Pnm4gJE10r80NwP751354C7gZiawM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNk76lDibhv3Km3aZfdGYY4GG9E5ypEiaURh0twla9LhrGM1lob7ZMzNTFFiatBhictZ3icPAEBuZCfZRypFxCVyXuZ1wMiaEMctAUOg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPfVia3zcNAGVlnyGUSB8EB4cnuQibniaGOybJkjB8t5NatI32Ya4iaKVL46aD65OGvGCc10qKOQlZNndoWOEV2B81hvwpYEMAnJk8/640?wx_fmt=png&from=appmsg
- http://mmbiz.qpic.cn/sz_mmbiz_png/JvRAOtGGLJtAxia0Gjbls2as6IvpOJj4ovOaYKdNic2PcAj0u875xVN8h1Kk5AlQ23PgDTAjqMI7xPXDPPd0D0yQ/0?wx_fmt=png
