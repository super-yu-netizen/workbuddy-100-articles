# WorkBuddy 100种用法 #50 | WorkBuddy × Ardot：AI驱动设计记账App的完整流程

- 合集序号：50
- 公众号：我与ai的那些事
- 发布日期：2026-05-20
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329063&idx=1&sn=bde0655d9f88b8375f9398e0d00b3ad2&chksm=883033a0bf47bab6101f23aab4e5d3701129f5182d76fc420be69e4db90be783ba5ea685ff28#rd
- 正文字数：4982
- 正文图片：11

## 摘要

用 WorkBuddy 召唤 Ardot 设计专家，对话生成5个页面的记账App全流程实录，含环境配置、6个常见踩坑及解决方案，2小时完成从零到可交互设计稿。

## 正文

前两天刷到Ardot公测的消息，手痒想试试。

如果你还不知道Ardot是啥——简单说就是一个设计工具，但跟Figma不一样的是，它可以通过对话来生成设计稿。而且它跟WorkBuddy做了集成，也就是说，我可以跟WorkBuddy聊天，让它帮我做设计。

听起来很酷对吧？

我决定试一下，做个稍微复杂点的东西——一个完整的记账App，5个页面那种。

第一步：下载安装Ardot

首先得把Ardot桌面版装起来。打开 ardot.tencent.com[1]，右上角有个"下载客户端"按钮。

目前支持 macOS（Intel 和 Apple 芯片）、Windows（即将上线），根据自己的系统选就行。

下载安装后打开，需要登录。支持微信扫码、手机号、邮箱三种方式，我用微信扫码直接登的，10秒搞定。

第二步：配置Ardot MCP

登录进去之后，界面还挺清爽的。但我不是要手动拖拖拽拽做设计——我要的是让WorkBuddy来操作它。

这就得配置MCP（Model Context Protocol）连接了。点击界面右上角的 "MCP 设置" 按钮。

会弹出一个 "MCP 集成" 窗口，里面列出了能对接的AI终端：CodeBuddy Code、CodeBuddy IDE、WorkBuddy、Claude Code、Cursor、Codex CLI 等等。把 WorkBuddy 那个开关打开。

这还没完。切换到WorkBuddy这边，在连接器页面找到Ardot MCP服务，会看到一个提示："首次连接此MCP服务需要您的信任确认"。必须点一下 "信任"按钮，不然WorkBuddy调不动Ardot。

这个设计有点反直觉——我以为在Ardot里开了开关就完事了，结果两边都得确认。点完就好了。

注意点总结：

-
Ardot必须保持运行状态，MCP服务是它本地启动的（默认在 http://127.0.0.1:50501/api/v1/mcp）

-
两边都要确认：Ardot里开WorkBuddy开关 + WorkBuddy里点信任按钮，缺一不可

-
不要关Ardot：如果Ardot退出了，MCP服务会断，WorkBuddy就调不动了

最后一个配置：安装 ardot-design-assistant 技能

光连上MCP还不够，WorkBuddy得知道怎么操作Ardot的画布。这个技能包含了完整的设计 workflow（9步标准流程、Agent Team模式、设计规则等等）。在技能市场里搜一下就能装。

到这里，环境才算真正配好。

最后一步：召唤Ardot设计专家

光有技能还不够，得找个专业的人来干这个活儿。在WorkBuddy的专家中心里，搜一下就能找到 "Ardot 设计专家"（作者是林觉初），点击**"召唤"**按钮，让它帮你搞定设计。

这个专家已经预设好了完整的Ardot设计workflow（9步标准流程、Agent Team模式、设计规则等等），你不需要自己写复杂的操作指令，直接描述需求就行。

第三步：提需求（30秒）

我跟WorkBuddy说：

"帮我设计一个记账App，要5个页面（首页/记一笔/统计/账户/我的），现代简约风格，通用移动端（不要iOS或Android专属）。"

然后它就开始了。

