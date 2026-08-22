# WorkBuddy 100种用法 #46 | 发现个实时航班模块，顺手做了个页面，使用EdgeOne部署到了线上

- 合集序号：46
- 公众号：我与ai的那些事
- 发布日期：2026-05-15
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328985&idx=1&sn=d32a78c491061b3a430fbda972e6e838&chksm=883033debf47bac840f65f3676b94e5dc38862a2275ce96ea18ed0a56d49a7af18d85f8b85e3#rd
- 正文字数：2271
- 正文图片：7

## 摘要

发现WorkBuddy有个实时航班模块，直接用它查了西宁、北京、上海上空的航班数据，生成了一个深色航空雷达风格的HTML页面，还尝试用EdgeOne Pages连接器部署到网上——虽然连接器连败6次，最后手动拖上去成功上线了。

## 正文

昨天看到 WorkBuddy 的【探索】列表里，有一个叫"实时航班追踪"的模块。

我的第一反应是：这玩意能干嘛？然后顺手点了进去，根据他的模板改了下，直接给 WorkBuddy 下了一个指令：

“

帮我查一下西宁上空现在正在飞行的所有航班，显示呼号、来源国、飞行高度、速度和航向，并对比北京和上海的空中交通繁忙程度。结果生成html格式，并使用品牌设计风格专家设计好看点，帮我把最终HTML页面部署到EdgeOne Pages

对，一次性把需求全说完了。

WorkBuddy 先加载了航班追踪技能，又去加载"品牌设计风格专家"技能——结果这个技能没装上，报了个错。

没关系，WorkBuddy 说自己按高质量设计标准来做。

然后它就开始干活了。

“

WorkBuddy 用的是 OpenSky Network 的 ADS-B 数据接口，这个接口是免费的，不需要 API Key，数据来自全球的 ADS-B 接收器。

它先给三个城市（西宁、北京、上海）分别设了经纬度范围去查数据。

结果回来一看：

西宁——0 架航班。 北京——0 架航班。 上海——0 架航班。

全部为空。

我当时也有点懵：中国天空上不可能一架飞机都没有吧？

“

WorkBuddy 没有放弃，它分析了一下，觉得可能是查询范围太小了，先验证一下 API 本身是不是正常的。

它查了一下欧洲区域（瑞士上空）——336 架航班，数据哗哗的。

API 没问题，中国区域就是没数据。

然后它把范围扩大到整个中国全境（东经73度到135度）——528 架航班。

但是仔细一看，这些航班大部分在印度上空（边界区域），东经100度以东有 316 架，主要分布在台湾海峡、东海、日韩航线上。

结论很明确：OpenSky Network 在中国大陆内陆没有 ADS-B 接收器覆盖，所以西宁和北京上空的飞机根本探测不到。

这就是开源数据的局限性——覆盖率取决于有没有人装接收器。

“

数据虽然覆盖有限，但 WorkBuddy 没停下，它把这 316 架航班全部拿过来，按距离三个城市分别统计了不同半径内的航班数量：

-
西宁：100km 内 0 架 | 300km 内 0 架 | 500km 内 0 架

-
北京：100km 内 0 架 | 300km 内 0 架 | 500km 内 0 架

-
上海：100km 内 1 架 | 300km 内 2 架 | 500km 内 6 架

上海附近好歹有 6 架。

然后它用这些数据，生成了一个深色航空雷达主题的 HTML 页面。

页面内容包括：

-
四个统计卡片（总航班数、平均高度、平均速度、数据源）

-
三个城市对比卡片（带 100/300/500km 多半径可视化条形图）

-
50 架航班的详细列表（呼号、来源国国旗、高度条、速度、航向箭头、坐标）

-
覆盖范围说明

设计风格很到位，深色背景、橙色主色调、JetBrains Mono 等宽字体，有那种航空管制中心雷达屏幕的感觉。

“

页面做好了，接下来是部署环节。

WorkBuddy 左下角的连接器面板里，EdgeOne Pages 显示的是 connected（已连接）状态。

WorkBuddy 调用了 deploy_folder 工具，传了三个参数：

参数

值

builtFolderPath

