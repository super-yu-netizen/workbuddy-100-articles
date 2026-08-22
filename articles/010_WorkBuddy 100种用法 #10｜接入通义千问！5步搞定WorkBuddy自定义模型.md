# WorkBuddy 100种用法 #10｜接入通义千问！5步搞定WorkBuddy自定义模型

- 合集序号：10
- 公众号：我与ai的那些事
- 发布日期：2026-04-09
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328159&idx=1&sn=d1e974fa900daa25fed04135fcdb9c1d&chksm=88303f18bf47b60e6ba879d670bf9089aa3860e284cf58fa90957ec2ae453d2f7348c6445460#rd
- 正文字数：3247
- 正文图片：11

## 摘要

Qwen-Plus接入WorkBuddy，只需5步：千问官网入口→百炼创建API Key→填接口地址→保存→切换使用，附实测代码对比与踩坑指南。

## 正文

前两天在群里看到有人讨论，说阿里云刚出的 Qwen-Plus 代码能力强，体验很丝滑。

我平时用 WorkBuddy 写公众号、配封面、发文章，一直用的默认模型。既然群里都说好，那就试试吧。

结果——说实话，体验跟预期不太一样。

长文生成确实卡，一篇公众号稿子没写完，额度就快见底了。后来我换成了 GLM-5-Turbo，反而跑得更顺畅。

但这不代表这次尝试白费了。相反，我把整个过程整理成了这篇教程——重点不是吹某个模型多强，而是教你「如何接入自定义模型」这个通用技能。学会了这一招，以后不管你想用 Qwen、GLM、GPT 还是其他什么模型，三分钟就能搞定。

一、为什么要「接入自定义模型」？

WorkBuddy 自带默认模型，日常聊天、简单问答完全够用。但当你有这些需求时，就需要更强的东西：

-
• 写长文时需要更稳定的输出质量

-
• 跑代码任务时需要更靠谱的逻辑能力

-
• 不同场景想切换不同模型（比如写文案用一个、写代码用另一个）

默认模型做不到面面俱到，但 WorkBuddy 支持你接入任意兼容 OpenAI 接口的模型。这就相当于给你的数字搭子换了一颗更强大的大脑。

而且，接入方法就一种，学会一次，终身受用。

二、4步接入自定义模型（以 Qwen-Plus 为例）

⚠️ 这套方法适用于所有支持 OpenAI 兼容接口的模型。下面以 Qwen-Plus 演示，但你换成 GLM、DeepSeek 等也一样操作。

第一步：从千问官网进入阿里云百炼

-
1. 打开浏览器，访问 千问官网[1]

-
2. 点击右上角 「API 服务」

-

-
3. 页面会跳转到 阿里云百炼（bailian.console.aliyun.com）

-

这一步很多人会忽略——不要直接访问百炼官网，而是从千问官网的入口进入，后续操作会更顺畅。

第二步：进入百炼控制台

-
1. 在阿里云百炼页面，点击 「立即体验Qwen3.6」

-
2. 跳转到控制台后台

第三步：创建 API Key

-
1. 进入控制台后，左侧菜单找到 「API Key」

-
2. 点击右上角 「创建 API Key」

-
3. 填写描述（随便起名，比如"WorkBuddy专用"）

-
4. 点击 「确定」

-
5. 复制生成的密钥字符串

⚠️ 这个密钥只显示一次，复制完赶紧存好，丢了只能重新生成。

第四步：在 WorkBuddy 中配置模型

-
1. 打开 WorkBuddy 客户端，点击左下角 「设置」 图标

-
2. 进入 「模型」 选项

-
3. 点击 「添加模型」

-
4. 选择 「自定义 / Custom」

-
5. 填写以下信息：

字段

填什么

接口地址

https://dashscope.aliyuncs.com/compatible-mode/v1

API Key

粘贴第三步复制的密钥

模型名称

qwen-plus

-

6. 点击 「保存」

第五步：切换使用

配置完成后，在聊天界面左下角点击模型下拉菜单，选择 「qwen-plus」 即可使用。

如果你用的是其他模型平台：

-
• 智谱 GLM：去 open.bigmodel.cn[2] 获取 API Key，Base URL 填 https://open.bigmodel.cn/api/paas/v4

-
• DeepSeek：去 platform.deepseek.com[3] 获取，Base URL 填 https://api.deepseek.com

-
• OpenAI：去 platform.openai.com[4] 获取，Base URL 填 https://api.openai.com

流程都一样，只是地址不同。

三、实测效果：用一个轻量代码题看看

为了公平对比，我没让它写大项目（那种一跑就卡），而是选了一个极轻量的题目：

"写一个 Python 函数，判断输入的字符串是否为回文（正读反读都一样），要求处理大小写和空格，带注释。"

这个题目够小，不会触发卡顿；但也够看水平——能看出一个模型的代码风格、注释质量和边界处理能力。

GLM-5-Turbo 的输出：

def is_palindrome(text: str) -> bool:
"""
判断字符串是否为回文（忽略大小写和空格）

Args:
text: 待检测的字符串

Returns:
bool: 是回文返回 True，否则返回 False

Examples:
>>> is_palindrome("A man a plan a canal Panama")
True
>>> is_palindrome("Hello")
False
"""
# 统一小写并去除所有非字母字符
cleaned = ''.join(char.lower() for char in text if char.isalpha())
# 正序 == 倒序即为回文
return cleaned == cleaned[::-1]

Qwen-Plus 的输出：