第四步：AI自动生成设计

WorkBuddy调用了Ardot的设计能力，自动创建了5个iPhone尺寸的画面（375×812），每个页面对应一个功能模块。

我看着它一点点把页面搭出来，说实话挺震撼的——它真的在"写设计"，不是拖拖拽拽，而是直接生成结构化的设计文件。

生成的5个页面：

1. 首页（Dashboard）- 总览当月收支

绿色主题（#2DB87B），顶部显示当月总支出和总收入，下方是最近交易记录。底部4个Tab（首页/统计/账户/我的）。

2. 记一笔（Add Record）- 快速添加交易

顶部有支出/收入切换按钮（红色/绿色），下方是10个常用分类：餐饮🍔/交通🚌/购物🛍️/娱乐🎮/居住🏠/医疗💊/教育📚/旅行✈️/通讯📱/其他🔧。

每个分类用emoji+文字，垂直排列。

3. 统计（Statistics）- 数据可视化

用SVG画了一个环形图，展示各类支出占比：

-
餐饮 35%（红色）

-
交通 20%（橙色）

-
购物 15%（绿色）

-
...

环形图中间显示总支出，下方是分类排行榜，按金额从大到小排列。

4. 账户（Accounts）- 多账户管理

3种账户类型：

-
现金：¥2,580.00

-
招商银行：¥8,000.00

-
支付宝：¥2,000.00

每个账户用卡片展示，白色背景+阴影。

5. 我的（Profile）- 设置和个人信息

顶部是用户信息卡片（头像+昵称），下方是设置菜单（分类管理/月度预算/数据导出/记账提醒），最下方是关于 section（关于我们/给个好评）。

第五步：调试和优化（最耗时的部分）

生成完初步设计，我仔细检查了一遍，发现了几个问题。

踩坑记录：

坑1：字体不匹配

AI用了 "Inter / Semi Bold"，但系统里实际是 "Inter / SemiBold"（少了个空格）。

为什么会出现这个问题？

因为AI是根据训练数据"猜"字体名称的，它不知道你本地系统里装了哪些字体，以及精确的样式名称。

解决办法：用 get_available_fonts 工具查询可用字体，然后用 Update 修正。

坑2：分类图标布局错乱

"餐饮🍔"的图标和文字排成了一横排，应该是上下排列才对。

原因：AI创建组件时，默认用了 layout: "horizontal"（水平布局），但分类项应该是垂直的。

解决办法：把每个分类项改成 layout: "vertical" 的Frame。

坑3：SVG环形图显示不出来

我想用SVG画环形图，但直接插入SVG代码不生效。

原因：Ardot不支持直接在文本节点里写SVG，需要用特殊的方式嵌入。

解决办法：用 type: "frame" + svg 属性的方式嵌入。代码示例：

pieSvg = I(parent, {
type: "frame",
svg: "<svg width=\"200\" height=\"200\" viewBox=\"0 0 200 200\">...</svg>",
name: "Pie Chart",
x: 100,
y: 50
})

坑4：颜色格式写错了

AI生成的代码里，把alpha值写在了 color 里面：

// ❌ 错误写法
fills: [{type: "SOLID", color: {r: 0, g: 0, b: 0, a: 0.1}}]

但Ardot的正确格式是：

// ✅ 正确写法
fills: [{type: "SOLID", color: {r: 0, g: 0, b: 0}, opacity: 0.1}]

原因：AI混淆了CSS的 rgba() 格式和Ardot的 fills 属性格式。

解决办法：手动修正，或者让AI重新生成。

坑5：交易记录日期重复了

每条记录都显示了日期，导致页面上出现了一堆重复的日期文本。

原因：AI在创建交易记录列表时，给每条记录都加了个日期文本，但实际上日期应该只显示一次（按日期分组）。

解决办法：删除多余的日期节点（用 Delete 操作）。

坑6：Binding名称过期

