# WorkBuddy 100种用法 #44 | 从没人像到带声音，我用WorkBuddy折腾出了30秒脱口秀视频

- 合集序号：44
- 公众号：我与ai的那些事
- 发布日期：2026-05-14
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328936&idx=1&sn=54a8ee78cd2ecbceb59eda47392b1d54&chksm=8830322fbf47bb39d47a7aaeb402a084280e2fc9a4fff1b8da4c06ced295acb7e58dde55075c#rd
- 正文字数：3182
- 正文图片：15

## 摘要

用 WorkBuddy 折腾了半天，终于用多分镜拼接搞出了一段30秒的脱口秀视频，还自带环境音。最搞笑的是 AI 一开始说混元不支持声音，追了一句\x26quot;你从哪看的\x26quot;才查出来——加个参数就行。

## 正文

这篇WorkBuddy 100种用法 #41 | 使用视频生成专家做脱口秀视频，结果翻车了3次写了用 WorkBuddy 的视频制作专家生成脱口秀视频的事。

当时生成完一看——没有人像。

画面里只有舞台灯光、观众席的模糊轮廓，就是没有演员本人。

我之前用视频制作专家生成过其他视频，效果还不错，所以第一反应是：可能这个场景不太适合，换一个方式试试。

然后我就去问 WorkBuddy 本身了。

我打开一个新的对话窗口，直接问了一句：

“

你能生成视频吗？

WorkBuddy 说可以，列了一堆能力：文生视频、文生图片、图片转视频特效、3D 模型生成。

我就顺手给了一个画面描述试试：

“

黄昏时分，一列复古蒸汽火车穿过被雪覆盖的森林，蒸汽从烟囱袅袅升起

90秒之后，视频出来了，16MB，画面确实不错。

然后我就问了一个关键问题：

“

为什么生成的视频只有5s，能生成30s的视频吗？

它说不行，5秒是模型的硬性上限。

我不太信，追问了一句：

“

你生成视频使用的什么模型？

它说是腾讯混元（Hunyuan）的文生视频模型，底层是腾讯云 VCG 服务。

接着我又问：

“

你能看混元的api吗？

这次回答比较实诚：没有直接访问腾讯云控制台或 API 文档后台的权限，但可以读脚本源码和查公开文档。

我说：你去调查下，混元api都支持多少s的视频生成，想办法生成30s的视频。5s的视频没有应用市场。

这句话可能刺激到它了。

WorkBuddy 开始读源码、查文档，然后给了我一份调查报告：

从 buddy-cloud.py 源码看到，视频生成默认参数写死了 5 秒：

"Vendor": "Kling", # 可灵模型
"Model": "v2.6",
"ModelParam": {"Duration": 5} # 写死了5秒

各模型实际支持的最长视频时长：

模型

最长视频

Duration 可选值

Vidu viduq3-pro/turbo

16 秒

1~16

Kling

10~15 秒

5、10

Vidu viduq2 系列

10 秒

1~10

Hailuo

10 秒

6、10

没有任何一个模型原生支持 30 秒。

但它给了两个方案：多分镜拼接，或者多 GPU 并行加速。

多分镜拼接的思路是：生成多个短视频片段，然后用 ffmpeg 拼成完整的长视频。

“

我看到方案之后说：

“

多分镜拼接（推荐）：混元 API 支持最多 6 个分镜，每个分镜可以独立生成 5~10 秒，然后拼接成完整长视频。6 个 5 秒分镜 = 30 秒。

使用这个方案帮我生成 30s视频，我看下效果。

接下来发生的事，说实话有点曲折。

WorkBuddy 先试着改 Duration 参数从 5 改成 10，想用 3 段 10 秒拼接。但脚本里 Duration 写死了，改不了。它试了 monkey-patch、直接写独立脚本、复制 buddy-cloud.py 本地改……折腾了一轮，最后发现并发限制是 2 个任务，之前测试的任务占着槽位，新任务提交不上去。

最后它换了个思路：不折腾 10 秒了，直接 6 段 5 秒顺序生成，ffmpeg 拼接。

脚本跑起来了，后台顺序生成 6 段视频，每段约 90 秒，总共 9-10 分钟。

6 段全部生成完成，30 秒视频用 ffmpeg 拼好。

文件

大小

内容

scene_1.mp4

15MB

蒸汽火车驶入雪林

