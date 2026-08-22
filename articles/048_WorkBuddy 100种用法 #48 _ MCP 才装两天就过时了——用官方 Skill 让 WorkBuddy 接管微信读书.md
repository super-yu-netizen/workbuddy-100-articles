# WorkBuddy 100种用法 #48 | MCP 才装两天就过时了——用官方 Skill 让 WorkBuddy 接管微信读书

- 合集序号：48
- 公众号：我与ai的那些事
- 发布日期：2026-05-17
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329021&idx=1&sn=e9ab96063761d98b02861cf7af1f80cb&chksm=883033fabf47baeca05a672f6a754341759e725402fbcab5e908b94cad0388f1256ad32a1b3b#rd
- 正文字数：3963
- 正文图片：11

## 摘要

前天刚装微信读书MCP，两天后官方Skill就来了。API Key一键获取不用cookie，8大能力比MCP多一倍，WorkBuddy接管微信读书终于不用折腾了。

## 正文

前几天这篇WorkBuddy 100种用法 #45 | 折腾半天，终于让 AI 翻开了我的微信读书刚折腾完微信读书 MCP，写了一整篇踩坑记录——cookie 过期、网站打不开、配置完还要手动信任。

没想到两天后，微信读书自己把 Skill 开放了。

直接开干。

我打开 WorkBuddy，问了一句：

“

微信读书现在有skill了吗？

WorkBuddy 回我：没有官方 Skill，但你可以用 MCP 方式接入。

跟两天前一样的答案。

我不信！

“

你去微信读书官网搜索看看，到底有没有

WorkBuddy 去搜了。

搜完回来，语气变了——

“

微信读书确实在 2025年5月16日 发布了官方 Agent Skill，版本 1.0.3。

好家伙，刚发布的。

WorkBuddy 给我解释了一波 Skill 和 MCP 的区别：

对比

MCP

Skill

认证方式

Cookie（会过期）

API Key（长期有效）

安装方式

npm 全局安装 + 手动配置 mcp.json

下载 zip 解压到 skills 目录

生态定位

通用工具协议

专为 AI Agent 设计

覆盖能力

4 个工具（书架/搜索/笔记/书评）

8 大模块（多出搜索/统计/推荐等）

简单说：MCP 是通用接口，谁都能做；Skill 是微信读书官方下场，专为 AI Agent 优化。

最关键的一点——不需要 cookie 了。API Key 绑定用户身份，不会过期，不用每次登录重新拿。

“

安装：官方方法 vs 野路子

我让 WorkBuddy 装：

“

好，你帮我安装下，他给我瞎安装，因为技能仓库有很多不名skill

然后又补了一句：

“

你安装这个skill要去官网查看如何安装

WorkBuddy 先试了官方推荐的方式：

npx skills add jerlinn/jerlin-weread -g -y

结果卡住了，等了好几分钟没有任何输出，超时了。

“

WorkBuddy 换了个思路：直接从官方 CDN 下载 zip 包。

curl -L -o weread-skills.zip https://cdn.weread.qq.com/skills/weread-skills.zip

下载完解压，把文件手动拷到 ~/.workbuddy/skills/weread/ 目录。

9 个 Markdown 文件，清清爽爽：

文件

用途

SKILL.md

总入口 + 接口规范

search.md

书城搜索（书籍/网文/有声书/作者/全文/书单/公众号/文章）

shelf.md

书架管理

book.md

书籍详情/章节目录/阅读进度

notes.md

笔记/划线/书签

review.md

书评

readdata.md

阅读统计（时长/天数/偏好/排行）

discover.md

个性化推荐/相似推荐

profile.md

用户画像

“

配置 API Key：官网一键获取

装完 Skill，要配 API Key 才能用。

跟 MCP 那次不一样——上次是让我去 Chrome 里翻 cookie，翻完还过期了。

这次直接去微信读书 Skill 官网拿，官网地址：https://weread.qq.com/r/weread-skills。

打开官网，第一眼就看到六个能力模块：

-
查阅书架——浏览你的个人书架

-
书籍搜索——在书城搜任意书籍

-
阅读统计——时长、天数、偏好分析

-
书籍详情——章节目录、阅读进度

-
笔记和划线——查看个人划线和想法

-
推荐好书——个性化推荐或相似推荐

然后点「快速配置」：

进入配置页，分两步：

