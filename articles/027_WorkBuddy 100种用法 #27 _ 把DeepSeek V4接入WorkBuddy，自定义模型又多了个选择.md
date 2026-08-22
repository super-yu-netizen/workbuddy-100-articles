# WorkBuddy 100种用法 #27 | 把DeepSeek V4接入WorkBuddy，自定义模型又多了个选择

- 合集序号：27
- 公众号：我与ai的那些事
- 发布日期：2026-04-27
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328463&idx=1&sn=4c5ba377b06e63329d5f2e7e46d43e60&chksm=883031c8bf47b8dede9ac6f2595178a6b0069147954b528e81ee85271159db83530b42ecb8f5#rd
- 正文字数：2643
- 正文图片：14

## 摘要

本文记录将 DeepSeek V4（含 V4 Pro 和 V4 Flash 两个版本）接入 WorkBuddy 的完整过程，包括 API Key 申请、实名认证、充值步骤及配置参数，帮你快速解锁自定义模型新选择。

## 正文

DeepSeek V4刚发布没多久，今天终于把它接入到WorkBuddy里了。以后用自定义模型又多了一个选择。

这篇文章记录一下接入的全过程，包括怎么申请API Key、怎么充值、怎么配置、填哪些参数，以及我踩过的一个坑。

DeepSeek V4是什么

DeepSeek V4是DeepSeek刚刚发布的新一代大语言模型，有两个版本：

-
• V4 Pro：专业版，性能更强

-
• V4 Flash：轻量版，速度更快

两个版本都支持思考模式（reasoning），API调用方式和OpenAI兼容，配置起来比较简单。

接入WorkBuddy的准备工作

在开始之前，你需要准备两样东西：

-
1. DeepSeek开放平台的API Key

-
2. WorkBuddy的自定义模型配置文件

下面一步步来。

第一步：申请DeepSeek API Key

1.1 注册与登录

-
1. 打开浏览器，访问 DeepSeek Platform 官网：https://platform.deepseek.com/

-
2. 使用手机短信验证码或者微信扫码登录注册

-

-

1.2 创建 API Key

-
1. 登录后，点击左侧菜单的「API keys」

-
2. 点击黑色按钮「Create new API key」

-
3. 在弹出的对话框中填写 API Key 的名称（比如"WorkBuddy专用"）

-
4. 点击「Create API key」完成创建

-

⚠️ 重要提示：API Key 创建后只会显示一次，请立即点击「Copy」复制保存。如果忘记保存，只能删除旧 Key 后重新创建。

-

第二步：实名认证与充值

2.1 实名认证

DeepSeek API 需要完成实名认证才能充值使用：

-
1. 点击左侧菜单的「Top up」（充值）

-
2. 页面会提示需要完成实名认证，点击「Verify」按钮

-
3. 选择认证类型：「Individual」（个人）或「Enterprise」（企业）

-
4. 填写以下信息：

-
• Real Name（真实姓名，仅限中文）

-
• Type of ID（证件类型，默认选择「二代身份证」）

-
• ID Number（身份证号）

-
5. 勾选同意服务条款

-
6. 点击「Submit」提交认证

-

2.2 充值

实名认证通过后：

-
1. 进入「Top up」充值页面

-
2. 选择充值金额：¥10、¥20、¥50、¥100、¥300、¥500 或自定义

-
3. 选择支付方式：支付宝或微信支付

-
4. 点击「Next step」完成支付

-

充值完成后，可以在「Billing」页面查看充值记录和余额。

💡 费用说明：DeepSeek API 采用按量计费，充值金额仅用于 API 调用。网页版和 App 对话是免费的。

第三步：让WorkBuddy自动配置

3.1 最简单的方式：让WorkBuddy帮你配置

拿到API Key后，最简单的方式是直接告诉WorkBuddy：

"workBuddy 中使用自定义模型接入 deepseek v4，API Key是 sk-xxxxx"

WorkBuddy会自动帮你填写好所有配置项，包括URL、模型名称、是否支持思考模式等。

3.2 手动配置（可选）

如果你想自己配置，或者想了解具体填了什么，可以手动编辑配置文件。

WorkBuddy的自定义模型配置文件位置：

~/.workbuddy/models.json

如果文件不存在，创建一个即可。打开 models.json，添加以下配置：

{
"models": [
{
"id": "deepseek-v4-pro",
"name": "DeepSeek V4 Pro",
"vendor": "Custom",
"url": "https://api.deepseek.com/v1",
"apiKey": "sk-你的deepseek-api-key",
"supportsToolCall": false,
"supportsImages": false,
"supportsReasoning": true
},
{
"id": "deepseek-v4-flash",
"name": "DeepSeek V4 Flash",
"vendor": "Custom",
"url": "https://api.deepseek.com/v1",
"apiKey": "sk-你的deepseek-api-key",
"supportsToolCall": false,
"supportsImages": false,
"supportsReasoning": true
}
]
}

3.3 关键字段说明

字段

说明

id

模型唯一标识，后面切换模型时会用到

name

在WorkBuddy里显示的名称

url

DeepSeek的API地址，必须是 https://api.deepseek.com/v1

apiKey

