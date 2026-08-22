# WorkBuddy 100种用法 #38 | AI 生图能用了，但带水印？WorkBuddy 帮我封装了个 Skill 解决

- 合集序号：38
- 公众号：我与ai的那些事
- 发布日期：2026-05-07
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328782&idx=1&sn=048f60e6c7ebca9461133ca4105a9499&chksm=88303289bf47bb9fa394b87698c4b0709d30f7a734aeef9761b95867eac10960d9bf59663e5e#rd
- 正文字数：4523
- 正文图片：4

## 摘要

WorkBuddy 升级后终于能直接生图了，但图片右下角自带图片由AI生成水印。我让 WorkBuddy 查源码、改参数、封装 Skill——结果它踩了个离谱的 Bug，折腾了两天才搞定。

## 正文

从「生不出图」到「生出来了，但有水印」

WorkBuddy 的老用户可能都知道，之前版本的 WorkBuddy 默认生图功能一直不太好使——要么出不来图，要么得靠第三方 skill 或者外接 API 才能解决。

但最近版本升级之后，我发现：它开始能生图了。

兴奋地点了一下，图片确实出来了，效果也还行。

但紧接着就发现一个问题——

图片右下角，有一个「图片由AI生成」的 水印。

对于公众号封面这种场景来说，有水印的图片基本没法用。发朋友圈无所谓，但正式发布的内容，带别人的 logo，总觉得不太专业。

我跟 WorkBuddy 说了一声：「帮我看看怎么去掉水印。」

第一步：WorkBuddy 顺藤摸瓜，找到水印的根源

既然生图模型是混元的，WorkBuddy 判断底层调的肯定就是混元生图 API。

它直接去翻了 WorkBuddy 的安装目录，/Applications/WorkBuddy.app/ 下面，内置 skill 的源码在 app.asar.unpacked/resources/builtin-skills/ 里。

然后 WorkBuddy 找到了生图相关的脚本 buddy-cloud.py，在里面搜了一下 LogoAdd：

# buddy-cloud.py 第 578 行
def_build_image_body(prompt: str, resolution: str = None,
revise: int = None, seed: int = None) -> dict:
body = {"Prompt": prompt}
if resolution isnotNone:
body["Resolution"] = resolution
if revise isnotNone:
body["Revise"] = revise
if seed isnotNone:
body["Seed"] = seed
return body

WorkBuddy 注意到了：这个函数里根本没有设置 LogoAdd 参数。

没有显式设置，就走 API 的默认值。而混元 API 的默认值是 LogoAdd = 1——也就是默认带水印。

对比一下同一个文件里视频生图的部分：

# buddy-cloud.py 第 567 行
def _build_video_body(prompt: str) -> dict:
return {
...
"LogoAdd": 1, # 视频生图显式设了 1
}

视频那边是显式写的 1，图片这边压根没写。但结果一样——都有水印。

原理清楚了，WorkBuddy 说方案很简单：写一个自己的脚本，把 LogoAdd 设成 0。

第二步：WorkBuddy 把它封装成了一个 Skill

与其每次手动跑脚本，不如直接封装成 WorkBuddy 的 Skill，以后说一句「无水印生图」就能用。

WorkBuddy 按照 WorkBuddy 的 Skill 规范（一个 SKILL.md 描述文件 + 一个 scripts/ 目录放脚本），以 buddy-cloud.py 的认证逻辑（TC3-HMAC-SHA256 签名）作为基础，写了一个 hunyuan_nowm.py，核心改动就是一行：

body = {
"LogoAdd": 0, # 关键：关闭水印
"Prompt": prompt,
"Resolution": "1280:720",
...
}

还加了几个实用功能：

-
自定义分辨率：支持 36 种预设尺寸（公众号封面 1280:720、竖版配图 768:1024 等常用比例）

-
自动下载：生成的图片直接保存到本地

-
Prompt 优化控制：可以开关混元自带的 prompt 重写（--revise 0 精确控制，--revise 1 质量更高）

SKILL.md 里也写清楚了和系统内置生图的对比：

特性

系统内置 ImageGen

无水印 Skill

水印

默认有水印

无水印
（LogoAdd=0）

分辨率

默认 1024:1024

支持 36 种预设尺寸

图片下载

返回 URL

自动下载到本地

Prompt 优化

默认开启

