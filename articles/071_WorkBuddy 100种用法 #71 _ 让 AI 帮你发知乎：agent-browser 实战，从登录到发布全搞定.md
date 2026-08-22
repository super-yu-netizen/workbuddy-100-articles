# WorkBuddy 100种用法 #71 | 让 AI 帮你发知乎：agent-browser 实战，从登录到发布全搞定

- 合集序号：71
- 公众号：我与ai的那些事
- 发布日期：2026-06-10
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329454&idx=1&sn=43a7f44641f68f5ca20e17fe9b844d8a&chksm=88303429bf47bd3f2588ac667b579297b81716f294c2325bd6100d23301a62e485f098c4ed1b#rd
- 正文字数：3125
- 正文图片：5

## 摘要

想让AI帮你发知乎？用WorkBuddy的agent-browser技能，从打开浏览器、登录知乎、填写内容到点击发布，全程自动化。踩了Draft.js编辑器的坑，最终成功发布第10篇想法。

## 正文

最近我一直想搞定一件事：让 AI 帮我把内容同步发到知乎。

不是复制粘贴那种——是真正让 AI 打开浏览器，登录，找到编辑器，把内容填进去，然后点发布。全程不需要我动手。

这期讲的就是这个尝试。结果？成了，中间的坑全是 WorkBuddy 自己踩、自己填的——我只管说了一句「帮我发这篇」。

为什么要搞这个？

很简单。写公众号的同时想运营知乎。每篇内容手动复制粘贴、调整格式、点发布……累，而且没必要。

AI 现在能操作浏览器了。WorkBuddy 里有 agent-browser 这个技能，底层是 Playwright，能真正打开 Chromium，点击、输入、截图，跟人操作一模一样。

所以我想试试：能不能只告诉 WorkBuddy 「帮我把这篇发到知乎」，剩下的它全搞定？

第一步：打开知乎，等你扫码

我先跟 WorkBuddy 说：「帮我把这篇文章发到知乎想法上」。

WorkBuddy 加载 agent-browser 技能后，自动执行：

agent-browser open https://www.zhihu.com
agent-browser wait --load networkidle

浏览器弹出来了，知乎首页正常显示。但登录态没保持——需要扫码。

这里有个细节：扫码必须人来操作，AI 扫不了二维码（也没有微信）。所以 WorkBuddy 自己判断出需要登录，停下来告诉我「登好了告诉我」，我扫完码回一句「登好了」，它立刻继续往下跑。

整个过程我没给它任何指令——判断何时暂停、何时恢复，全靠 WorkBuddy 自己。

第二步：找到「发想法」的入口

登录之后，页面上有一排按钮。WorkBuddy 用 snapshot -i 自动把页面上所有可交互元素列出来，每个元素带一个 [ref=exx] 编号：

button "创作" [ref=e13]
...
button "发想法" [ref=e24]

它自己找到了「发想法」按钮，用 click 去点：

agent-browser click "[ref=e24]"

第一个坑来了——click 超时了：

✗ Action on "[ref=e24]" timed out.
The element may be blocked, still loading, or not interactable.

这时候有意思的地方来了：我没有介入。WorkBuddy 自己分析错误原因（按钮被动画遮罩导致不可交互），自己想出替代方案——不用 click，改用 JS 直接找按钮调用 .click()：

[...document.querySelectorAll("button")]
.find(b => b.textContent.includes("发想法"))?.click()

一行 eval，自己解决了。我没有写这行代码，没有教它怎么做，它自己诊断、自己修、自己继续。

第三步：往编辑器里填内容——最大的坑

想法编辑器打开了。但往里填内容，才是整个过程中最棘手的部分。

知乎用的编辑器是 Draft.js（Facebook 的富文本框架）。这个框架有个特点：不能直接改 innerHTML，也不能通过 execCommand("insertText") 正确保留多段换行。

WorkBuddy 第一轮尝试：把带 \n\n 换行的完整文章内容用 insertText 填进去。结果——内容确实填进去了，但所有换行全被吞掉，只剩最后一段文字（393 字的内容只剩 47 字）。

WorkBuddy 自己发现了这个问题（通过截图对比发现文字不完整），自己分析了原因（Draft.js 的 insertText 会消费 \n\n），自己调整了方案：去掉所有 \n\n 换行符，将全文作为连续纯文本整体插入。

第二轮尝试，381 字完整写入，一字不差。

这一来一回，从失败到成功，我全程没说话。WorkBuddy 自己截图验证、自己发现问题、自己查文档/推理原因、自己改策略重试。

第四步：激活「发布」按钮

内容填完，「发布」按钮还是灰的（disabled）。

又是 Draft.js 的坑——DOM 虽然被改了，但 React 内部的 editorState 没更新，所以发布按钮认为「内容为空」，继续保持禁用状态。