你的DeepSeek API Key（第一步申请的）

supportsReasoning

是否支持思考模式，V4建议开启

保存文件后，完全重启WorkBuddy，模型就会出现在模型列表里了。

踩坑：刚开始DeepSeek V4不支持图片

配置好之后我兴致勃勃地测试，结果一上来就报错：

Failed to deserialize the JSON body:
messages[80]: unknown variant `image_url`, expected `text`

这个错误的意思是：DeepSeek V4不支持图片输入。

问题出在对话历史上。之前我用别的模型跑过带图片的对话，WorkBuddy切换到DeepSeek V4后，把整段历史都发过去了，但V4只认纯文本，不认图片。

解决方法很简单：开一个新对话，不要带任何图片消息。

所以如果你在WorkBuddy里用DeepSeek V4，建议：

-
• 开启新对话时再切换到这个模型

-
• 不要在包含图片的历史对话里切换

切换模型试试

配置好之后，在WorkBuddy里切换到DeepSeek V4 Pro或Flash，就能直接用了。

DeepSeek V4的响应速度不错，思考模式开启后能看到推理过程，对于需要复杂推理的任务很有用。

写在最后

WorkBuddy的自定义模型机制真的很方便，只要API支持OpenAI格式，理论上都能接进来。DeepSeek V4刚发布，趁现在用的人还不多，可以先体验一下。

这是「WorkBuddy的100种用法」系列的第27篇，前面26篇覆盖了很多实用场景，如果你感兴趣可以翻一翻。

本期互动：你还想把什么模型接到WorkBuddy里？或者接入时遇到什么问题？评论区聊聊。

#WorkBuddy #DeepSeekV4 #自定义模型 #AI接入 #DeepSeek配置 #WorkBuddy进阶 #模型切换 #API配置 #效率工具

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNMnOKyDwth7Lz7w8h131lzvmafSb6qBh9jbRb6bpLuaHJibAPNt3sDnFFfHNGjYdX6ZvfHqib1huqbjcUrxRx6tUtaAMMeF38jE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO5vpnFtWcBswYSMDKJgHfSl8qiagjasP4RNz2eJQ0oqROLFSmRPibHsvUVXDeZDZpFCaljsWEXaXokeOgjFFicY8T0c3wLibSxPDY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM6NBSBZTtPq75tAL9iaXMYcia7oOtE82LPZfEic99c6CCgs4MKyIcicLuibzbianrgUyxZ6pviciay9kts928D5TWBOCZLMhHdiaK9VExQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPK7EwwiahwwQ7Xp65koiagkv0kk8MdjwCPI0IGeiapoRy1LlKMcfUeQLNxbwnbYVibCKr1WXHhIYH6pTT4LSGzcuFgkbnILxGib2Rg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROsSnwRf942BlThriaGCNP7Hakia4e7iahaiaqoQwe9BvyZPopeye7GMxxpJnhWdqoOyu3vbvUkqWURFJzyyzRic03sJ0JRAPHLEZG4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO7mXQsB4hmuiaLib87UDZUGmKlv8ja4QMpnic2EpkEprxKSy1ekYG4aaQtTV9MnWicMITYfzbjYhxTDvsvI5kkXe4MQ8wOouBdQtY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPQuDicDheWHdtmwvgBPYxd4jpyjjNXfeeg2MDKQmBN6Lmv87knYWDj7hTWIsPbSfGNcuKp5k5oWOy2kffzHv18voqlwb4NCbqU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROlEvmW1ppic08XCKQpLoJu254obV5lzXzeiaQoE3mpT3ic1GW7mYl20PVW089jfx3ayLMVjTm864YVOOdIE8U49SWJJQZGj6hJQU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPrFCojqoPrLV4HT69WVh9FIj13MNV9aShM99ZcMYG0qQuTpgYIxiaHZNibQUcy74hNibicv0ib8jaj1vJOiasrhLWX8vjz04q0lFJAE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNcEbKx0QFtK56GfLT5Neic92dSxXic5pRZ7OSy2RvCYmY97YALiaMlMCkjEhZLckl3RCn7CqicEOadB75BZic664Ric3zxdwYIBUIkw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROOsIMPwSUdYuGiafWsKKj7BWib4viagw3HAibUoPSjNH4QlVAZNATeWCSA5ON6wCgtZPgjQsvrElYQPSmHxpHLr9aZicTkDzJu6BiaY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP4VIrEru3m6ibHnmTQnpa4oiayyrrllcGZ5SLKXia0xErkwmeYhJ5eDc1H4ibhHHhGGibO5tOrqTynNSxBW7bv8mfLd6RibeFRZUuhw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN2HSQCsySgNYlqdiaiaezZwfahZ0mbnmzqIibJuXoiaQw9RqOiahtY9RRQYfTDLtMkicWlrVwa0NBSe3fqibErjn1PtBzDEZaGpFhyt0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNlVugEuZWR7eu4B4f3tbHSRufLeHSAk9C2tzf9OGyNw9ic957A7ia8Yo9Pzs9Ecqa3u9n9F94HyznRSvFjY0RrwicIrVSX7m083I/640?wx_fmt=png&from=appmsg