可控（--revise 0/1）

第三步：踩了一个大坑——脚本一直超时

Skill 封装好了，第一次跑——超时了。

第二次——又超时了。

然后又试了好几次，全都超时。一直提示「任务超时（300s）」。

但奇怪的是，通过 API 查询任务状态，显示明明已经完成了——图片都已经生成好了，就是脚本检测不到。

这就很离谱了。

第一天下午WorkBuddy 就卡在这里了。 试了各种方法：

-
换 token → 还超时

-
改轮询间隔 → 还超时

-
关闭 prompt 重写（revise=0）→ 还超时

-
直接用内置的 ImageGen 工具生成 → 图片能出来，但有水印，没意义

折腾了一下午，没找到原因。当时只好先用内置 ImageGen 生了一张带水印的图凑合用，有事出去了，打算第二天继续排查。

（没错，是 WorkBuddy 自己在折腾——我就在旁边看着它试错 😄）

第四步：第二天，WorkBuddy 终于找到 Bug 了

第二天早上，我重新打开WorkBuddy ，让他处理，他换了一个思路：直接打印 API 返回的原始数据，看看实际返回了什么。

打印出来一看，关键数据长这样：

{
"JobStatusCode": "5",
"Status": "DONE"
}

WorkBuddy 注意到了：JobStatusCode 的值是字符串 "5"，不是整数 5。

再看脚本里的判断逻辑：

# 修复前（有 Bug 的版本）
code = result.get("JobStatusCode")
if status == "DONE" or code == 5: # "5" == 5 永远为 False
return result
if status == "FAIL" or code == 4:
raise RuntimeError(...)

Python 里字符串 "5" 和整数 5 是不相等的。

"5" == 5 的结果是 False。所以 code == 5 这个条件永远命中不了。

但 status == "DONE" 不是能命中吗？确实能——如果 API 同时返回了 Status 字段的话。 但实际上，API 有时只返回 JobStatusCode，不返回 Status。这时候两个条件都为 False，程序就继续轮询，一直等到 300 秒超时。

图片早就生成好了，WorkBuddy 的脚本就是「看不见」。

修起来也不复杂，加一个类型转换：

# 修复后
raw_code = result.get("JobStatusCode")
try:
code = int(raw_code) if raw_code isnotNoneelseNone
except (ValueError, TypeError):
code = None
if status == "DONE"or code == 5:
return result
if status == "FAIL"or code == 4:
raise RuntimeError(...)

修完之后再跑——5 秒出图。

从超时 300 秒到 5 秒完成，就差一个 int()。

昨天下午折腾了一下午没找到原因，今天加了一行打印、发现一个类型不匹配，WorkBuddy 就解决了。

有时候排查 Bug 就是这样：最难的不是修，是找到它。

第五步：验证无水印效果

Bug 修完之后，WorkBuddy 赶紧验证了一下。

生成一张公众号封面图：

微信公众号封面图，极简科技风，深蓝到紫色渐变背景，画面中央是一个发光的透明水滴，水滴内部折射出数字代码和光粒子，水滴周围有细微的光晕和光线扩散，干净留白，高端大气，无文字

几秒钟后，图片就下来了——没有水印，干净利落。

对比之前用内置 ImageGen 生成的带水印版本，右下角的 logo 确实没了，画面干净了很多。

第六步：WorkBuddy 一口气生成 5 张不同风格

既然搞定了，干脆让他多生成几张，测试不同风格：

风格

Prompt 关键词

效果

极简科技风

深蓝到紫色渐变，几何线条网格，抽象数字粒子

科技感拉满

水墨中国风

青山绿水，云雾缭绕山峰，留白设计

东方韵味

温暖治愈系

粉色橙色渐变，卡通云朵星星，手绘插画风

温馨甜美

商务精英风

深灰金色渐变，城市天际线剪影，光效粒子

专业沉稳

赛博朋克风

霓虹粉蓝紫撞色，雨夜街道倒影，蒸汽波

视觉冲击力强

5 张图并行提交，总共不到 30 秒全部完成。

这里有个小发现：部分图片上出现了 AI 自动生成的中文文字（比如「温馨时刻」「商务精英」），这不是水印，是混元模型根据 prompt 里的描述词自己加上去的。如果需要纯背景无文字的图，在 prompt 里避免出现主题词就好。