WorkBuddy 自己想到了触发机制：往编辑器里插入一个字符再删掉，强制 React 重新计算 editorState：

document.execCommand("insertText", false, " ");
document.execCommand("delete", false);

一插一删，「发布」按钮亮了。这个技巧不是我在文档里看到的，是 WorkBuddy 在 zhihu-post 技能文档里读到、自己判断该用在这里、自己执行的。

第五步：点发布，收工

按钮亮了。WorkBuddy 再次用 agent-browser click 点发布——又超时了。

同样的动画遮罩问题。WorkBuddy 不需要我再提醒什么，直接复用之前成功的方案，JS eval 点按钮：

[...document.querySelectorAll('button')]
.find(b => b.textContent.trim() === '发布')?.click()

点下去，知乎弹出「发布成功」确认窗口。第 10 篇想法，发出去了 ✅

全程回顾：我只说了两句话

回过头来看整个流程，我跟 WorkBuddy 的对话大概是这样的：

我说的

WorkBuddy 做的

「帮我把这篇发到知乎想法」

打开浏览器、加载技能、打开知乎首页

（等扫码）

判断需登录 → 暂停等我

「登好了」

找按钮、点开编辑器、填内容……

（沉默）

遇到超时 → 自己切换 JS 方案

（沉默）

遇到换行丢失 → 自己诊断、去掉换行重试

（沉默）

发布按钮灰色 → 自己 insert+delete 触发

（沉默）

发布超时 → 自己 eval 点击

（沉默）

截图确认 → 关闭浏览器

从头到尾我就说了三句话。剩下几十个步骤，全是 WorkBuddy 自己完成的——包括遇到四个坑、四次自己解决。

踩过的坑一览

第几坑

问题

WorkBuddy 怎么解决的

①

click
发想法按钮超时

自动切换为 JS eval .click()

②

Draft.js 吞掉 \n\n 换行

自动去掉换行，改为连续纯文本

③

发布按钮因 React 状态未更新而 disabled

自动 insert+delete 触发 state 重算

④

click
发布按钮也超时

自动复用 JS eval 方案

这些坑有一个共同特点：文档里不会提前告诉你，只有真刀真枪跑一遍才会遇到。而 WorkBuddy 的价值就在这里——遇到问题不需要你去查 Stack Overflow、去试错，它自己会排查、自己会修、自己会继续。

agent-browser 还能干啥？

发知乎想法只是冰山一角。agent-browser 能做的远不止这个：

-
定时发布内容：配合自动化调度，每天固定时间自动发文

-
多平台同步：公众号发了，自动同步到知乎、小红书、微博

-
评论/互动管理：自动查看新评论、回复常见问题

-
数据采集：抓竞品数据、热点话题、行业动态

关键是——一切都在真实浏览器里发生，不需要平台开放 API。没有权限限制，没有 rate limit，跟真人操作一模一样。

你也试试？

如果你也想让 WorkBuddy 帮你在知乎发内容，只需要：

-
告诉 WorkBuddy：「帮我把这段内容发到知乎想法」

-
它会打开浏览器，等你扫码登录

-
登完说一句「好了」

-
剩下的事你别管了

不用写代码，不用懂 Playwright，不用担心前端框架的坑。那些坑，WorkBuddy 已经替你踩过一遍了。

这是WorkBuddy 100种用法第71篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #知乎自动化 #浏览器自动化 #agentbrowser #AI工具 #内容运营 #知乎想法 #Playwright #Draftjs踩坑 #自动化发布

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROdmRcsJQ4khxXfJL282Uf8Zcpv3GHdh6SFk2K63UOH9nggsPscfhvicqEyFU1E3FnVMEia71Vnewz0RlDS5LuGXpOngXHuAhQV0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROib35GbmpbZogFVISwDV1qoskRC2xEOv2lFEib7S3L6vqLYeCpLkr59uCJC07c3TbuLKFNDQVNNXPTQ2B7muRiaCcy1AWPM3ibJHw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM8nLOP2Jl8Htw8Caj1lZAtrgn5fUwiahv6hTJDXfXy4VjUQVF7gFHn65IN4Hakx2wy3tBkn6CEYj24Hsac8SR2nY1BRfTQNdc8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNxVRrrMOtO9gN4kT1HWrwu1KxEDjrWXEd1sjVLsDecAvI1gJxPA6B1489lbQIbUwibiciaIHlZHo8d1ZnqibLYLiaJbSy6WUG3yW7I/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPha4EhlS0stkibibolpw9yshibDaJyHvyibqYjPzOcUXrbCr45iabHEXtQMbuiaicvjiaPKplAf2iaTKV4dC0XZZeCic8Nic7ZVibjmSQFWpc/640?wx_fmt=png&from=appmsg
