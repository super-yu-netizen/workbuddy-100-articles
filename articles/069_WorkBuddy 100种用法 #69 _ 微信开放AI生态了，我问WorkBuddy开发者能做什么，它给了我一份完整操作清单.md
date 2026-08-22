# WorkBuddy 100种用法 #69 | 微信开放AI生态了，我问WorkBuddy开发者能做什么，它给了我一份完整操作清单

- 合集序号：69
- 公众号：我与ai的那些事
- 发布日期：2026-06-08
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329427&idx=1&sn=6c8b2eb2a4949834a6fcb56d4b97c22b&chksm=88303414bf47bd02389600d89aecb1d911b6a1a2061a094183d1ae51f338b118f815aecb28cd#rd
- 正文字数：3982
- 正文图片：7

## 摘要

下午收到微信开发者推送——微信AI正式开放接入。问WorkBuddy作为开发者能做什么，从信息检索到完整接入清单，12步操作指南直接可执行。

## 正文

今天下午，我正在刷信息，突然收到微信开发者推送了一条消息——

微信 AI生态 开放给开发者接入了。

作为一个开发者，第一反应是：

我能做什么？

直接问核心问题

我直接把问题丢给了 WorkBuddy：

今天微信开放微信AI了，我作为开发者，能做什么？

WorkBuddy 没有给我泛泛而谈的回答。

WorkBuddy 做了什么

它做了三件事——

① 实时搜索当天最新信息

搜到了 2026年6月8日 华尔街见闻的报道——微信发布《关于开发者接入微信AI生态的指引》。

这就是为什么它看到了，而我还不知道。AI 的信息获取速度比刷手机快多了。

② 抓取微信官方开发文档

直接访问微信开放平台的开发者文档，拿到了第一手的接入指引。不是只看概览页，而是把相关子页面都抓了一遍：接入方式、运行机制、调试指南、最佳实践、设计规范……

③ 给出结构化分析

不是一段文字打发我，而是分成了清晰的层次来讲。

WorkBuddy 给出的答案

以下是 WorkBuddy 回复的核心内容：

微信AI到底是什么？

微信AI = 内置在微信里的 AI 智能体，用户右滑就能对话。

它最大的想象空间是——调用小程序来完成真实任务：订餐、预约、查订单、买票……

你作为开发者，核心要做的是：把你的小程序变成微信AI可以调用的"能力模块"。

两种接入模式

模式

成本

原理

适合谁

自动模式

零开发

平台自动分析你的小程序页面

快速上车

开发模式

需写代码

自己封装 Skill / 接口

有定制需求

两种可以同时开启。

关键时间线

2026-01 AI成长计划启动（送算力+Token）
2026-04 扩展到全行业
2026-06-08 ← 今天，发接入指引
近期 合规审批 → 灰度测试 → 正式上线

看到这个时间线的时候，我突然意识到——现在就是最好的入场时机。大部分人还在观望，提前卡位成本最低。

要一份可执行的清单

光知道"能做什么"还不够。我说：

好，给我一个具体的接入操作清单

然后 WorkBuddy 做了一件让我印象深刻的事——

它去抓了微信官方文档的所有相关子页面，基于第一手资料，输出了一份完整的操作清单。

WorkBuddy 输出的完整清单（精华版）

这份清单分为 3 个阶段、12 个步骤。

第一阶段：零成本上车（今天就能做）

Step 1 — 申请 AI 小程序成长计划

-
• 免费云开发环境 6 个月

-
• 腾讯混元大模型 1 亿 Token 额度

-
• 流量激励资源

访问：https://developers.weixin.qq.com/miniprogram/dev/ai/growth-plan

Step 2 — 后台开「自动模式」

-
• 入口：微信公众平台 → 基础功能 → AI能力

-
• 或「微信开发者助手」小程序 → 管理 → 微信AI管理

-
• 授权平台读取源码 → 零代码

-
• 平台自动分析你的页面，微信AI就能调用

这一步，10 分钟搞定。

第二阶段：开发模式（核心玩法）

WorkBuddy 把整个 SKILL 架构拆解得清清楚楚。

每个 SKILL 是什么？

一个独立子包，包含三个核心文件：

|-- your-skill/
| |-- SKILL.md # 业务说明书（给AI看的，≤16KB）
| |-- mcp.json # 接口定义（输入输出Schema，≤24KB）
| |-- index.js # 注册所有原子接口（必须）
| |-- apis/ # 原子接口代码实现
| |-- components/ # 原子组件代码（GUI卡片）

mcp.json 怎么写？ WorkBuddy 直接给了示例：

{
"apis": [
{
"name": "getWeather",
"description": "查询当前位置或某地的未来天气",
"_meta": {
"ui": { "componentPath": "components/weather-card/index" }
},
"inputSchema": {
"type": "object",
"properties": {
"location": {
"type": "string",
"description": "要查询的地点"
},
"days": {
"type": "number",
"description": "预报天数，范围1-15，默认7"
}
},
"required": ["days"]
}
}
]
}

原子接口怎么实现？ 同样有代码示例：

// apis/getWeather.js
async function getWeather({ location, days }) {
// 你的业务逻辑...
return {
isError: false,
content: [{ type: "text", text: "已为您查询到北京未来3天天气" }],
structuredContent: {
location: "北京",
forecasts: [
{ date: "2026-06-09", weather: "晴", high: 28, low: 14 }
]
}
}
}
module.exports = getWeather

怎么注册到 index.js？

