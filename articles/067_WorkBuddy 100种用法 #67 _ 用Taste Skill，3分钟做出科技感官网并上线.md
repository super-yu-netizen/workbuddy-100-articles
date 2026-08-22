# WorkBuddy 100种用法 #67 | 用Taste Skill，3分钟做出科技感官网并上线

- 合集序号：67
- 公众号：我与ai的那些事
- 发布日期：2026-06-06
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329376&idx=1&sn=92f0edb69b92496a7bac844141347cf8&chksm=88303467bf47bd71af1c3ff47c489ab715b53312485f5e909ea7bd90d84f3b01fbb125af0599#rd
- 正文字数：1959
- 正文图片：7

## 摘要

发现 GitHub 17k+ Star 的 Taste Skill，让 AI 告别模板味。我用它为研智科技做了暗黑科技风官网，修复移动端适配后一键部署上线。

## 正文

前几天逛 GitHub，看到一个叫 Taste Skill 的项目，17k+ Star，专门教 AI 编程助手告别"模板味"。

我心里一动——正好有个朋友想做企业官网，不如拿来试试？

Taste Skill 是什么

简单说，Taste Skill 是一套纯文本规则文件（SKILL.md），不是代码，不联网，就是告诉 AI："别再生成那种千篇一律的模板页面了。"

它里面有 13 个子技能：极简风、工业风、品牌系统、图片转代码、老站翻新……覆盖了大部分设计方向。

关键是它的核心方法论——Design Read：先读懂你的需求，推断设计方向，再选对应的设计系统输出。不是拿到需求就开写，是先"读懂"再动手。

我直接跟 WorkBuddy 说：帮我安装 Taste Skill。

它从 GitHub clone 下来，把 13 个子技能全部装到了 ~/.workbuddy/skills/ 目录。整个过程不到一分钟。

第一个版本：差点意思

装好之后，我给 WorkBuddy 提了需求：

公司名叫「研智科技网络公司」，做成人高考培训、AI培训、招聘会策划、企业培训。页面要有科技感。

它很快生成了一版。我打开一看——

嗯……能看，但不够看。配色偏素，排版中规中矩，科技感？几乎没有。

这就是典型的"模板输出"——结构完整，设计为零。

第二个版本：暗黑科技风，对味了

我直接说：这个没有设计感，也没有科技感，换个方向。

WorkBuddy 读取了 Taste Skill 的规则，重新做了 Design Read，这回选了暗黑科技风的方向：

-
深色背景 #0a0f1a，像赛博朋克的城市夜空

-
青色光晕 #06b6d4 作为主色调，像终端屏幕的光

-
粒子网络背景，用 Canvas 画的动态连线粒子，像科幻片里的数据流

-
扫描线效果，一条青色光线从上到下缓缓扫过整个页面

-
Space Grotesk 字体，等宽风格的显示字体，代码味拉满

打开的一瞬间，感觉来了——这才是"研智科技"该有的样子。

四个业务板块用卡片呈现，鼠标 hover 有微动效；数据区域四列排开，有渐变分隔线；底部有联系方式和简洁 Footer。

部署：一波三折

页面做完了，得上线。我本来想部署到 Cloudflare Pages，绑自定义域名 kt.yaniw.com。

结果 wrangler 授权出了问题——OAuth token 权限不够，sandbox 环境又没法弹出浏览器完成授权。折腾了几轮，算了，换方案。

WorkBuddy 用 CloudStudio 一键部署，几分钟就拿到了线上地址：https://c7adaa3e5543449eb5de3e925be4d198.app.codebuddy.work

虽然没能绑上自定义域名，但页面本身已经完全在线了，手机电脑都能访问。

移动端适配：细节不能少

上线后我手机打开一看，问题来了——宽度溢出，右边多出一截，右上角的菜单按钮得横向滑动才能看到。

WorkBuddy 排查后发现三个坑：

-
绝对定位的装饰元素溢出：粒子光晕、渐变圆这些装饰元素用 position:absolute 定位，部分伸出视口外，父级没有 overflow:hidden

-
inline style 覆盖了 Tailwind 响应式类：手动写的 grid-template-columns 优先级比 Tailwind 的 md:grid-cols-2 高，导致移动端还维持桌面端的多列布局

-
HTML 属性重复：好几个元素写了两个 class= 或两个 style=，浏览器只认第一个，后面的响应式样式直接被忽略

修复方案：

-
给所有 section 加 overflow:hidden

-
删掉 inline 的 grid-template-columns，让 Tailwind 响应式类接管

-
合并重复的 HTML 属性

-
加了一套完整的 @media(max-width:768px) 样式

修完再打开，移动端效果出来了：

卡片从横排变竖排，字号自适应，导航收进汉堡菜单，一切刚刚好。

Taste Skill 的核心价值

回头看整个流程，Taste Skill 做的事情其实很简单——让 AI 在写代码之前先想设计。

普通流程：拿到需求 → 直接写代码 → 出来一个模板页 Taste 流程：拿到需求 → 读懂需求 → 推断设计方向 → 选择设计系统 → 再写代码

就多了一步"Design Read"，出来的东西完全不一样。

而且它不是固定风格的——极简、工业、赛博朋克、品牌定制，都可以。同一个需求，换个方向就是完全不同的设计语言。

这才是 AI 辅助设计该有的样子：不是替代设计师的审美，是让"不会设计但知道想要什么"的人，也能做出不丢人的页面。

这是 WorkBuddy 100种用法第67篇，持续日更，每篇都是真实场景。

关注我，一起探索 WorkBuddy 的更多玩法。

#WorkBuddy #TasteSkill #企业官网 #前端设计 #AI建站 #科技感设计 #CloudStudio #移动端适配 #100种用法 #AI工具

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNQ0icWpbOkfgLlYe2LDicrLmvGsNIOp9kvk5Vdiavdic3ElFf5O8qgltNJF9XtoiaGFw9lB3XQ5uoPvhUSpOzoTuiaG6VZ4zNJNSBRo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROUtBYaViascNjj6zqFIrd8JPHOdajRbRIChGTXCJzm3ibajvELOfAt5chicHPuunLouL3vAfIsWib24SPOZxBhmJCA3j3awuspnEc/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNqzvTJicIhqoxwPHvjiayHxcG3tMVGNZBU2rWRqYbBdjnyGIcq4iaV4ZQ9HicDmwcLqameL4h4H9jzGNQibyfBn9LYtX1W6e7rBRX4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROo68SOKQ7Eujk3NicOGxJhzkxCNhoww8MJ8Mwia944NNMib5joFwbMhQ1rH0rF7pY4iaYKTJn8bUq1DW1S3XUibk3PjeRljZOFnNcU/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNA5ibZkatcWZC2xbjEeNxAmadSNdiaI93rLjicMicgOVf3u7WapyfQr1trWCIA62EIib6OhKuplicPD0MDlicpNask0x9XMG2libWPbX4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNoBXPRNja72ibQrJLbv9Y3lhNDG7bRzEJHO5knboicOtJd8NA9jrozcibSf09koiacJuiaiavflKBN6KBvk5mx7DLjjpYr3icIuA6fias/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPicAy2RIUlj6se4HHN4R2298XaCsTRibufONHj0IwUdJKc5vatuImeGKO2cLsGIRRh9H4iamYX5LuNia8VHPqqlEtaCkuPXpEibzwY/640?wx_fmt=png&from=appmsg
