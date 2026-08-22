# WorkBuddy 100种用法 #72 | 封装一个公众号贴图技能，从生图到发草稿全自动

- 合集序号：72
- 公众号：我与ai的那些事
- 发布日期：2026-06-11
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329553&idx=1&sn=6515febf7c8bb19ab266f3ef953b3f18&chksm=88303596bf47bc8086063089a508ce49ccb036cc03b973c3f641b1c6b3c6c470603642668042#rd
- 正文字数：3074
- 正文图片：10

## 摘要

微信出了个「贴图」功能，我让 WorkBuddy 帮我封装了一整套发布技能——混元生图、自动上传素材、一键创建草稿，踩了 5 个坑才跑通。

## 正文

最近看好多朋友在玩微信贴图，早上随口问了一嘴 WorkBuddy——

「微信公众号出了个贴图功能，你知道吗？」

他竟然说他不太清楚！！！

再问他知道不知道，他去搜索了下。

「这是单独的问题，与ima没关系。我是问你知道不知道贴图」

它先是搜了一圈，说这是个新功能，2026 年 2 月才灰度上线，形态对标小红书——不用写长文，一张图加一句话就能发。
然后我问它：这个功能，可以使用api方式吗？如何可以，如何处理？

「这个功能，可以使用api方式吗？如何可以，如何处理？」

它搜完告诉我：目前贴图没有独立的发布 API，能用的替代方案就两个：要么用素材管理 API 上传图片，要么手动发。草稿箱 API 只支持图文，不支持贴图。

又给我瞎说……

我把微信开发文档，甩了一个链接过去：

「你好好看下这个接口文档，这里面不是有类型图片消息吗？」

WorkBuddy 看完，沉默了——确实有。draft/add 接口的 article_type 参数有两个值：news（默认图文）和 newspic（图片消息）。newspic 就是贴图。

原来贴图跟图文走的是同一个草稿箱接口，只是换了个类型。

我接着问：「发贴图除过发图片，还需要什么？贴图内容和图片，标题，话题关键字，你要帮我准备好。」

WorkBuddy 确认了一遍字段：title（标题）、content（正文）、image_info.image_list（图片列表），话题关键字没有独立字段，在正文里用 #话题名# 实现。

故事这才正式开始。

下面是用混元生图生成的第一张贴图样张——「AI生图公式」主题，768×1024 竖版：

先踩的几个坑

搞明白接口后，第一个问题：图片从哪来？

贴图里的图片必须用永久素材，也就是 material/add_material 接口返回的 media_id。我一开始图省事，用了 uploadimg 的 URL，连报两次 40007 invalid media_id。这是第一个坑。

第二个坑——这个接口最花时间。搞到这一步，我突然意识到：这跟 WorkBuddy 平时封装技能的逻辑几乎一模一样——输入内容 → 调用服务 → 产出结果。为什么不把整个过程封装成一个技能？

让它帮我封装一个技能

我跟 WorkBuddy 说：「帮我把这个过程封装成 skill」。

注意，不是让它写个一次性脚本，而是做成一个可复用的技能——下次我只要喊一声「发贴图」，它就知道该干什么。

不到几分钟，WorkBuddy 搞出了一个 wechat-tietu 技能，结构很清晰：

~/.workbuddy/skills/wechat-tietu/
├── SKILL.md ← 完整流程文档
└── scripts/
└── tietu_publish.py ← 核心脚本

这技能能干什么？简单说就是：我给它标题、正文、图片路径，它自动搞定后面的所有事情。

而且生图环节不写死——默认用混元无水印，我如果想用 DALL·E、即梦、Nano Banana，一句话就能切换。

但是，坑来了

第一个版本跑起来就炸了。

坑一：中文全变乱码

草稿创建成功了，打开后台一看，标题和正文全是 \uff0c、\u5de5 这种东西。

这跟微信没啥关系，是 requests 的锅。它家 post(json=payload) 方法默认会把中文转成 \uXXXX 转义序列发出去，微信原样存了。

改成手动序列化就好了：

# ❌ 旧写法
resp = requests.post(url, json=payload)

# ✅ 修复
resp = requests.post(
url,
data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
headers={"Content-Type": "application/json; charset=utf-8"},
)

关掉 ensure_ascii，中文以 UTF-8 原文发送，问题解决。

坑二：换行符成了字面文本

第二篇草稿发上去，正文里赫然写着 \n\n。

因为命令行的 \n 传到 Python 里是两个字面字符（反斜杠 + n），不是真的换行。微信又原样存了。

WorkBuddy 在脚本里加了一行自动转换：

args.content = args.content.replace("\\n", "\n")

修完重发，换行终于对上了。

坑三：标题报 45003

标题明明只有十五个字——「记住这3个AI生图公式」，怎么还报超限？

后来发现，微信贴图的标题限制是 32 字节（UTF-8），不是 32 个字。中文字在 UTF-8 里一个占 3 字节，15 个中文字 = 45 字节，早就超了。

改成短标题「3款AI，画出三种世界」才过去（8 个字 = 24 字节）。

这个坑 WorkBuddy 也顺手更新到了技能文档的错误码表里。

下面是用混元生图生成的对比贴图样张——同一 prompt，三种 AI 画风：

坑四：IP 白名单没设