陪 WorkBuddy 踩坑的两天

作为在旁边看着 WorkBuddy 折腾的人类，这两次折腾下来，有几个感受：

① AI 写代码也会犯低级错误

这次的 Bug 说白了就是一个类型不匹配——API 返回字符串，脚本里用整数比。WorkBuddy 写的代码，也会犯这种人类程序员常犯的错误。AI 不是神，代码该 review 还是得 review。

② 但 AI 排查问题的能力确实强

换作人类程序员，可能要花半天才能定位到这个 Bug。WorkBuddy 在第二天换了思路，直接打印原始数据，一眼就看到了问题。AI 的优势不是不犯错，而是犯错后能快速迭代。

③ 让 AI 自己封装自己的工具，体验很奇妙

这次是让 WorkBuddy 去改造 WorkBuddy 本身的生图功能。相当于「AI 给自己做插件」。整个过程下来，感觉 AI 工具的可塑性比想象中强得多——不只是「用工具」，而是「改工具」。

④ 人类的价值在哪？

我觉得是判断方向。WorkBuddy 负责试错、写代码、调 Bug，但我得判断「这个目标值不值得做」「这个方向对不对」。分工明确，效率最高。

完整时间线

Day 1
├── 我发现 WorkBuddy 默认生图带水印
├── 让 WorkBuddy 去翻源码
├── WorkBuddy 找到 LogoAdd 参数（未设置 = 默认 1）
├── WorkBuddy 封装 hunyuan-no-watermark Skill（LogoAdd=0）
├── 跑脚本 → 超时
├── WorkBuddy 反复测试 → 全部超时
└── 暂时搁置，用内置 ImageGen 凑合

Day 2
├── WorkBuddy 打印 API 原始返回值
├── 发现 JobStatusCode 是字符串 "5" 而非整数 5
├── WorkBuddy 加 int() 类型转换
├── 5 秒出图，无水印 ✓
├── WorkBuddy 批量测试 5 种风格，30 秒完成 ✓
└── 搞定！

写在最后

这件事给我的感触挺深的。

WorkBuddy 升级后能生图了，这是好事。但默认带水印这个设定，对需要公开发布内容的用户来说是个硬伤。

好在工作Buddy 是开放的——源码可以看、Skill 可以自己写、参数可以自己调。这不是每个 AI 工具都能做到的。

整个折腾过程，其实是「我和 AI 协作」的一个缩影：

-
我提出问题（生图带水印，能不能解决？）

-
WorkBuddy 去执行（翻源码、写脚本、封装 Skill）

-
遇到 Bug，WorkBuddy 自己排查（打印原始数据、发现类型不匹配）

-
修完验证，交付成品

AI 能帮你写代码、调参数、生成图片，但问题得你来提，方向得你来定。

这才是「AI 协作」的正确打开方式。

这是《WorkBuddy 100 种用法》系列的第 38 篇，我每天都会更新一篇，记录 WorkBuddy 的各种真实使用场景。

从自动化办公、内容创作，到法律咨询、数据分析、AI 生图……100 种玩法，我和 WorkBuddy 一起帮你一一踩坑。

关注公众号，不错过每日更新。

你平时用 AI 生图遇到过什么坑？欢迎留言交流，说不定下一篇就是 WorkBuddy 帮你解决的那个问题。

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPbGPvF1NHnpey4JcATdIDwnpfr1XMIKsia9IzTnyzH4zxTvMGIBPVR7iaqCOVrgr9ibhZ6zWno5uwicibiaXPQNnrzBfkqnrzuSibKPI/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMVwUiatgxvNiaZa7NNKuXfXWArMIic0FFQg3HNkXrpn5Vq6IIDpFZ6GVucgS2CZyvO2LicYiclYJChv96pxWTOaC5zpvQvqCjtwUV8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO8KZAY13kflKGicHNRJw5DehOy0yGVGT0p59kFdwd0EkqMKZLuG6oDMoczUbC1DDsuGC9u7JH68lyaAYFeefUzrL3AbW1SgGys/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM93X83SXwWAyZiadJppaGbwiaypw1d9q5Sic1MWO35OrIrDmMmfDOJOhYsUE47t1sic7vNfHHw7joeAsgnhmZcYhTiaynAEC0XEof4/640?wx_fmt=png&from=appmsg
