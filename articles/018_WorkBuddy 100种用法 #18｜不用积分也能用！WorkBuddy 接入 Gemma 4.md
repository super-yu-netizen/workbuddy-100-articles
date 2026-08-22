# WorkBuddy 100种用法 #18｜不用积分也能用！WorkBuddy 接入 Gemma 4

- 合集序号：18
- 公众号：我与ai的那些事
- 发布日期：2026-04-18
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328279&idx=1&sn=357d409e4069f02e5a381576835f3fbc&chksm=88303090bf47b986cb9c5fe9a37e09e880f5cdb537651520d3a8b53fd82bdb2101975501d461#rd
- 正文字数：2131
- 正文图片：7

## 摘要

WorkBuddy内置模型需要消耗积分，长期使用有成本。本文教你用Ollama本地运行Gemma 4，接入WorkBuddy完全免费、不扣积分、隐私更安全。

## 正文

用过 WorkBuddy 的朋友都知道，它的内置模型调用是要消耗积分的，要花钱。免费额度用完、签到不够用，高频办公很快就见底，长期用也是一笔开销。

上周 Google 悄悄发布了 Gemma 4，开源、免费商用，最小的 2B 版本手机都能跑，最大的 27B 版本性能已经接近主流付费模型。
很多人看到这个消息的第一反应是：听起来不错，但怎么用？

今天这篇就完整走一遍流程——从安装 Ollama、下载 Gemma 4，到在 WorkBuddy 里接入自定义模型，全程不花一分钱，不扣WorkBuddy 积分。

Gemma 4 是 Google DeepMind 在 2026 年 3 月底发布的开源模型，基于 Gemini 3 技术架构。
它有几个非常突出的优势：

-
• 支持 256K 超长上下文，长文档、PDF 一次性处理

-
• 采用 MoE 混合专家架构，27B 版本推理时只激活约 4B 参数，速度更快

-
• Apache 2.0 开源协议，个人使用、商业使用都无限制

-
• 提供 4 种规格：2B、4B、26B、31B，覆盖手机到高性能电脑

第一步：安装 Ollama

Ollama 是目前本地运行大模型最简单、最稳定的工具，支持 Mac、Windows、Linux 全平台。

Mac 安装方式

打开终端，执行安装命令。

brew install ollama

如果没有安装 Homebrew，需要先安装，再执行命令。
也可以直接去 Ollama 官网下载安装包，拖入应用文件夹即可。

安装完成后，在终端输入版本查看命令，验证是否安装成功。

ollama --version

Windows 安装方式

-
1. 打开 Ollama 官网下载 Windows 版本

-
2. 双击安装，系统会自动配置环境

-
3. 打开 PowerShell，执行版本查看命令验证

Linux 安装方式

在终端执行官方一键安装脚本即可。

curl -fsSL https://ollama.com/install.sh | sh

第二步：下载 Gemma 4 模型

根据你的电脑内存选择最合适的模型版本：

-
• 8GB 以下内存：建议使用 2B 版本

-
• 16GB 内存：推荐 4B 版本，速度与效果最均衡

-
• 32GB 及以上：可运行 27B 版本，效果接近付费顶级模型

下载并运行 2B 版本：

ollama run gemma3:e2b

在终端输入运行命令，首次使用会自动下载模型文件（约 7.2GB）。
下载完成后自动进入对话界面，能正常回复即代表运行成功。

输入退出命令即可回到正常终端界面。

第三步：启动 Ollama 服务

Ollama 会在本地启动一个 API 服务，供 WorkBuddy 调用。
默认服务地址：http://localhost:11434

在终端输入服务启动命令。

ollama serve

启动成功后，不要关闭这个终端窗口，保持后台运行。

打开浏览器访问上述地址，显示“Ollama is running”即正常。

第四步：在 WorkBuddy 配置自定义模型

Ollama 正常运行后，就可以接入 WorkBuddy 了。
重点：接入后走本地模型，不扣 WorkBuddy 积分！

第一步：进入设置