// index.js
const getWeather = require('./apis/getWeather')
const skill = wx.modelContext.createSkill('/path/to/pkg/weather-skill')
skill.registerAPI('getWeather', getWeather)

原子组件（GUI 卡片）怎么写？

Component({
lifetimes: {
created() {
const modelCtx = wx.modelContext.getContext(this)
const { NotificationType } = wx.modelContext
modelCtx.on(NotificationType.Result, (data) => {
this.setData({ weatherData: data.result.structuredContent })
})
}
}
})

甚至连中间件（统一登录、日志、错误处理）的写法都给了：

skill.use(async (ctx, next) => {
const token = wx.getStorageSync('token')
if (!token) {
const { code } = await wx.login()
// ... 登录逻辑
}
await next()
})

第三阶段：调试与提交

-
• 下载 Nightly 版微信开发者工具

-
• 用官方 Demo（github.com/wechat-miniprogram/ai-mode-demo）跑通流程

-
• 提交平台评测 → 通过后即可被微信AI调用

-
• ⚠️ 当前内测阶段暂未开放代码提审，可以先开发准备好

从这个过程中看到了什么

说实话，这次对话让我对 WorkBuddy 有了新的认识。

1. 它不只是"回答问题"，它会"做调研"

当我问"能做什么"时，它没有凭已有知识编答案，而是：

-
• 先搜索当天的新闻报道

-
• 再抓取微信官方的开发文档（多个子页面）

-
• 最后基于一手资料给出结论

这跟我自己去翻文档的效果一样，但它只用了几十秒。

2. 从模糊需求到可执行清单

"我能做什么"是一个很模糊的问题。WorkBuddy 把它变成了：

-
• 两张对比表（自动模式 vs 开发模式）

-
• 一个时间线

-
• 12 个步骤的操作清单

-
• 每一步都有具体的代码示例和文件路径

这就是从"信息"到"行动"的距离。

3. 当天消息，当天给我

微信AI开放是今天（2026-06-08）发布的消息。WorkBuddy 能搜到、能分析、能给出行动方案——而不是给我一个"我无法获取最新信息"的回复。

作为开发者，我的下一步计划

基于 WorkBuddy 给出的清单，我的计划是：

-
1. 本周 — 去后台开启自动模式，零成本上车

-
2. 下周 — 下载 Nightly 开发者工具 + 官方 Demo，跑通开发模式

-
3. 近期 — 结合我现在运营的公众号生态，想想哪些能力可以封装成 SKILL

如果你也是开发者，建议你也去看看。毕竟——

微信 13 亿用户，AI 是下一个流量入口。现在入场的成本最低。

相关资源

资源

地址

用途

微信AI总览指引

developers.weixin.qq.com[1]

官方入门

接入方式文档

integration[2]

SKILL封装细节

官方Demo

GitHub[3]

可运行的示例代码

最佳实践

best-practices[4]

SKILL设计经验

设计规范

design-guild[5]

卡片UI标准

AI成长计划

growth-plan[6]

申请Token和云资源

💬 你觉得微信AI开放后，最有潜力的应用场景是什么？ 欢迎评论区聊聊。

这是WorkBuddy 100种用法第69篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #微信AI #开发者 #SKILL封装 #小程序 #微信AI生态 #微信接入ai

引用链接

[1] developers.weixin.qq.com: https://developers.weixin.qq.com/miniprogram/dev/ai/guide
[2] integration: https://developers.weixin.qq.com/miniprogram/dev/ai/integration.html
[3] GitHub: https://github.com/wechat-miniprogram/ai-mode-demo
[4] best-practices: https://developers.weixin.qq.com/miniprogram/dev/ai/best-practices.html
[5] design-guild: https://developers.weixin.qq.com/miniprogram/dev/ai/design-guild.html
[6] growth-plan: https://developers.weixin.qq.com/miniprogram/dev/ai/growth-plan

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNANSzG0AcdYTrCqMqJtl0ty9RIRdJ3wicmyG2VOXYA6NdwcPlu24zJ8ia5XbkW4iaZCTqmZaqlbAF8SF8vw224GQ1bQeDnzicC1MQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPaSnZSqZejFBzeE3Cg7XNBZWe94CbHrepf3ngjMIefYISnkJyJSA0NwnReqYoanXg4CFfQvP79R60ctzsL0IsKniayrX31j7RQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP9hFau3l6Iw2aUmjrWc4ibSQGHzwmbjvKqwgOCs2X3Gd77Kx2FQ3t7I4Xnlswtia99HxUFSh2V3q0yT1iaQELy9ENPbiataHUibLgU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNHCW0t7SDhV0Zpibkm7B4TLDvQI0XRmN9R1Jv8qpm3oO0y3Sme0hJESYOGv1kXMSDo7SA6nDN1vlsK5xwBqxggOJ8iaFclGmXcY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPe0GdPXEABXaXPnfmuNFgOmQPMpxicpovJVsOuxDFibDib5Z3QWHBEFwpO3EmlQf6yUO5zLQUSETbWhCh59FtYCLW6XSMnp1ERek/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMOzuuZsf8eJoQ5xVWt7k8GKJbXZCNBjOibib8SCiaibOE2E74u7X8HibtoR9dSACcP2McKH98TPxawp9EgPFeQ4kS759RBG1GJge68/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMhTn6He1lMibD4SI0SQMGghEdyeES1CLOFRTxcprQThjWdeZ21kjQxIaCtbDtedQL5rAIlJVLqpKH8vq1Xa3CY53ZW4ticzkzGQ/640?wx_fmt=png&from=appmsg