这其实是最大的一个前置条件，不设的话 access_token 都拿不到。

微信要求把调用方公网 IP 加入白名单。WorkBuddy 把这个提醒直接加到了技能的「首次使用：凭证配置」章节里，还在脚本里做了自动检测——遇到 40164 / 61004 错误时，自动 curl ifconfig.me 查出口 IP 并打印设置指引。

坑五：凭证路径不通用

初版脚本的凭证路径写死在我自己的 ~/.baoyu-skills/.env 里。这显然不对——别人哪有这个目录？

WorkBuddy 改成了自动查找：先找 ~/.workbuddy/wechat.env（所有用户都有），找不到再 fallback 到旧路径。新用户只要创建这个文件就能用。

实际效果：一口气发了 5 篇

技能封好之后，我让 WorkBuddy 帮我出个系列选题——「AI工具美学」，5 篇贴图，从选题到生图到草稿全部一条龙。

#

标题

类型

1

WorkBuddy，你的AI数字搭子

Hook 吸引型

2

记住这3个AI生图公式

干货教学型

3

3款AI，画出三种世界

对比展示型

4

一个打工人的AI 24小时

场景代入型

5

2026，AI工具箱升级指南

总结推荐型

每篇配 2-3 张混元无水印生图（768×1024 竖版），加上正文和话题标签，五篇草稿全部创建成功，就等我在后台手动点「发布」。

推送到草稿箱后的效果：

下面是其中几张贴图的效果样张：

这个技能现在能干什么

以后我要发贴图，流程就是：

我：「发贴图，主题是XXX」
WorkBuddy：规划内容 → 生图 → 上传素材 → 创建草稿
我：去后台点「发布」

一句触发，全流程跑通。

而且这个技能的设计思路是开放的——生图模型可选、凭证自动查找、错误有详细指引。换了电脑、换了人，照样能用。

一个小总结

这次经历让我对 WorkBuddy 的技能封装有了更深的理解：

一个真正「可用」的技能，不光是能跑通自己的机器，还得考虑别人怎么用。凭证放哪、模型怎么切换、报错怎么提示——这些「边角料」才是决定一个技能能不能流传开的关键。

另外，这次还有个很重要的体会：AI 给的答案不一定对，要有自己验证的能力或办法。

比如一开始我问 WorkBuddy 知不知道贴图，它说不知道。让它去搜，它搜得浮皮潦草的，直接下结论说「贴图没有独立 API」。我把微信官方文档链接甩过去，它读完才承认自己没好好搜——article_type=newspic 明明写在那儿。

所以用 AI 干活，也不能全信。关键信息自己看一眼文档，或者拿着官方的东西跟它对一下，往往能发现它漏掉的东西。

这是WorkBuddy 100种用法第72篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #公众号运营 #贴图功能 #混元生图 #微信API #技能封装 #自动化发布 #内容创作 #AI工具 #效率提升

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROaRKicGHuNwrE4mWYQMqCic1l8gpETsf8VC4DjL6BkoibPianQDZiagvEDKD5s1MKd3fKVWeV1iagxOmibDkotDR2hjRd8JNrYjicxibcY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMXK9INWzxcSmUvibs0iaxMcH8npQ17FE3UMMNWnBTS2RV4kANN4RqF4ou0WnSuO74kNiaZTO8wzcyQyXXiaRqBCHXeIo9gmrumhOo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROqkLd3O36ic96h7yDzGgMLxIh05W9csC73mN5O62ctWIzR519VZYQtKAAAJnJ6SLfUjL0kP15YDicARjpEHa80QcUk5kicicb2ibV4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMQ50QADcAAb4lQ3jyzprjQR2y9QBgHdVxk6AH7OI4gfw5MkfJprICiaxFQaXaJBWqBzlGMwV3Pv8TwtFjEYJPEpc5seWicnOxMw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROx5WbWqNhzKYdibNuAia0jxUcKp0yGIElgcBBKicHbDhtlSOaewAokckjnofFxibNXqbD7lu7PaUyC95ZVuuXIUVMZ8JGib6bjMIjo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROusJeibvhOFb0g3ldNwhXgocF7VKls8rOF8ZPK5fuEbDKQov0ox1r0GvdjHiaw9K0YWiahVzUuSKzlLF6eaeyxI8GlgDZO5DBGyQ/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNwiaiaaIObsQkO4uhY92FZXG3c3ib0DC8l9z1uFE577yzR8y4n9JsAGND4v3AQzFF1vYALP41ThPRRqBict7DX1fibiaiaOSTZXaznrk/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRPmutGcpicDaZBtYcmSnnYky0psBau1WUquj05s7TTiaPbzRSx4xLUoyt5gqxYf5VluSWhksDHl1Fw56G7rM5qfic7ReNVtww38y4/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMRxZuaiaU2aeVgYDlrleWPlUzrWgelqwCRrpEK7LUSQHWo215vkBJk5K8DU8mibBlx70UhtcreCM3RTMrUB4Hp2VDzduJo3Y9Dg/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNRhXwbj2OMv0QUaxqM7SeClXpqsSVfvLhEGE61SM8eh2iaYXsO8w766BiaSZlgg6FV7htc57evWFnfcCoPmprao7qMtVQOXFiaPk/640?wx_fmt=png
