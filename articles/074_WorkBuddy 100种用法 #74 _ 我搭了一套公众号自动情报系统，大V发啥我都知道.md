# WorkBuddy 100种用法 #74 | 我搭了一套公众号自动情报系统，大V发啥我都知道

- 合集序号：74
- 公众号：我与ai的那些事
- 发布日期：2026-06-13
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329630&idx=1&sn=daf68e64d961bb779792487dabe25d84&chksm=88303559bf47bc4f224d9333451c754fb7138028ff039da1b9f1a390a3e19d418c7b9fffc7f9#rd
- 正文字数：4391
- 正文图片：15

## 摘要

从发现WeRSS项目到部署踩坑，再到用IMA知识库搭建公众号自动情报系统，大V发啥我都知道，早9晚6自动同步，一个WorkBuddy全搞定。

## 正文

今天在GitHub上刷到了一个项目叫WeRSS，能把微信公众号转成RSS订阅源。

我直接把链接丢给WorkBuddy，让它帮我介绍下这个项目。

WorkBuddy看了一圈源码和文档，给我整理了一版介绍：这是一个把微信公众号转成RSS的开源项目（Star 3.5k），核心功能就四个——公众号转RSS、Web管理界面、定时自动更新、钉钉通知。技术栈是Python+FastAPI做后端，Vue3+Vite做前端，数据库用的SQLite或MySQL可选。

看完介绍我没多想，直接抛出了我的真实需求：

我想做这么一个功能，把关注的大V的公众号采集下来。加入到IMA知识库，形成自己的内容情报系统。这个应该怎么做？

WorkBuddy思考了一下，直接给了我一个完整的架构方案：

微信公众号
↓ （采集）
WeRSS / WeWe RSS
↓ （RSS 输出）
定时抓取脚本
↓ （解析清洗）
IMA 知识库 API
↓ （存储）
IMA 知识库（可分主题建库）

就这么几句话，整条链路就定下来了。但我有个问题：公众号又没开放API，它怎么抓的？

两种采集方案，两种思路

架构方案里提到了两个采集工具——WeRSS和WeWe RSS。我先问了WeWe RSS的原理。

WeWe RSS 采集的原理是什么？帮我简单介绍下。他为什么能采集公众号内容，原理是什么。

WorkBuddy解释：WeWe RSS走的是一条"曲线救国"的路——通过微信读书间接获取公众号文章。

微信读书 App（weread.qq.com）
↓ 可以搜索和阅读公众号文章
WeWe RSS 登录你的微信读书账号
↓ 调用微信读书的内部接口
获取公众号文章列表和正文
↓ 转成 RSS 输出

但这里有个关键问题：WeWe RSS不是直接连微信读书的，它要经过一个闭源的第三方中转服务weread.111965.xyz。你的微信读书token要先发到这个中转服务器，由它转发请求到微信读书。

我接着问：

weread.111965.xyz 这个中转服务主要作用是什么，我自己搭一个可以吗？

WorkBuddy查了一圈告诉我：这个中转服务没法自己搭——它是闭源的，代码没公开，只提供接口。也就是说，你的token要过一遍别人的服务器，安全性不太可控。

这我就不太放心了。于是我问了第二个方案：

方案2：WeRSS（你之前看的那个）中有没有中转，他的原理是什么？

这一问，答案完全不一样——WeRSS没有中转，所有流量直连微信服务器。

WeRSS模拟的是微信公众平台后台（mp.weixin.qq.com）的操作：

-
让你扫码登录微信公众平台（跟你自己在电脑上登录一样）

-
用Playwright无头浏览器模拟真实操作，拿到你的登录token和cookie

-
用这些凭证直接调用微信公众平台的后台接口，获取文章列表和正文

-
转成标准RSS格式输出

你的微信扫码授权
↓
WeRSS拿到微信公众平台的token + cookie（存在你自己机器上）
↓
用token直接请求 mp.weixin.qq.com 的后台接口（不经任何第三方）
↓
拿到公众号文章列表 + 正文
↓
转成标准RSS格式输出

它甚至还内置了一套反爬虫对抗机制（anti_crawler_*.js），包括模拟鼠标行为、User-Agent轮换等，让请求看起来像真人操作。

两边一对比就很清楚了：

WeWe RSS

WeRSS

数据来源

微信读书（weread.qq.com）

微信公众平台（mp.weixin.qq.com）

是否需要中转

✅ 要经过 weread.111965.xyz

❌ 直连微信服务器

Token安全

要发到第三方服务器

只存在自己机器上

项目状态

已归档，不再维护

活跃维护中

果断选WeRSS。token不过别人手，这点很重要。

这也是为什么WeRSS需要定期扫码续期——因为微信的登录token会过期，过期了就得重新扫。

踩坑开始：部署WeRSS

原理搞清楚了，开干。

我的服务器是一台AWS EC2，上面已经跑了newapi（3000端口），WeRSS用8888端口，不冲突。

Docker部署一行命令就搞定了：