每次调用 batch_edit 时，如果复用之前的binding名称（比如多次用 header 这个变量名），会报 "expiredBindings" 警告。

原因：Ardot的binding名称是一次性的，只在当前 batch_edit 调用中有效。下次调用必须用新的binding名称。

解决办法：每次调用 batch_edit 时，用新的变量名（比如 header1, header2, header3...）。

第六步：我让AI自己评价一下

设计做完后，我让WorkBuddy自己看看效果，评价一下。

它的评价还挺中肯的：

做得不错的地方：

-
配色体系统一（绿色主题 + 红色支出/绿色收入）

-
5个页面结构完整，信息层级基本清晰

-
记一笔页面的分类网格布局整洁

-
统计页的环形图 + 排行榜组合实用

-
底部Tab栏一致性保持得好

需要改进的问题：

-
首页那个大绿圆圈是什么鬼？（应该是快捷记账按钮，但看起来像个没加载完的占位符）

-
首页缺少快速操作入口（好的记账App首页通常会有明显的"+"号按钮）

-
图标太简陋（底部Tab栏和设置项用的都是基础emoji或简单图标）

-
缺少数据可视化细节（统计页环形图可以更好看）

-
卡片阴影/圆角不够精致

总结：功能完整度 75分，视觉精致度 60分。作为第一版可用，但如果要达到"好看"的标准，还需要打磨。

最终效果

经过几轮调试，5个页面全部完成：

-
✅ 首页：绿色主题，清晰显示当月收支

-
✅ 记一笔：10个常用分类，红绿配色区分收支

-
✅ 统计：SVG环形图+分类排行

-
✅ 账户：3种账户类型（现金/银行卡/支付宝）

-
✅ 我的：设置菜单+关于页面

如果你想试试

环境配置步骤：

-
下载安装Ardot桌面版（ardot.tencent.com[2]，选对应系统的版本）

-
登录Ardot（微信扫码/手机号/邮箱都行）

-
在Ardot里启用WorkBuddy：点击右上角"MCP 设置" → 找到WorkBuddy → 打开开关

-
在WorkBuddy里信任Ardot：连接器页面找到Ardot MCP → 点击"信任"按钮

-
安装 ardot-design-assistant 技能（技能市场里搜）

-
召唤Ardot设计专家：专家中心 → 搜索"Ardot 设计专家" → 点击召唤

-
保持Ardot运行（不要关，关了MCP就断了）

设计步骤：

-

召唤Ardot设计专家：在WorkBuddy专家中心搜索"Ardot 设计专家"并召唤

-

描述需求：越详细越好。比如：

设计一个记账App，包含：
- 5个页面：首页/记一笔/统计/账户/我的
- 风格：现代简约
- 平台：通用移动端（375×812）
- 配色：主色#2DB87B，支出红#FF3B30，收入绿#2DB87B

-

让AI生成初始设计：专家会调用 batch_edit 工具，一次性创建多个页面和组件。

-

逐项检查并调试：重点检查字体、布局、颜色格式、交互逻辑。

-

导出设计稿：用 export_nodes 工具导出PNG/SVG/PDF格式，或直接生成前端代码。

几个避坑建议

1. 字体名称要精确

AI可能会"发明"一些不存在的字体样式名称（比如把"SemiBold"写成"Semi Bold"）。

建议：每次创建文本节点后，用 get_available_fonts 查询可用字体，然后用 Update 修正。

2. 布局属性名很容易写错

常见的错误对照表：

-
❌ textColor → ✅ fill

-
❌ justifyContent: "center" → ✅ primaryAxisAlignItems: "CENTER"

-
❌ borderRadius → ✅ cornerRadius

建议：把Ardot的属性对照表保存在手边（或者直接让AI查文档）。

3. 每次batch_edit要用新的binding名称

Ardot的binding名称不能复用，否则会报"expiredBindings"警告。

建议：每次调用 batch_edit 时，用新的变量名（比如 header1, header2, header3...）。