scene_2.mp4

13MB

穿越茂密雪松林

scene_3.mp4

13MB

俯瞰火车行驶

scene_4.mp4

11MB

冰湖倒影

scene_5.mp4

12MB

驶出森林进入雪原

scene_6.mp4

11MB

日落全景航拍

final_30s.mp4

74MB

30 秒拼接视频
**

“

然后我看了一下，发现一个问题：

“

为什么生成的视频没有声音？

WorkBuddy 回答说：混元 API 只支持无声生成，API 本身不支持同时生成音频。

这个答案让我觉得不太对劲。

一个主流的视频生成 API，怎么可能只支持无声？我就追了一句：

“

你从哪里看的，混元API只支持无声的？

“

它沉默了一会儿，然后说：

“

好问题，我重新确认一下。

然后去查了文档，查完之后改口了：

“

我之前说错了。查证之后确认：混元 API（Kling v2.6）是支持音频生成的，我之前没用这个参数而已。

关键参数是 sound: "on"。

参数

说明

sound

"on"
开启音频生成，"off" 关闭（默认关闭）

voice_list

可选，指定音色（V2.6+）

另外还有一个坑：只有 pro 模式才支持音频，std 模式不行。

就这一个参数，加上模式切换，声音就有了。

“

知道原因之后，我就让它重新生成带声音的视频，主题还是脱口秀——之前用视频制作专家没搞定的人像问题，这次换 API 直接来：

“

你帮我写一脱口秀的脚本，使用有上面的方案，带声音生成，然后合成我看下效果。

WorkBuddy 自己写了一个脱口秀脚本，6 个分镜：

-
演员出场、调整麦克风

-
讲段子、手势丰富

-
做出无奈表情、摊手

-
得意地笑、竖大拇指

-
比划相机取景框、表情调皮

-
鞠躬谢幕、观众席亮灯

这次 ModelParam 里多了两个字段：

{
"Duration": 5,
"Mode": "pro",
"Sound": "on"
}

就这三行改动，声音就有了。

“

然后跑脚本，中间又出了一个小插曲。

一直等不到提交槽位，每隔 20 秒打印一行：

[INFO] S1/6 waiting for slot (1)...
[INFO] S1/6 waiting for slot (2)...

等了半个小时没提交成功。

不是参数问题，是 5 月 11 日当天的 API 额度用完了——每天最多提交 10 次，之前生成雪林视频用了 6 次，加上几次测试调试，10 次正好耗尽。

等到 5 月 14 日额度刷新，重新跑，一切顺利。

“

6个分镜下载完成，用 ffmpeg 一行命令合成：

ffmpeg -y -f concat -safe 0 -i stitch_comedy.txt -c copy comedy_30s.mp4

28MB，30秒，1920×1080，AAC 44100Hz 立体声。

合并日志里出现了几条 Non-monotonic DTS 警告，但不影响播放，这是多段视频拼接时音频时间戳的正常偏差。

“

先给大家看下最终生成的效果：

看完之后说实话，画面效果有亮点也有硬伤。

亮点是：每段 5 秒的画面质量其实不错，有灯光、有观众席、有演员的动作，而且确实带了声音——你能听到舞台的环境音，不是静音。

硬伤是：每段里的人都不一样。

第一段是个穿西装的男的，第二段可能变成了另一个人，第三段又换了一张脸。

这不是 bug，是多分镜拼接方案的本质问题——6 个分镜是各自独立生成的，AI 每次随机生成一个人物形象，没法保证同一个人。

如果你只需要展示画面氛围（比如风景、场景、特效），多分镜拼接完全没问题，雪林火车那版就挺好的。但一旦涉及「人物连贯性」，这个方案就不够用了。

目前想到的解决思路有两个：

-
用图生视频（Image-to-Video），先确定一张人物参考图，每段都基于同一张图生成，人物一致性会好很多

-
等模型本身支持更长时长（比如原生 15 秒），减少拼接段数

这两个方案后续有空我试一下。

再解释一下这次生成的「声音」是什么：

不是台词，不是配音，是 AI 根据画面内容自动生成的环境音。

脱口秀场景里，AI 生成的主要是舞台气氛音、观众的背景声，不会自动生成「演员说话」的声音。

如果要有真实台词，下一步可以单独做 TTS 配音，再用 ffmpeg 混轨进去，那就是另一篇文章的内容了。