第1步：复制 Skill 安装指令

显示的就是下载 zip 包的命令：

下载 https://cdn.weread.qq.com/skills/weread-skills.zip 安装 skill

第2步：获取 API Key

API Key 用于连接你的微信读书账号，数据仅你可见。

点「获取 API Key」按钮，直接生成专属 Key：

Key 生成成功，显示 wrk-NVbX··············dgAA，下面有「复制 Key」按钮：

注意下面的小字——创建于 2026-05-17，尚未使用。全新的 Key。

我点「复制 Key」，然后把 Key 发给 WorkBuddy：

“

wrk-NVbXuyyHTDaMjpfT5UbjdFAA

WorkBuddy 收到后，把它写进了 ~/.zshrc：

export WEREAD_API_KEY="wrk-NVbXuyyHTDaMjpfT5UbjdgAA"

然后验证了一下——直接调接口查书架：

curl -X POST "https://i.weread.qq.com/api/agent/gateway" \
-H "Authorization: Bearer $WEREAD_API_KEY" \
-H "Content-Type: application/json" \
-d '{"api_name": "/shelf/sync", "skill_version": "1.0.3"}'

秒回。

53 条数据——52 本电子书 + 1 个文章合集。

跟上次 MCP 拿到的数据一致，但这次没有 cookie 过期，没有认证失败，没有手动信任。

“

推荐几本书

配好了，我直接用：

“

推荐几本书给我

WorkBuddy 这时候犯了个错——它没加载 Skill，而是自己写 Python 脚本去调 API 了。

虽然也能用，但这不就失去装 Skill 的意义了吗？

我说：

“

你不是安装了微信读书skill吗？直接使用skill不行吗？为啥还用python调取

WorkBuddy 立刻纠正，加载了微信读书 Skill，按 Skill 文档里的规范调了推荐接口。

12 本书推荐回来，还带 deep link，点击直接跳微信读书 APP：

#

书名

作者

推荐理由

链接

1

《金钱心理学》

摩根·豪泽尔

财富不是智商，是行为

阅读[1]

2

《定位：争夺用户心智的战争》

特劳特

经典商业战略

阅读[2]

3

《卡片笔记写作法》

阿伦斯

知识管理的底层逻辑

阅读[3]

...

...

...

...

...

“

8 大能力，比 MCP 多了一倍

我接着问：

“

微信读书的skill还有什么能力？在我看下

WorkBuddy 把所有能力模块列了一遍：

模块

你可以这样说

核心接口

搜索书籍

"帮我搜一下三体"

/store/search
（书籍/网文/有声书/作者/全文/书单/公众号/文章）

书籍信息

"这本书有多少章""我读到哪了"

/book/info
+ /book/chapterinfo + /book/getprogress

书架管理

"看看我的书架"

/shelf/sync

阅读统计

"我这个月读了多久""今年读了几本书"

/readdata/summary
+ /readdata/detail

笔记划线

"看看我在三体里的笔记"

/user/notebooks
+ /book/noteCount

章节热门划线

"这章有什么热门划线"

/book/chapterBestHighlights

书籍点评

"三体这本书有什么点评？"

/book/review
+ /book/reviewByCategory

推荐好书

"给我推荐几本书"

/book/recommend
+ /book/similar

对比 MCP 的 4 个工具，Skill 多了：

-
搜索——书城全品类搜索（书籍/网文/有声书/公众号文章等 8 种类型）

-
阅读统计——时长、天数、偏好、排行榜（按周/月/年）

-
个性化推荐——基于你的阅读数据推荐

-
章节热门划线——看别人在哪些句子下面划了线

这四样 MCP 都没有。

“

Skill vs MCP：我的真实体验

装完 Skill 之后回头看 MCP，最大的感受就两个字：省心。

MCP

Skill

安装

npm install + 配 mcp.json + 重启 + 手动信任

下载 zip 解压到 skills 目录

认证

复制 cookie，会过期，过期要重新登录拿

一个 API Key，不会过期

调试

cookie 过期报 -201，排查半天

API Key 写进环境变量就行

能力

4 个工具

8 大模块

维护

社区维护

微信读书官方维护

上篇文章我踩了三个坑：cookie 过期、CookieCloud 网站打不开、MCP 配置完要手动信任。

这次一个坑都没踩。

唯一的小插曲是 npx skills add 卡住了，换成手动下载 zip 就好了。