docker run -d \
--name werss \
-p 8888:8001 \
-v ~/werss/data:/app/data \
--restart unless-stopped \
ghcr.io/rachelos/we-mp-rss:latest

但部署完发现访问不了。WorkBuddy一看就说：AWS安全组没放行8888端口。

它手把手教我：EC2控制台 → 实例 → Security → Edit inbound rules → 加一条Custom TCP 8888端口 → Save。

还提醒我：0.0.0.0/0那个警告不用管，个人工具站无所谓。

登录又翻车

端口放行了，WeRSS页面打开了，但登录又出问题——输入账号密码提示错误。

WorkBuddy说：部署的时候没设账号密码环境变量！ WeRSS的账号密码不是在页面上注册的，要在Docker启动时指定。

好，重新来。因为密码里有@符号，WorkBuddy建议用环境文件的方式：

cat > ~/werss/.env << 'EOF'
USERNAME=zgedu
PASSWORD=你的密码
SECRET_KEY=werss2026secretkey
EOF

注意那个SECRET_KEY——第一次我没加，登录看似成功但Token不生效。加上之后才正常。

扫码授权：二维码又出不来

登录好了，到扫码授权微信这步，二维码又加载不出来。

看日志发现问题：后端生成了二维码，但前端找不到图片文件。

WorkBuddy给了一招——用主机网络模式启动：

docker run -d \
--name werss \
--network host \
-v ~/werss/data:/app/data \
--env-file ~/werss/.env \
-e PORT=8888 \
--restart unless-stopped \
ghcr.io/rachelos/we-mp-rss:latest

重启之后二维码出来了，就是有点卡——毕竟服务器在美国，请求微信接口要跨太平洋，能不卡嘛。

25篇文章，一键入库

扫码授权成功，添加了公众号，RSS地址出来了：

http://x.xx.29.xx:8888/feed/MP_WXS_3089182632.rss

WorkBuddy验证了一下RSS能正常访问，25篇文章全在。

接下来就是重头戏：把文章导入IMA知识库。

这里有个细节值得说清楚。IMA提供了三种操作方式，但能力不一样：

方式

能做什么

能写入吗

IMA MCP连接器

搜索知识库、获取条目内容

❌ 只能读，不能写

IMA Skill

读取 + 写入（通过内部脚本ima_api.cjs调OpenAPI）

✅ 能写

IMA OpenAPI

完整的读写能力

✅ 最直接

一开始WorkBuddy先试了IMA MCP连接器——不行，只有读取能力。然后改用IMA Skill自带的ima_api.cjs脚本写入，结果报skill auth failed。一查，OpenAPI凭证过期了。

我去ima.qq.com续期了凭证。续期之后，WorkBuddy直接用curl调IMA OpenAPI的import_urls接口搞定了。其实IMA Skill也能做这件事（它内部调的就是同一个OpenAPI），只是当时WorkBuddy换了种方式没再回头试Skill。

最终用的是import_urls接口——直接把微信文章的URL丢进去，IMA会自动抓取正文入库，不需要自己下载文章再上传：

# 实际调用方式
curl -X POST "https://ima.qq.com/openapi/wiki/v1/import_urls" \
-H "ima-openapi-clientid: 你的ClientID" \
-H "ima-openapi-apikey: 你的APIKey" \
-H "Content-Type: application/json" \
-d '{
"knowledge_base_id": "你的知识库ID",
"urls": ["https://mp.weixin.qq.com/s/xxx", ...]
}'

25篇文章，分3批导入（接口每次最多10个URL）：

批次

数量

结果

第1批

10篇

✅ 全部成功

第2批

10篇

✅ 全部成功

第3批

5篇

✅ 全部成功

整个过程从拉RSS到入库，全是WorkBuddy在对话里帮我操作的。我啥也没干，就说了几个"好"和"继续"。

IMA凭证的坑

说起来中间还有个小插曲。

写入IMA知识库需要OpenAPI的Client ID和API Key。我之前配置过，但过期了。WorkBuddy先通过IMA Skill的ima_api.cjs脚本尝试写入，一直返回skill auth failed，排查后发现是凭证过期。

需要去ima续期凭证。续期之后，可以使用ima skill或者直接调用api都可以。我这里WorkBuddy直接调用了IMA OpenAPI就通了。

还有一个知识点：IMA知识库的ID有两套。MCP连接器返回的是短ID（比如7471411958392889），但OpenAPI接口用的是长ID（比如IQZDEbf14_n4fXCkn4cbfb6SDugzQEMOZbuiUB2_pDA=）。WorkBuddy帮我通过API查到了正确的长ID，这才导入成功。

最后一步：自动化

历史文章入库了，但总不能每次有新文章都手动同步吧？

WorkBuddy帮我建了两个自动化任务：

任务

触发时间

做什么

早间同步

每天 9:00

拉RSS → 找新文章 → 入库IMA

晚间同步

每天 18:00

拉RSS → 找新文章 → 入库IMA

