# WorkBuddy 100种用法 #83 | 我给公众号绑了个AI客服，零代码

- 合集序号：83
- 公众号：我与ai的那些事
- 发布日期：2026-06-22
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329877&idx=1&sn=cacf839dd734147fa477b341c7d3a335&chksm=88303652bf47bf448ae337d689ad47bace112ea9871e4599977fe2ce791b575121cf343728d7#rd
- 正文字数：2072
- 正文图片：12

## 摘要

给公众号加 AI 客服，不用写一行代码。IMA 知识库通过微信小程序跳转，10 分钟配置自定义菜单，读者点一下就能在你建的知识库里随便问。零成本，零运维。

## 正文

公众号的读者给你发消息，问"这个效果怎么"、"那个同步我为什么不行"、"上次你说的那个东西是什么来着"，你回不回？

我知道很多人不回。因为一天几百条消息，真的回不过来。

但用关键词自动回复吧，又太蠢了。设置一堆规则，结果读者问"多少钱"触发了一次，问"价格"触发不了，问"咋卖"又触发不了。

有没有办法，让公众号接入真正的 AI 客服？

有。而且零代码，十分钟。

偶然发现

前几天我研究 IMA 知识库的时候，注意到一个功能 — 知识库右侧有个「分享」按钮。

点开一看，除了复制链接，还有一个选项：「接入公众号」。

我第一反应是：直接接入？不是要通过服务器开发？

点进去看了一圈，发现 IMA 跟微信公众号的整合方式，比我想象的聪明多了。

它不是通过 API 调用（那个确实得写代码搭服务器），而是利用了微信小程序跳转。

说白了就是：在公众号菜单栏里放一个按钮，用户点一下，直接跳进 IMA 知识库小程序，在你指定的知识库里随便问。

整个过程，不需要写一行代码。

怎么搞

整个流程大概 10 分钟，拆成四步：

第一步：建一个共享知识库

打开 IMA 桌面端（或者手机端也行），把你想让读者问到的资料全丢进去 — FAQ 文档、价格表、产品说明、退货流程、联系方式。

然后点「共享」，让它公开可见。

比如我建了一个「WorkBuddy 100种用法」的知识库，里面放了我写过的所有文章：

第二步：拿到知识库 shareId

点右上角「分享」→「复制链接」，会得到一串地址。

我复制出来是这样的：

【ima知识库】WorkBuddy 100种用法
https://ima.qq.com/wiki/?shareId=090c36e38192aa26f03bd9e0d99c01a31...

记住这段 shareId，后面配置菜单的时候要用。

第三步：公众号关联 IMA 小程序

公众号后台 → 广告与服务 → 小程序管理 → 点击「关联小程序」：

管理员扫码授权：

搜索「IMA知识库」，找到之后点关联：

看到「关联成功」就对了：

注意：这一步需要有公众号管理员权限，不是管理员的话找人扫一下就行。

第四步：配置菜单栏

公众号后台 → 互动管理 → 自定义菜单 → 添加菜单。

先选「跳转小程序」，然后选「IMA知识库」：

关键一步：在「小程序路径」里，把第二步拿到的 shareId 拼进去。路径格式是：

pages/index/index?shareId=你的shareId

备用网页可以留空，不管它：

然后右下角点「保存并发布」：

确认发布：

就这些。完了。

效果咋样

来看看手机上的最终效果：

读者在公众号聊天界面底部，看到「AI客服」按钮 → 点一下 → 直接进入你自己的 IMA 知识库：

背后的模型是 DeepSeek，回答是基于你上传的资料生成的，不会胡编乱造。

举个例子，你上传了一份「产品价格表.pdf」，读者问"多少钱"：

-
如果是关键词自动回复，只能匹配到"多少钱"这三个字

-
但 AI 客服能从价格表里找出对应的产品价格，然后用正常的人话回答

而且不只是 FAQ — 你公众号写过的文章、产品手册、使用教程，全部都可以丢进去。读者问的问题如果在你文章里写过，AI 会自动找出来回复。

一个遗憾

唯一的遗憾：用户会跳出公众号聊天界面，进入小程序。

不是那种"在公众号对话框里直接对话"的体验。是"点按钮 → 跳小程序 → 在里面问"。

但说实话，进入小程序之后的体验，比公众号内对话好太多了。

因为小程序里有完整的聊天界面、上下文记忆、还支持多轮对话。公众号内的客服消息 API 很多限制 — 48 小时内才能主动发消息、每条消息还得验证 openid，挺麻烦的。

这个小程序方案，等于绕过了所有技术障碍。

这算不算 WorkBuddy 的用法