打开 WorkBuddy，点击左下角设置图标，进入设置页面，找到「自定义模型」入口。

第二步：添加模型并填写信息

点击添加模型，按以下内容填写：

-
• 模型类型：选择 OpenAI 兼容

-
• 模型名称：可自定义，例如 Gemma4:e2b（2B）

-
• API 地址：http://localhost:11434/v1（必须带 /v1）

-
• API Key：任意填写，本地模型不校验，我这里写ollama

-
• 模型 ID：gemma4:e2b（必须与下载的模型名称一致）

第三步：切换模型并使用

在 WorkBuddy 主界面的模型下拉列表中，选择刚刚添加的 Gemma 4。
发送一条测试消息，能正常回复即配置成功。

实际体验

2B 版本日常使用完全足够：

-
• 日常问答、文案写作、代码生成都很流畅

-
• 本地运行无网络延迟，速度比云端 API 更快

-
• 256K 上下文可一次性处理几十页 PDF

-
• 中文理解正常，偶尔略生硬，但办公完全够用

-
• 完全免费、无 Token 限制、不扣 WorkBuddy 积分

适合哪些场景

-
• 不想消耗积分、长期想免费使用 WorkBuddy

-
• 处理隐私数据，不想上传到云端

-
• 电脑配置 16GB 以上，想体验本地 AI

-
• 追求安全、私密、稳定的工作流

局限性：
综合能力仍略逊于 GPT-4o、Claude 等顶级付费模型。

常见问题（避坑必看）

-
1. WorkBuddy 连接失败：检查 Ollama 服务是否启动、API 地址是否带 /v1、模型 ID 是否一致

-
2. 模型运行卡顿：关闭后台程序，内存不足可换 2B 版本

-
3. 下载速度慢：可更换国内镜像源

-
4. 端口被占用：关闭占用 11434 端口的程序再重启

这是「WorkBuddy 100种用法」系列第 18 篇，全部都是真实可复刻的操作实战。
关注我，持续更新剩下 82 种用法，每天学一个新的 AI 办公技能。

#WorkBuddy #WorkBuddy100种用法 #Gemma4 #Ollama #本地大模型 #开源AI #自定义模型 #免费AI #省积分 #隐私AI

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

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPa2RshnUibibPE2w2Mml4msibicntbwoLr68zgYa6yeQuoGMoLs3UPzwctUkq8iakcfaWetYcjEoZ7yPAB8p8aCzOFWaia6B3Tnn7F4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPFqAbece9YiagFu2zYmxzMvSb8BSbRtrVf7v7Xn79h6r3wLgITzjdjtUIeSfAaoaovJbbge9uWuibBfzk8BxA0wCDlVzaEiam8ME/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROncMrxw06KpMXibAiacOxVSrmykicmYpxgjDu3hwnRe34Sj1ThMK9LEmdDCV8u53yLLviaXx5QHx9To1oI7bTTlxI61AGlibdfe0Eo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPIBibEEaSIQDSccJ4Wpib05Ot7Nw1vfrEyQickegxw67knw5YFCshJgCIoNYMpzPbmWmCW6oHCteic1vhHVfLz4QjEc4hWJNe8HBU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNJdPUtbX2Xl3vqZRsWv7WfOickyqYRpUk3CdtpedX4ehWfgZGDPvTxn82aH46c8ldlNK8lLXVza5KhDOYhNZbjDpz26BkprrWE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPjP952RibNibeOrd9BrKzHTwicYHTRQtcymzrWh764Yl0ZQjunClCR4iaPkIXmbgVptgEmOzuSucic1DZCIEY8kweEXm5qecaIgSVk/640?wx_fmt=png&from=appmsg
- http://mmbiz.qpic.cn/sz_mmbiz_png/JvRAOtGGLJtAxia0Gjbls2as6IvpOJj4ovOaYKdNic2PcAj0u875xVN8h1Kk5AlQ23PgDTAjqMI7xPXDPPd0D0yQ/0?wx_fmt=png