flights-radar 文件夹路径

workspacePath

工作区路径

projectType

static

第一次调用——超时了。

第二次——还是超时。

我让 WorkBuddy 再试，第三次返回了一个新的错误：API error: undefined。

没超时了，但 API 报错了。

“

我让 WorkBuddy 再试，第四次——超时。 第五次——API error: undefined。 第六次——又是超时。

连续六次，不是超时就是 API 报错。

我当时跟 WorkBuddy 说：连好了，你帮我再试一次。

结果还是一样。

WorkBuddy 分析了一下：MCP 通道能通（偶尔不超时），但 EdgeOne Pages 的后端 API 本身有问题。

然后我手动打开了 EdgeOne Pages 的管理后台，把这个 flights-radar 文件夹直接拖上去上传了。

秒传，成功了。

线上地址：https://flights-radar-gvy19xppwv.edgeone.cool/[1]

“

回顾一下整个流程

从发现技能到页面上线，中间经历了这些：

-
发现"实时航班追踪"技能，提出需求

-
WorkBuddy 加载技能失败一个，自动降级处理

-
查航班数据——中国内陆没有 ADS-B 覆盖，数据为空

-
扩大范围找到 316 架航班，做了三城市对比统计

-
生成深色航空主题 HTML 页面

-
尝试用 EdgeOne Pages 连接器部署——失败了 6 次

-
手动拖拽上传到 EdgeOne Pages——成功

整个过程大概一个多小时，大部分时间花在了部署这个环节上。

两个收获

第一，WorkBuddy 的技能生态确实有意思。

一个"实时航班追踪"技能，就能直接调用全球航班数据 API，再加上 HTML 生成能力，做一个雷达页面出来。不需要写代码，自然语言描述需求就行。

第二，连接器这个东西，能用但还没到完全可靠的程度。

EdgeOne Pages 连接器显示 connected，但实际调 API 连续失败了 6 次。最后还是手动拖上去的。连接器的体验还有优化空间。

线上效果你可以直接打开看：

https://flights-radar-gvy19xppwv.edgeone.cool/[2]

深色主题，航空风格，316 架航班实时数据，还挺好看的。

你有没有用过类似的实时数据追踪工具？评论区聊聊。

这是WorkBuddy 100 种用法第45篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #航班追踪 #实时数据 #EdgeOne #部署 #航空 #雷达 #HTML #技能 #AI工具

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROiaI3ORQI00sG4GKdqiaowr3FNh4S3unmgp9dGibM3yRKLnlEHGCAS5d0icddrRGIjk7hlXJARMDAOWsaPonriaOjgqQfvkxELUicQc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMviahOAQiaTTsEXyw3dldibVIiaib3yDYIGBlibDTdFqoMCtJ8BoIqxlUbn7ibkQeuujBYjY0xg2ib8YlMY8GU0DmM58s1ib93VGw21t84/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMnwQNxPpcj7CMDA9xNn25HE52zoaIN2XdvL7Idk1xWJDswkIVIw3sbiaibpl9mibR3S6ra2DwM4mWJWK7wIRq2Elx6A37KcO1FUY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROSllIs1mDxP7hq7twGEo3BMxVZaYalHu6YYnW7qGFh9fMRQ7IntGNX0Yl1ePG8NvAgbuz32WYYTvVPZSvKKTEK40ACZ642iaD0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROD5C4eQPrQYribicqaZu6XPHoO21mibyNgVHtwxBIJ3FRUfcqU82LoaYp4icwByiaLVDNVbGZ4pS4KyODxhZIlx7f49eIicAWtUhbQE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPqgmxJmfbMlt4GeKN8BwHaXfIkqTsqOUSo6MKJCIywwuChgfq3licjYCde1gv6Uh6iaCKYCu9vtTI6FWibYADfYH6cpBMC6sCpfc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNhjfiaJAGeG1bQPIIwgP0vicaoiaYBJmQ7meVgTtvzFHiclkkvkFIwVRKiaVQg9a4D0unS9fqPgvlT3nCfNpibuhMkgl6vZAvvUPbWk/640?wx_fmt=png&from=appmsg