这次最大的收获不是视频本身，是那句追问：

“

你从哪里看的？

AI 的第一个答案不一定是对的。不懂的时候问一下出处，它会自己去查，查完发现错了，会重新告诉你正确的。

这个习惯用起来，能省掉很多走弯路的时间。

你用 WorkBuddy 生成过什么内容？有没有遇到过 AI 第一次答错的情况？

评论区聊聊，下期看你们的场景出。

这是WorkBuddy 100 种用法第44篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #AI工具 #视频生成 #AI视频 #可灵 #脱口秀 #多分镜 #效率工具 #AI声音 #Kling #ffmpeg #混元视频

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNQyKZXxrbvCrlttDknTCljfQZW7RLr7ibORyrn8BfCemy6zDKumnwuLGOnXiaUHH1zEIka4QvVia62mxZwfia7Mk2GWyQZCibXdxLE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROqnwmZUVicVpT4icnsz1t80yX2gjGnIccLafiaEOKJauHnq0CPaCSZ0VbH2JChqchc9rjrTp7q5MYU6YeSAicy82nqOMpzZ22olYA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNF2OZzNUJkCDdA2uvBP1icXmIx1MGdSUnMsicjYTibDsRHyddJKGJor4xrn9xklyLL07XGdJYEdzicAiacVOBib4jONtuAdzAWZPpeU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROxicgEAPlaiaeq0EpZQWrE8WiaNhFxdH66ibibezLZ930NxpTLhkMIpMTzTCqDCjFUREgW8UpNdRl8HkiaAHMnpQfpgm4icAsicUtL8Ek/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPZG7RMJ6aFPnWZSiaCSfLkknUO6rLyle5z4O6zDjTOLamiaia2uvCZ1JqQQdgibd87Nnic8sn6CFPxX6yFm3rNyZXHn6WDoTOCRFxA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP62ibAzOia0icvokiaInHenddh92dS0Kgq5wOAdjRA9P71MmEK3LCXgy4WibHBmZvenaQcO4ooJwnQlA08JffBAe5Q3XTciaMfDqibeg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPSZwZglt27rUzvicQibAor6KuZF7Fs0U08Y68tM0zmYYpnDmiaibEjJLJkrzBKKNkvqJmGNSIPepAW5ZjdThw6n1jNYmF3bGwibiaco/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNHb9GP27225zwcIKlQ9wWqw9XYjCtkXhkYyprRrmLpDbWZeicicLnMK28WrQ8NLH1UUXcXfDHqqtObBsiblYVNkmQxHt0llalu40/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMQ0hndvkRiaBeUQJJn91sWF0naeAMjQOSWWmUtT5AAQyejsLngdZiaTA6yQ5KRGuL3lliamAmmH5IGujPBttZXIs7DLMiaTDVnKS4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMpRicJ4Rh5Jg2ibASQ0kYgRGuTlgaebeGcAezdgYj4h9M5V7zRS0JldOxllgvHTbVlZAJNyHTYW6Bdkw5KSW0Ok6JyDUFcyamrA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROibRtCYhsjPbcEb3ia9k3hgu1vxZJPFNNMO6ibicMkcMLyEwmgo9hgKFs8ppjpu9LCETxtHXLPibAXqGLYBoGcZzogibuu1dhdjDhZk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNrdljTWvQUWicEVsrIeV6DFDBjL4QdNGTP3ian4W2hsegEeAadUzYjALzI0qhuicOKUoxGCe34VAT8icicBLfsYHGthk0BibSMuNP18/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPrgRwRVA38c1aXiaqkIrrEUcTR205Ljm4J5sKVY1uwibjogMboqfeUS3ibhWKIp5bn1UvIbJHiaX3wTpCMZNkUt9ia4qmIGjkxUZq4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMeoUBWpL3M4RRu8xqqWWT3K4EiaVyzLxdSU6ALNAZl8qJSbCY3viblZuwJ3mmvatbibKoEVb6DISViatU2Q1SErgiaVclxsgG9LKzY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMJ0w4FTFniacuXF6YHicg3UAw0q5KaZcPibPROU97DVPbCLSpSiaLKulIGHDkxND68IaTJG7KDvPBntO7ngTRPotGRjKjrrosWiabA/640?wx_fmt=png&from=appmsg