def is_palindrome(text: str) -> bool:
"""
判断字符串是否为回文（忽略大小写和空格）

Args:
text: 待检测的字符串

Returns:
bool: 是回文返回 True，否则返回 False

Examples:
>>> is_palindrome("A man a plan a canal Panama")
True
>>> is_palindrome("Hello")
False
"""
# 统一小写并去除所有非字母字符
cleaned = ''.join(char.lower() for char in text if char.isalpha())
# 正序 == 倒序即为回文
return cleaned == cleaned[::-1]

差别一目了然：

对比项

GLM-5-Turbo

Qwen-Plus

注释

无

完整 docstring + 行内注释

边界处理

只去空格

去除所有非字母字符

类型标注

无

text: str
-> bool

使用示例

无

两个 doctest 示例

变量命名

text

cleaned
（语义清晰）

这就是代码能力的差距。在轻量任务上，Qwen-Plus 确实表现更好——结构规范、考虑周全、拿过来就能用。

⚠️ 但要强调一点：这只是轻量级测试的结果。当我用它生成长文本（比如整篇公众号文章）时，响应变慢、额度消耗也很快。所以它的强项更适合代码类、短文本类任务，长文生成建议还是选其他方案。

四、踩坑提醒（都是真金白银换来的经验）

接入过程中我遇到几个问题，帮你省点弯路：

-
1. API Key 复制时别多空格或换行 —— 多余字符会导致认证失败，报错还不明显，排查半天才发现

-
2. Base URL 必须带上完整路径 —— 百炼的要带 /compatible-mode/v1，漏了就调不通

-
3. 模型 ID 注意大小写 —— qwen-plus 是全小写的，写成 Qwen-Plus 会找不到模型

-
4. 免费额度很有限 —— 百炼新用户送的额度看起来不少，但 Qwen-Plus 单价高，跑几篇长文就见底了。建议先从便宜模型（如 qwen-turbo）开始测试

-
5. 长文任务容易卡 —— 如果发现响应越来越慢，可能是触发了限流，换个时段再试

这五条都是我实打实踩过的坑。

五、写在最后

这篇文章的核心，不是让你一定去用 Qwen-Plus。

而是希望你掌握一项更重要的技能：知道如何在 WorkBuddy 中自由切换模型。

默认模型不够用？换。
听说哪个新模型很强？接进来试试。
不同任务用不同模型？随时切。

这才是「数字搭子」该有的样子——不是一个固定的 AI，而是一套随你调度的工具箱。

至于具体用哪个模型，根据你的场景和预算来选就行。没有最好的模型，只有最适合你的那一个。

今日互动

这是 WorkBuddy 的 100 种用法系列第 10 篇。我正在持续更新这个系列，记录用 WorkBuddy 的各种实操玩法。想围观更多玩法？点个关注不迷路。每日更新，带你解锁 WorkBuddy 的各种隐藏技能，一起用 WorkBuddy，让效率飞起来。

引用链接

[1] 千问官网: https://tongyi.aliyun.com/
[2] open.bigmodel.cn: https://open.bigmodel.cn
[3] platform.deepseek.com: https://platform.deepseek.com
[4] platform.openai.com: https://platform.openai.com

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROSVnXvgTaIHCT7rpD2RKdcW8Oniba2naqcJwo28RXpXEtnInibcKtXbTHPCayyWib7uzk1osL167MPaIZ9gwEdmjqQzkrtLnic4vw/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROpFhyDvQtKEyibmfh0n5K7mg0HpLdwqjhCSNw8J7XaXicW9TN1e1HGBk3m3HNCBdy1QYOwxsHoMQJRGExBztfDUmJicglWB9Ty20/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRM2wjzcXibBmj0e2Mo07u3SCdq9yyoFjjOy1wjVjtS3bNy1ZJJpLTpLpmP62teiaXNhfib3E3qaiaQibPuwfv7bLsyQ5j4SW1GXznVk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNv6D8d39KNCEKTYiaN9rs456k9aXWKGHxPjqrXurwO3pQtUuxKhibaKicWpiaiap3oFePjVWJvxIcQ4j1TibdASML2ibhSXsuvS2cicAg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNU1ygQQZfjgXvxoibFbicicsj04h8icbzicVJazZOibhnE84LpuqAkpfP1NL1QVyZSRgBEU7PNj9iat1yic65icE18lkQHmwNGSIpQ1FicM/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRNR64iaS8TASUhrTmZcHJRuI8gd0VnicbdNNGWIG7iauzp73HnQlf6lIxUEKwEGby5X1AoRMLtXjcgTtog7rSFojzXxtSNL4CgghE/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRM75vibibxBQeEvW7MfIkcgT6elxoRuN5K4sgktZibticK3fQz5icY2QqkDM98lheRYw0VRFCpjvjicMNnJ1dIPanhr6cLs6iaAEhWyWk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPwoBVWn249ibia6uvtIpx02IibUibfAdnHRMXvNDQ0yAcQIWIrxoYfhsjGAfvS6bbNp0Q0M51LfzXEBLFDQicFxnSzHoiaPUDyFcYq8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbROOzsxzZoUS6F3FW9Qa6DwO6pCAJKzib2Cbb4deMaKhtfak5QewxbTBwdp3krQgpGOibAaMOvdibYdL5K88KzVOuSN0aQ6HvblVrY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbROeM3R0QQrtUffVYcuzFvzsbk64hTPDw0q15GZ4gia0OVyFibZy5qiaaadracnaozuNgmEtwDGEuXEUzictweUibPGRlZV7SVBXXdVo/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNDqoH1AiboU9SjxJG4dtuNMdteLlpf6p7YnHZZR5ncdYTlVnRsibd9FuEODSJMzjqJuzCZjf9BicA6oItENJBFoiaL4FducnjdxGw/640?wx_fmt=png&from=appmsg