可能有人问：这跟 WorkBuddy 有啥关系？

有关系。

因为 IMA 知识库本身，在 WorkBuddy 里就是直接可用的。你可以在 WorkBuddy 里搜索知识库内容、上传文件到知识库、甚至让 WorkBuddy 帮你批量整理知识库。

而且在 WorkBuddy 里操作 IMA 知识库，比在 IMA 客户端里方便多了 — 不用翻文件夹、不用一个个点上传，直接说一句话就行。

比如：

"帮我把公众号最近 80 篇历史文章全部同步 IMA 知识库，文件名用文章标题。"

WorkBuddy 十几秒就搞定了。你自己去爬文章、复制粘贴、一个个创建笔记，得搞到天荒地老。

所以逻辑是这样的：

-
用 WorkBuddy 管理 IMA 知识库（批量导入内容、整理归类）

-
用 IMA 知识库连接公众号（菜单栏一键跳转）

-
读者用 AI 自助查询（再也不用来找你问重复问题）

三个环节，WorkBuddy 在第一环。

其实我觉得，公众号未来的标配，可能就是「AI 客服按钮」。

现在做公众号的人，不管是做内容的、还是做服务的，最大的痛点就是人工回复太费时间。但用户又确实有问题要问。

有了这种零成本的 AI 客服方案，以后不是你有没有的问题，是你不做就是在浪费用户耐心。

这是WorkBuddy 100种用法第83篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #IMA知识库 #公众号AI客服 #零代码 #AI客服 #微信小程序 #DeepSeek #公众号运营 #100种用法 #AI工具

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNb3Y3vWLwibDQn8NPjvmnmrlpYdfjfabricia6ozsGtxX3egQja1obuofGEnrYnLcI80WpxhH8d09NwAVyusKss1aVNwBViaVRNMY/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMExjg69RDw1n8jReBytam2pxqqJynGoa8OJCbbFRAUUWLbVjL99ichlGktQjEKe6Qrb1cGqpTTuEu99kn6P6bKjuo3YI4jRicR8/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROcGXswjEbCAscicSdjYicnB32Lc9ic1ibJz3ib0LLrN0LWCjfke0bY4khicQ8ZTjEjqiajOb1nonCk5l8WkW6jmodtDInPAibh7Zoep8w/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM5Enf0GdSZoAL3MWCTiajNmFzmEZW86hRI5LkEicbvKEHvx3aeqEMqVJpLvS1BjoNiarkDEFBy5CrhbDUGDAfZBXkh1vOA8bE8yo/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNIrqgULoQyy5iaeA7H98Mw6cmN2xahgHCeMr78YFUddVevsq7vUdWqKsZTz8TNaxia6AAGkdK1z17dlKdYOH9icd1gdQ2dpCiaUEY/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM6C0xGRmZctnGlGLn4HS5IIYGicw7aic7mxQFMf1KEwsDM0oWcNVQPtibAsTLicfDhrZhdSkfNRfbOpI5etO2hThVFQ65DqFibo7nc/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPM03bibZtZz37nDVGZckb93Nj3NBWS2B5RLQwzHbWwX9kuWiaf3gQuezYmMmIXEdMmqG5keh3TP8OrtOqWBpuEqEKdDllccrNDk/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROBzw00bKibCdibYL1ICsgYnM01iaClwEtZibJvzlA0sTbbWA016R9pQG8N07bTmSVhdxwPol3pFI0qlylHia4ibG1cuTJ980CGnsc3U/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPTx6GEKPReXfv7gvB5SvGDGUv45Zlb7xC0wCpuyv27cnwfXDAicibKAphWcC5jRXhUJ4lgwQ0HSeO1KVVXSiaLye6cBebIfa4pUU/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROgQP1YtoHB8TkuiauUStrJp3ZiaAh3X3Ngw5wGdwBeLOUvxW5c8nkYARFPms7eUFgfqebBibibJTicLCmujYt7ibM5LQDxtiaQ1OVL7A/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRPZ1ITLVqyMolMlkIPyq7wZPIsh54Edia3Sic6PYYibaehAheuQtcNvlLfSO6QUdq8y0BDKibGiaz10hMIquQcKib05nAgBL9J0RqrFU/640?wx_fmt=jpeg
- https://mmbiz.qpic.cn/sz_mmbiz_jpg/s516EMWvbRM9Xt1odDIia0B3NUYH8LKDgsPQUEHDJnspWBEHLDG6ytJ7JdW7Rd7ueKWGbAqibgP20uKHYZROu6fdLs2PjEKO60exj9PabN2Zw/640?wx_fmt=jpeg
