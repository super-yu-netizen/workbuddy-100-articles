# WorkBuddy 100种用法 #84 | 我用HTML写了一支30秒竖屏视频，配音还是AI

- 合集序号：84
- 公众号：我与ai的那些事
- 发布日期：2026-06-23
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329894&idx=1&sn=a363a03f93363840a7c222d216b2e031&chksm=88303661bf47bf77287bb219ac140594cae9c22e63ce8e7bd073df95c25d53132115c12b24aa#rd
- 正文字数：2513
- 正文图片：5

## 摘要

不会剪辑也能出片。WorkBuddy 发现 HyperFrames，直接用 HTML 写视频，AI 生成配音，横屏转竖屏一气呵成。中间翻车三次，但每次都能自己修回来。30 秒竖屏视频，全程零手动。

## 正文

一直在写公众号。昨天写完那篇WorkBuddy 100种用法 #83 | 我给公众号绑了个AI客服，零代码之后，我就在想——要是能给每篇文章都配一支短视频发视频号，那该多好。

但问题是：我不会剪视频。

不是矫情，是真的不会。打开剪映我就头皮发麻，时间轴、关键帧、转场特效，光看着就想关掉。今天发现了个HyperFrames，于是我就问了 WorkBuddy。

HyperFrames ，你知道这个吗？

HyperFrames 是什么

一句话：写 HTML，渲染成视频。

HeyGen 出的开源项目，Apache 2.0。核心思路很简单——你用 HTML+CSS 做画面，用 GSAP（一个动画库）驱动时间线，然后它的 CLI 用 headless Chrome 逐帧截图，FFmpeg 合成，输出 MP4。

最妙的是，它专为 AI Agent 设计。Claude Code、Cursor、Codex 都能直接用。

也就是说，你不需要会剪视频，你会写网页就行——甚至你不需要会写网页，你会跟 AI 说话就行。

开搞：30秒视频，主题就是上期文章

我让 WorkBuddy 基于 #83 的文章内容，生成一支 30 秒的视频。

它先检查了我的环境：Bun 已装、FFmpeg 已装，只差 HyperFrames CLI。装完就开始写 composition。

HyperFrames 的 composition 就是一个 HTML 文件，里面有 5 个场景：

-
0-5s：Hook 开场「给你的公众号装一个AI客服」

-
5-11s：痛点共鸣「关键词回复太蠢」

-
11-17s：三步解决方案

-
17-24s：四步操作详解

-
24-30s：CTA + 关注引导

每个场景是一个 <div class="scene">，用 GSAP 驱动进出动画。WorkBuddy 一口气把整份 HTML 写出来了，色彩方案、字体大小、动画节奏都帮我定好了。

跑 hyperframes render，一分钟不到，1920×1080 的横屏视频出来了，30fps，H.264 编码。

翻车第一次：配音听不懂

点开一看——画面没问题，但配音是英文乱码。

HyperFrames 自带 TTS 功能，用的是 Kokoro 模型。但这个模型只支持英文，让一个英文 TTS 读中文，效果约等于把中文词用英文发音规则硬念出来。

WorkBuddy 立刻切换方案：用 edge-tts（微软语音服务），选「晓晓」女声，语速调到 1.15x。这次出来的配音标准得一批，清晰流畅，29.7 秒，完美匹配 30 秒视频。

翻车第二次：竖屏才是刚需

横屏视频看着还行，但我需要的是竖屏——视频号、抖音都是 9:16。

第一次偷懒，直接用 ffmpeg 加黑边，把 1920×1080 的画面塞进 1080×1920 画布里。结果你猜怎么着——画面只有 1070×607 大，上下各 650 多像素的黑边，在手机上看跟看邮票一样。

不行，得重写 composition，针对竖屏重新设计布局。

WorkBuddy 把整份 HTML 重写了：

-
画布改成 1080×1920

-
文字全部加大：标题 118px，正文 46-48px

-
布局从左右流改成上下流

-
每个场景都加了渐变背景和氛围光

翻车第三次：HyperFrames 的特殊语法

