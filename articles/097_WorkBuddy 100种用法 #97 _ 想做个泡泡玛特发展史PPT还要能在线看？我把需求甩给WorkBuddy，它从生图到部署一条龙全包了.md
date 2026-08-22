# WorkBuddy 100种用法 #97 | 想做个泡泡玛特发展史PPT还要能在线看？我把需求甩给WorkBuddy，它从生图到部署一条龙全包了

- 合集序号：97
- 公众号：我与ai的那些事
- 发布日期：2026-07-06
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330140&idx=1&sn=9af3a24cbf4533f019f4c56a17ca7671&chksm=8830375bbf47be4d609e79d082157646965c86337d04b063d92897b2608227f5b15a3d01a8a1#rd
- 正文字数：2012
- 正文图片：9

## 摘要

想要每页一个IP的泡泡玛特发展史PPT？把需求甩给 WorkBuddy：混元生图出9张无水印角色图，13页卡通风排版，导出PPTX并部署上线，一条龙。

## 正文

前两天朋友丢过来一句话："能不能帮我搞个泡泡玛特发展史的小PPT，要好看点，每页都得有个IP角色，最好还能发链接让我在线翻。"

我脑子第一反应：13页PPT、每页一个潮玩IP、还得卡通风、还得能部署上线——这搁以前我得先找一圈版权图、再在PPT里一张张排版、最后还得租个服务器或者用某网盘生成分享。想想就头大。

然后我想起 WorkBuddy。我把需求原样甩给它，没抱太大希望，结果它一条龙给我干完了。

一、提需求：一句话甩过去

我没收拾需求文档，也没画原型图。就发了这一段：

"帮我做一个popmart发展史ppt，每一页都要有一个ip"

WorkBuddy 带着需求直接开了干，没让我补第二个字。

二、第一轮：先搭骨架，定风格

我："等等，你说的前端？我就要个PPT啊。"

WorkBuddy："网页PPT比传统PPT好改、好部署，最后也能一键导出成 .pptx 文件，两不耽误。你先别管技术，看效果。"

它用的是 Vite 那套网页PPT方案，先给我把整个前端脚手架搭起来，然后定了全局风格：粉 #FF4D8D、紫 #7C4DFF、黄 #FFC400 三色打底，圆润卡通风。

我没再插嘴，等它出活。

三、第二轮：9张IP图，现画还没水印

最难的是图。泡泡玛特的IP我不能乱用官方版权图，WorkBuddy 直接调了混元生图（带了个"无水印"技能，自动关掉水印），按每个角色的特征写了提示词，一口气生成了 9 张 1024×1024 的卡通图：

-
• LABUBU（尖耳獠牙那小子）—— 封面、2018、2023、结尾都用它

-
• MOLLY（撅嘴湖绿眼）—— 2016 元年

-
• DIMOO —— 2017

-
• SKULLPANDA —— 2019

-
• HIRONO 小野 —— 2020 上市那年

-
• PUCKY —— 2021–22 全球扩张

-
• CRYBABY 哭娃 —— 2024 破百亿

-
• Sonny Angel —— 2010–2015 起步期

-
• 一张 IP 总览网格图 —— 目录页和总览页用

我后来还专门让 WorkBuddy 核对过，9 张图 MD5 全不一样，不是同一张图复用的——每页 IP 视觉确实是独立的。

四、第三轮：13页内容，每页一个IP

骨架和图都有了，WorkBuddy 开始往里填内容，严格按"每页一个IP"来排：

页

主题

主视觉IP

1

封面

LABUBU

2

目录

IP 网格

3

2010–2015 起步

Sonny Angel

4

2016 Molly 元年

MOLLY

5

2017 DIMOO

DIMOO

6

2018 THE MONSTERS

LABUBU

7

2019 SKULLPANDA

SKULLPANDA

8

2020 上市

HIRONO

9

2021–22 全球扩张

PUCKY

10

2023 现象级

LABUBU

11

2024 破百亿

CRYBABY

12

IP 总览

网格

13

结尾

LABUBU

五、第四轮：导出PPTX + 部署上线

内容定了我又提一嘴："这个生成的ppt是个网页是吧，你帮我把这个部署到线上我看看。"

WorkBuddy 两步搞定：