安装微信读书 Skill：完整步骤

如果你也想装，照着来：

1. 下载 Skill

curl -L -o weread-skills.zip https://cdn.weread.qq.com/skills/weread-skills.zip

2. 解压到 Skills 目录

unzip weread-skills.zip -d ~/.workbuddy/skills/weread/

3. 配置 API Key

在 ~/.zshrc 里加上：

export WEREAD_API_KEY="wrk-你的key"

然后 source ~/.zshrc。

4. 验证

重启 WorkBuddy，让它帮你查一下书架，能返回数据就说明配好了。

装完之后，你可以直接问 WorkBuddy：

“

帮我搜一下三体 我这个月读了多久书 给我推荐几本书 看看我在《精进》里的笔记

全部一句话搞定。

从 MCP 到 Skill，微信读书这波更新确实让人省心。不用再折腾 cookie，不用手动信任，API Key 一配就完事。

这篇 WorkBuddy 100种用法 #45 | 折腾半天，终于让 AI 翻开了我的微信读书 我说"MCP 的意义在于让 AI 从只会聊天变成能操作你各种服务的助手"。现在 Skill 把这条路走得更远了——不只是能操作，而是官方下场优化，让操作更顺滑。

你装了微信读书 Skill 了吗？还有什么想连的服务？评论区聊聊。

这是WorkBuddy 100 种用法第48篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #微信读书 #Skill #API #AI工具 #读书 #书架 #推荐 #效率工具 #AI助手

引用链接

[1]阅读: weread://reading?bId=3300202570

[2]阅读: weread://reading?bId=3300201945

[3]阅读: weread://reading?bId=3300201731

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPXIMHmmJLcyOMZOzMgiafpVmhriaTLfc3Bj7dqWTFeD7Xfalwia03uKhKLYumx0TKARnh9oMGah1cCR5dxjGhhbvWSNJYBwjmaAw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNUUZzEicDDQDhmbCkSejgib5rwARh656klXMT5PiboBlyymC19a5MjR96e3iaOsNFNgJ44QXyaeLmlECXJDq2CK1Y8BEHGVgyaYMA/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRO8hETIRwmjw4HRfsFrJxCUgs3zVqz64gu8TX47d19ia1EWdBa9fDYcSboq4t6I4EDmrQ4x4P9iavG3fgSOYFjIBJETj7xfM4E4g/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMXtMfOYUOe07yYoK6p2wmykYH5hSj94taPT1J2OE0ic41f7lTXs3MW4iabsicADqSEkujzrdJY0iaIGXnU8XQ4TYrqpVibLvkQIAZE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMgdCYTkoWftwfxs3643JZBg1wLW8YxW8qMviaOmUCtZ4xLMsT0IWImBTaQMO3jgrZ52WP38ankJlr4yZzz2W7klkicia0Nh97j2Y/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNmAxI8Tas9EqTmbwcrF8lP3KffHXRTfXxZBPjOapgnN7W0DbVc3XW3Iyiak0kRmqwib0wVbcb5CHHyn4DI4hhrawpAjnXGXGbfA/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRPFXDAzcndxicTJzUSFic0icFLTtIHCJ9dtVNERDyeIdLAN4L6cdLIDJYJ76sr7Xr6LPvwzhMTDwc9nnjOnoAVaRtXFLgqaEjb0Bw/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNje2HWmicrK44nN3Jib1meTPeEcjwSsmMyTQszN8EsIAD4l15MwSOHwU3pkAnZibVGY06UbX1ZDDC7tJUx6iapX7zLv755Kmab150/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPPicQptib6fbQVKib0RfOicYFIOTrOqpSCRYjvKtjJvLuHbTa9awWBz6c9NI5EF88fA9NuYnpZNpQ2BU7dicCKJSQ6ibHRjr7iapHsZ8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNianIZB1ZM0HJPbPok2RI4zYSenEjrsJOXEsGib3anMaPLUbxpsVTPZxgDvMAplHib5nJG0ibIcB6YZhjt50UK3icXsECzZ9181QKs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRP5nIdtxGfD6mWMILCqic4PEPibyyqC5uEibBmFPqZvD6XKKN010nCD4UFHFkSDmlySS5mDS7Is8H1GQErQ72ficiaH6oJMAstdPTHs/640?wx_fmt=png&from=appmsg