4. SVG要用特殊方式嵌入

不要直接在文本节点里写SVG代码，要用 type: "frame" + svg 属性的方式。

5. 颜色格式要注意

alpha值要写在 opacity 字段，不要写在 color 里面。

最后说两句

这次用WorkBuddy的Ardot功能设计记账App，整体体验可以用**"惊喜"**来形容：

-
速度快：从配置环境到5个页面完工，不到2小时（大部分时间花在排查环境问题和调试上）

-
质量还行：配色统一、布局合理、交互逻辑清晰

-
可迭代：发现问题直接跟AI说，它会自动修正

当然也有不足——比如首页那个大绿圆圈（本来想做成快捷记账按钮，结果看起来像个没加载完的占位符）。但这就是AI辅助设计的好处：改起来快。

如果你也想试试，记住一句话：

"描述清楚你的需求，剩下的交给WorkBuddy。"

互动时间 👇
你用过哪些AI设计工具？觉得跟传统设计工具相比怎么样？欢迎在评论区分享你的经验~

这是WorkBuddy 100 种用法第50篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

引用链接

[1]ardot.tencent.com: https://ardot.tencent.com

[2]ardot.tencent.com: https://ardot.tencent.com

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRPvLA5R5DHPwjqdW052ddgqC46xYnI2F9PWymAhdWKRI79W0ibcOJlB2lricVPeFPfa7knMQ7or1SQn80SWWZY9HLVzD7xjT6Qw4/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRMm7D9vcLpV3Xq0U1BSj32iatt8WPVNwoYY9Qq3V20pTMCuUPcjp7P8SIAOC1iaBxwDA3nDM0kk6f9iaiapcTWJdH33aQIZw5wBrgc/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPsN06WBejU8ahBj0brOWVqwK9G12qtqSa06icwdD7BXA6sickeWmv0SDRaytNURAzZB6hX3Wv1qurB3xicUkPjvBrA5AHSSSo6x4/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPynyFCSN3UCh4icqqI78TTuCRjQ1IWyKZm4gKQcZPLB0VvgB4KUaC9t3rhAKlOIGhBs2Ix4tEbO8xl74CBsarPxgkUKpzPtKnk/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPvrqAlAibA3BFuOxcMAhJMhWSiaOU94yb149NIveqmQ6buBZR53u0TZoDBg6iaicRK3pic53L69ePQ2Yic762odjyfcJh5tanS9bGicU/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPnL0rfmAMqYicT4eXEkqv4sLYBP01Wn0kibtw4fQmCHTQIB2fHtHpVE2zF4DA5AP0Avx7Dx0Gxy0semx9xnXqwzwR4W1nib2f2ics/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMomesVkRrDr9YqOrWwUp2ouJrAnNPPHLmsVQtvcvxp3QmQMD9DkcgwvYv1znELbzZJeJZmRJLP1zW0Qfzncnzf2W84N5E4I4A/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPzBTSgJgHzRQMsrYYNLTkY5AwVev4IVUIRSlutaoyA8vgtYibPfYW9kon3u5x4Q49SJRe4A8ibiaH5ISEC6sK9aT2Bnia47zy4kMA/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMXVr7c4u4spU97alsCncMiaickuOpFbw7FicicKZlRDERHfGBGIrmv0WlOAib6dmeqSbiaaaekYtibYqjgbUGD0glnAzIAvaoEsJkrMo/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROb8MTcogEskdG2Wp3MqzSjiauiacjLZyYrWL9xk1OrAicReH969zy1EPBCKXvF41d6zlB0CPZZjelX4RGj0joRmt1zmYrtv8iaKWY/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPLfbIkicIZ7qw8ic3Ml4xwZR2y39icMktCS2BhZf0hFiaaNDlJ9oiadJRBaQiaTU6yRMRW0cjd1ER8PsGVql89gSepk2xP9L1s7j0ib4/640?wx_fmt=png
