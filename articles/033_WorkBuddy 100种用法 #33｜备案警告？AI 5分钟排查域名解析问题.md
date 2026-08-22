# WorkBuddy 100种用法 #33｜备案警告？AI 5分钟排查域名解析问题

- 合集序号：33
- 公众号：我与ai的那些事
- 发布日期：2026-05-02
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328649&idx=1&sn=7a642dcfab72bfa814281d2cc3873ce9&chksm=8830310ebf47b8189e2e545856de5214263df0f5269920affac84586687bd95ba601bd01aba9#rd
- 正文字数：1883
- 正文图片：6

## 摘要

收到火山引擎备案警告短信，ping域名发现解析到海外IP。用WorkBuddy分析Cloudflare配置，5分钟修复DNS解析问题。

## 正文

昨天傍晚，手机看到一条火山引擎的短信提醒——备案信息存在不合格情况，要求及时整改。短信里没说具体哪里不合格，只让去查邮件和站内信。我心想是不是域名解析出了问题，随手 ping 了一下域名，果然——解析结果指向了一个海外 IP，完全没打到火山云的服务器上。

📱 一条引发恐慌的短信

【火山引擎】经核查，您在火山引擎已备案完成的信息，账号：2108068103，主体：XXX，存在不合格情况，请您及时完成整改。核查详情，请查看邮件和站内信。

这下有点慌了。明明在 Cloudflare 配了 A 记录指向火山云服务器 IP，怎么 ping 出来是国外地址？

第一步：ping 发现异常

打开终端，先 ping 一下自己的域名：

⚠️ 异常：IP 指向海外172.67.x.x 是 Cloudflare 的美国边缘节点 IP，不是我的火山云服务器 115.xx.xx.xx。国内用户访问时绕道美国，速度极慢，且触发备案核查。

第二步：截图发给 WorkBuddy 分析

把 Cloudflare DNS 后台截图直接扔给 WorkBuddy，问：

我： 这是我域名的 DNS 解析配置，帮我分析下，我有一台服务器，为什么没解析到服务器，解析到国外了？

WorkBuddy： 一句话结论：你的服务器没问题，是 Cloudflare 的 Proxied（代理）模式在"截流"，所以看起来解析到了国外。

你的三条 A 记录（admin、marathon、yaniw.com）都指向了 115.xx.xx.xx，但全部开启了 Proxied（橙色云朵图标）。

Proxied 模式的机制是：DNS 查询不返回你的真实 IP，而是返回 Cloudflare 的边缘节点 IP（这些节点在海外），用户的请求先打到 Cloudflare，再由 Cloudflare 反向代理回源到你的服务器。

💡 核心知识点：Proxied 模式到底做了什么？

理解这个问题的关键，是搞清楚 Cloudflare 的两种代理模式：

模式

DNS 返回的 IP

流量路径

适合场景

🟠 Proxied

Cloudflare 边缘 IP

用户 → CF节点 → 服务器

国际访问加速、隐藏真实IP

⚫ DNS only

你的真实服务器 IP

用户 → 服务器（直连）

国内服务器、需要直连的场景

💡 关键洞察 Cloudflare Proxied 模式本质是一个反向代理：真实 IP 被隐藏，用户看到的永远是 CF 的 IP。

对于国内服务器 + 国内用户的场景，这反而是负优化——流量绕道美国再回来，延迟倍增，还会触发 ICP 备案核查。

🔧 三步修复，5 分钟搞定

1. 登录 Cloudflare DNS 管理后台 进入 yaniw.com 的 DNS 记录列表，找到所有 A 记录。

2. 将 A 记录的 Proxy 状态从 Proxied 改为 DNS only 点击每条记录右侧 Edit，把橙色云朵图标切换为灰色（DNS only），保存。重点修改 yaniw.com 主域名记录。

3. 等待 DNS 传播，重新 ping 验证 Cloudflare DNS 更新通常在几分钟内生效。再次 ping 域名，确认返回的是 115.xx.xx.xx。

修改前后对比截图（橙色云朵 → 灰色云朵，以及修改后 ping 结果）

✅ 修复结果：改为 DNS only 后，ping yaniw.com 直接返回 115.xx.xx.xx，国内访问延迟从 140ms+ 降至 20ms 以内。同时向火山云提交备案复核，问题解除。

🤔 什么时候该用 Proxied？什么时候不该用？

WorkBuddy 同时给出了决策建议，整理如下：

🟠 适合开启 Proxied 的情况：

-
服务器在海外，希望用 CF 的 CDN 节点加速国内访问

-
需要隐藏真实服务器 IP，防止 DDoS 攻击

-
使用 Cloudflare Workers / Pages 部署的服务

⚫ 应该关闭 Proxied（使用 DNS only）的情况：

-
服务器在国内，有 ICP 备案需求

-
需要通过 IP 直连访问的服务（如 SSH、游戏服务器）

-
已有国内 CDN 加速，不需要 CF 代理层

AI 的价值不是替你操作，而是帮你快速理解「为什么」——5 分钟就搞懂了一个困扰了我一下午的问题。

WorkBuddy 100用法 · 连载中

💬 你在用 AI 处理过什么「意外」技术问题？

这是 WorkBuddy 100用法 系列的第 33 篇。从备案警告到修复完成，全程不到 10 分钟——AI 充当的是那个帮你快速理清思路的搭子，而不是替你打键盘的工具。

你遇到过类似的「DNS / 服务器 / 域名」折腾经历吗？在评论区告诉我 👇

-
📡 DNS 配错过

-
🔒 SSL 证书报错

-
🌐 备案被警告过

-
😅 都没遇到过

关注我，每天分享一个 WorkBuddy 真实使用场景。

#域名解析 #Cloudflare #DNS配置 #ICP备案 #WorkBuddy100用法 #AI效率工具 #网站运维 #服务器部署 #火山引擎 #技术排障

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROkE1RPGoNica4JvA4PfYSsjQO6rukXEuqwqkOib4Ux7AXNemNV1S1VOMOh5BCVZibFJMhdP3gwUmzRU9MQGicJ8RpE83fSicER2HPM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNBYsEt628uvqUvgll7VEdtJAXb3cfj9x1l3ibYy3ibdWwKyGURqppKQdibiaKmRUsexSHGRnHppwwhZ5nCpAQMXPGUjY5ZviakL9bw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMoibC7kYDZUkr0ib7TxT8UkyU64uEB5J1Y5II1TPBU62U1MOkpV5Xibc8jVwganN8nooJy6NXf7fGVictbnXwTfib7dhJL0du2eVLc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRONuuIc5AKn3ACYo97kHwicnibL5miaCMyLlyr88ydzHCXPN0dTD4ovDG5ePtqeJltIyzjib3RtX4zYlejxCxFa7j7KcvL58icPgiaSU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNdO9tdu1YC6CZTfJMsFibZGhKSNVftwsXhOFxvIx6vobJMgR6czMT1F6t7mgbQSgqJ41DnNAkiaibTbGN1icrcjicRHg9auWbZdm9k/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROJA30YIA0pw0FEI68U5howP7e0nyagdAsKk5812vgg38PDzIvBH97ZX9BMTVEDm4rpCjnXFw9n4RMtZxtYuNbUHqDZxBwiaAeQ/640?wx_fmt=png&from=appmsg