自动化会自动维护一个状态文件，记录哪些文章已经入库了，不会重复导入。

现在整条链路完全自动：

大V公众号发布新文章
↓ WeRSS定时抓取
更新RSS Feed
↓ WorkBuddy自动化触发（早9晚6）
拉取RSS → 发现新文章
↓ 调IMA接口
自动入库「公众号内容情报库」

我什么都不用管，每天早晚各跑一次，新文章自动进知识库。

加更多公众号

目前我只加了一个公众号做测试。WeRSS支持添加多个公众号，在后台点"添加"就行。

不过要注意：

-
一次性不要加太多，容易触发微信风控

-
建议先加3-5个试试

-
每个公众号都会生成独立的RSS地址

加完之后，在WorkBuddy里告诉我要加哪些RSS地址，我帮你更新自动化任务的配置就行。

最终效果

现在我的IMA知识库里有一个专门的「公众号内容情报库」，里面自动收录着我关注的大V文章。

想找选题灵感的时候，直接在IMA里搜关键词；想看某个领域的最新动态，知识库里都有。

从"收藏即读过"到"自动入库随时搜"，就差一个WorkBuddy。

这是WorkBuddy 100种用法第74篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #公众号采集 #RSS订阅 #IMA知识库 #内容情报 #自动化 #WeRSS #微信公众平台 #Docker部署 #AWS

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPDZC0VkKziapDW0LPAoModX5jwhjYFLW0ib6qF6t2dsrHiaS98q7pqaRficbwvom2L35CE4xzSo7TrcjAUAsauqcKLIooHdia1khXo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPxKbluw8EBibiakPO7CbuhYmK6JMYc7YibX74qe45DkiaYTogYzmNgcqhX2NKYDbbpFVCeor27tHkarp4kQu6IfVkPZWQYsXJicfuk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNXUyQCXJtUIbNfic5ELIDUoDm44hNyVcNW9dm1q6Rltv70x9H7IWr0OFFRSyBaBSkUqjeI3kHFr10p5IJQIo0I1qib9F7wevibbs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMibd0Aiby7wbiab2WKCQezSUwZu6saQ422icsichnWolYkr6mwsJLTgcZON8xrVKklL5QgnKjtoIWOPkgqEchyGzt2U3Z5L3QVpZUU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROkmBHeSxW8RZs1uq0Kju3sOsic4ospYziaOQdCOv1qs9Uf1NiatcicCUrl4iaSG5jv7RXCLMCWicC6TrFGXficFZceNM1uqbAEia9Oycs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMUgMoDrArG1mnFFvYiaBxzueTIE5BCZ8sLvNHnbB5ov4icOfZnhpflUeK7oANyD81JSJ9kSicuzOP0fu7wGxFRKQqTKjHUAGGXzY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPia9FCqCNYZk6UWubISUQSU3Nic407ouP3Oy8GchKAJKuiacLZthADqro93XlOxfrS56emn03zUm5rU0RCRVqflRYr0REmvgKuto/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROG5AoiaCPcXwkyfXpic0uDTFnwgYedC6YPBbNcLbOfhqqdp9eicfJ02CHAvElUbmibEczgxNEGSajFUOAx1oAas1vF2YTwFt8cwmA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMnia1iaRic6N9n2MHOAGzYRjaDII0ooiaZf0iazwZoEcibshe76Y1Og7Z3KteTNbJGxQ2rqJ0LnvFf0W5WrNRAFcDRx1tsVOGxurMZE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRNv6yDd04Srn7vtHTYe6lSeyDWicKpjpoPvVPUXxkGeQ9clB5Aicibf9AFfSplJyhSy0PeGEaxVNM7ShjWravqiaRlUg3xz6SXl87M/640?wx_fmt=jpeg&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRODMbHQuvZriaLUENq0leZCHC99yc8kLT7ia3Gg0LDLmCsjvtjoEQh55R2jvp2k5iaZDRbZcRTVsWARN8KadxFxwiayJhbI4EibUvw8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNZFevb6ELf0Mdib5P9m1Xic1Xq5OyAuaWb2gQreNiaZFxeBaH8KfHtGoibNeOPI6YI2PuMDB7dzmGg4zaB7m6OCTjPYO8DOSWe4Kw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROMwLaGL2SDALP2W8veqTpxJteQpI2tUU4a4l1MLJg9GpofL2GS7KN975ekZZcD8WCBRpKP6M4IPlShiclmicYlCtoNPM7VPtHxs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPW6HZb1Ew58qJzWFW5CRL9YmcNneicTAyqDKhsJIIyUWib0xdkqKlJVoBJt6sGeXWoLMLpCv79f0rqD676jJxKwMR7Snb1wWgd8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPsW2cibINWBfY7Yut37q5oZTzYRia4e3jOzEoM3IdDiaHibxHHc6l8KtKzaTicIYhdqHxBia01HSYibhKevBico6u5tneYv4EKFggTKhc/640?wx_fmt=png&from=appmsg