-
1. 用内置导出，把我那份网页PPT压成了一个 41MB 的 presentation.pptx（13页，带图，能直接编辑）；

-
2. 用 CloudStudio 部署工具，把网页版推上线，给我返回了一个分享链接。

-

线上地址： https://b54a568fbd7b4dfdb815310858de726d.app.codebuddy.work

在浏览器里点开那个链接，← → 就能翻页，跟本地一模一样。

回过头看这轮对话

我做的

WorkBuddy 做的

提需求（13页、每页一个IP、卡通风）

搭前端PPT脚手架、定粉紫黄配色

中途插嘴确认方向

调混元生图技能现画 9 张无水印IP图

最后看效果、补一句"要能发链接"

写 13 页内容、按时间线排好每页IP

导出 41MB 可编辑 .pptx

部署到 CloudStudio、生成在线分享链接

说白了，我全程就动了嘴和眼睛。

我的几点感受

① 一句话需求就能出成品。从"生图 → 排版 → 导出 → 部署"它全包了，我不需要在五个工具之间来回切。

② 无水印生图技能是真省心。不用自己去抠版权图、不用后期去水印，直接拿到干净的角色图。

③ 部署一条龙，零服务器知识。给个链接就能让朋友在线翻，不用我自己搞托管。

④ "每页一个IP"这种硬要求它真做到了，不是模板套话——我核对过 9 张图确实各不相同。

最后

这轮下来，我搞清楚了三件事：

-
1. WorkBuddy 做 PPT 不是"生成几张图"，而是一套「前端网页 + AI生图 + 导出 + 部署」的完整流水线；

-
2. 想要干净的角色图，用「混元生图 + 无水印技能」比到处找图稳得多；

-
3. 做完想让人看，直接 CloudStudio 部署拿分享链接，比传网盘、发文件体面多了。

说句实话：那些 IP 图是 AI 按角色特征生成的卡通再创作版，做科普演示够用；真要商用，还是得用泡泡玛特正版授权素材。

这是WorkBuddy 100种用法第97篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #泡泡玛特 #PPT制作 #AI生图 #AI部署 #效率工具

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPgUz3ZibPfyx0nFBJCiaDNjSZD0XxN7zyQm6f6jnf6Riah4D19iapRuj9eMVoyN8bMBjgytZkKEicqZfAQ4wWCav8xSbicyZ1DPO90I/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMncGLf5rEAedsCGpck2eoTA1YYNqg2gGfKPT5ia9vy0rwzEWiclaH0lvCYC8BV0WB5yjpO8uNfa2mEgtia25ypENH86M7ts1oBuQ/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRML3RhkYYKEdI3Zmib2ib87EpKKSzd81jcsE1tibkwD8gOUgSWqfDdtQstF2CB0U1RoWh5sIXVsT9TJhhxZPzibGC9fDv1LW85GUn4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRO50LaQ9AnRHvqyEK2wvF1GTSdmH7jkz2V7hKP8VaXArzYKUc7ygAfcGoZO5k5GFZibWibYWAd7351muIlaKlvYrdvsezYDAyY8o/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNjuKWmqdictlWNFicPm14u5l36aaGDW1XzgZldO8o8YOmR5JGwGayYVObO5ccx4L43S12x7tt56A9egWMWQD9HByu4X0EwvzYMs/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMkSGvGNcndYZkTTGG4ZAEAUUOq3Za3JT8AjDyrnyHWHCIqnAiab1icJBcyy6g0uj4vBWbVXcNSYXcSjCV1CV7doYic0ia8pLmefdU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNHTFYPwOd5QyFgZ6ib3ARS38zEUnN6ialzibxDJYDQMsIyCOpxmjiaGuxmURFtdxEmJeMUbmbQTA8IgTenPteicJwXzFicOoFwmjXN0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM9jS9kPAIwgp9gwyI3m3J5b6kxRiaFSdib7AVNPGjxF69RtGs4bcDNqDxOaTAde9RCODexmQ0IH9yYlnRNpCVgW7bY19wrLqVm0/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMfLgfX3ohUEr1qvo3ic3WA1X4IAibZ6FSPMXUv192rvfptBhGl8ia5Vqhiapriblmol0pPPNz8GXpRb0MDKjQmiagBwPcHXpB2bN26A/640?wx_fmt=png&from=appmsg