渲染又挂了。

报错信息说：「No GSAP timeline registered」和「Root composition missing data-composition-id」。

原来 HyperFrames 有它自己的一套规则：

-
根元素必须有 data-composition-id="root"、data-width、data-height、data-duration

-
每个场景需要 data-start 和 data-duration

-
GSAP 时间线必须注册到 window.__timelines["root"]

这些如果自己从头写，肯定踩坑。但有 WorkBuddy 在，它看到报错直接就把结构修对了。

第三次渲染，跑通。30 秒，1080×1920，3.3MB。

再用 ffmpeg 把 edge-tts 生成的配音合进去——

完美。

整个流程复盘

从「想做个视频」到「做完可以发」，经历了：

-
安装 HyperFrames → 检查环境 → 一次完成

-
写 HTML composition → WorkBuddy 一把梭

-
渲染 → 跑通但没声

-
换 TTS → Kokoro 翻车 → edge-tts 救场

-
竖屏需求 → 先加黑边（丑）→ 重写竖屏版

-
HyperFrames 语法适配 → 修三次结构 → 跑通

-
合成音轨 → ffmpeg 一条命令

全部在 WorkBuddy 里完成。我没碰过剪映，没调过时间轴，就一直在聊天框里说「能不能生成竖屏」「配音换中文」「黑边太大重新渲染」。

这玩意能干什么

除了给我这种懒人做视频号物料，HyperFrames 还能做很多事：

-
产品发布视频：写个 HTML 页面，配上动画，直接出片

-
数据看板录屏：把图表做成 HTML，加上录屏旁白

-
教程演示：逐屏讲解，每屏一个知识点

-
社交媒体短视频：文字动画、卡片切换，全在 HTML 里

而且因为是 HTML，你可以用任何前端能力——CSS 渐变、SVG 图标、Three.js 3D 场景——全部渲染进视频。

一点心得

这次用下来，最大的感受是：AI Agent + HyperFrames 这套组合，让视频创作的门槛从「会用剪辑软件」变成了「会说话就行」。

你不需要学 Timeline、Keyframe、Composite——你只需要描述你想表达什么，AI 帮你写 HTML，HyperFrames 帮你渲染成片。

还有一些坑要注意：

-
HyperFrames 对 composition 结构要求严格，data-composition-id 和 window.__timelines 一个不能少

-
Kokoro TTS 不支持中文，老老实实用 edge-tts 或 Azure 语音

-
竖屏和横屏的排版完全不一样，别偷懒加黑边，直接重写

-
渲染可能遇到字体映射问题，优先用 HyperFrames 支持的字体（inter、roboto 这些）

这是WorkBuddy 100种用法第84篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI视频生成 #HyperFrames #公众号 #视频号 #AI工具 #TTS #HeyGen #HTML视频 #竖屏视频

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMzQbnFT63TWdrtBaEasAbN90FlWRtuN7qC0Bib2NYlyujAfh58u0vmQozuoeuicA1B3NW7LFjEh1IhDHxBmnWX3BUmibxvUUEJK8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNTvLtcevdkicZwRFbMG7KzDvyIK6ZibUE4X9aOPNNQAibiataSQ0WG9Q8ENYc1IKK7w2LQ3oL2T68EEbbmSMBMfEf8jVH1wFibrFDE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNx9NZfibVWzCYQVXkm0Y3pBNxkg2EZLXCk4SURhylkibK210lW2ic3Lm3QnjiaiaecicWHysazRGibWxc7VhmUfd4HKWxiaDunoUvVgicQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNY8BXtcHJMYbjziaunTM0THhBHCqjAXBUTnUBpcPyCmaBWzkXrFG41ickCbY8KicP8zzavr3BTsA3DqcHH5uiar6riaUx4cKXKgaEk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMzNXCR7ziaKiak7DyPEaZqXCJzMxJ28BjptWLWzNVRF3wpicUtRDweibAs3sC6Ar0x9C82hdFhKohLonftHqEdrySTxOcmVerMPrY/640?wx_fmt=png&from=appmsg
