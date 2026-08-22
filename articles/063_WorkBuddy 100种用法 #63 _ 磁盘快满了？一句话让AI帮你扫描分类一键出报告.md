# WorkBuddy 100种用法 #63 | 磁盘快满了？一句话让AI帮你扫描分类一键出报告

- 合集序号：63
- 公众号：我与ai的那些事
- 发布日期：2026-06-02
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648329297&idx=1&sn=1f266337de4f8821d5f3c99aeacd58b2&chksm=88303496bf47bd80fcdeb8dba1150ae9b2986d1b58f15ee041b6b9446aeeafac77c7eaa429e6#rd
- 正文字数：2210
- 正文图片：4

## 摘要

Mac只剩9GB濒临爆盘，我用一句话让WorkBuddy自动扫描磁盘、AI智能分类、生成交互式报告，全程零代码三步搞定。

## 正文

今早的真实遭遇：Mac 磁盘只剩 9.2 GB，用 WorkBuddy + storage-analyzer 技能，三步搞定磁盘扫描和分类报告。

起因：磁盘亮红灯了

最近打开电脑，一上微信电脑老是提醒存储空间不足——233 GB 的盘，只剩 9.2 GB。

说实话以前遇到这种事，我一般都是这套路：

-
打开「关于本机」→「储存空间」看一眼大数字，然后懵

-
开终端敲 du -sh *，一个一个目录猜

-
搜"macOS怎么清理磁盘"，翻一堆过期教程

-
最后还是下了个清理工具，还得掏钱买会员

这次我不折腾了，让 WorkBuddy 来。

第一步：先让 AI 帮我研究一下这个技能

早上正好看到 卡神 开源了电脑清理技能 storage-analyzer，直接把链接扔给 WorkBuddy：

帮我看看这个 skill 有什么作用：https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer[1]

WorkBuddy 自己爬了仓库里所有文件，给我出了份完整报告：

-
干啥的：macOS / Windows 只读磁盘分析助手

-
工作流：扫描 → AI 智能分类 → 交互式 HTML 报告

-
亮点：三级分类（🟢可清理 / 🟡需判断 / 🔴谨慎）、零依赖、全程只读

看完觉得靠谱，装它。

第二步：安全审计 + 安装，一步到位

装第三方技能，安全肯定得先看看。我就说了一句：

帮我安装这个 skill

WorkBuddy 自己调了腾讯朱雀实验室的 skill-scanner 做安全审计：

检测项

结果

来源可信度

⚠️ GitHub 开源（12.5k Stars），社区挺活跃

会不会动文件

⚠️ 扫描阶段只读，删除得在网页上手动确认

有没有偷偷联网

✅ 纯本地，没任何外部请求

有没有危险操作

✅ 多层安全机制兜着呢

审计没问题，7 个文件自动下到 ~/.workbuddy/skills/storage-analyzer/，全程不用我动手。

第三步：一句话开扫

技能装好了，高潮来了——

帮我看看存储

就这一句话，WorkBuddy 自动触发了 storage-analyzer 技能，背后跑了三件事：

① 扫描：跑 scan.py，只读方式把 HOME 目录下一级二级子目录全过一遍

② AI 分类：拿着扫描结果 + macOS 目录参考文档，自动识别每个目录是干嘛的，然后分级

③ 出报告：生成交互式 HTML 报告

扫完我傻了：95.9% 已用

项目

数据

总容量

233.5 GB

已用

224.2 GB（95.9%）

剩余

9.2 GB
🔴

文件系统

APFS

🟢 能放心清的：约 10.6 GB

项目

大小

怎么清

Library/Caches（各种缓存）

5.5 GB

rm -rf ~/Library/Caches/*

开发缓存（.npm/.cache/Chromium快照）

4.5 GB

逐项清理

Xcode CoreSimulator

1.5 GB

xcrun simctl delete unavailable

🟡 得想想再清的：约 56.3 GB

项目

大小

怎么说

微信

15.8 GB

用微信内置清理，千万别手动删容器文件

Docker

9.7 GB

docker system prune -a
清掉没用镜像

Ollama 模型

6.7 GB

不用的模型 ollama rm 模型名 删掉

.gemini 备份

2.1 GB

确认用不上了再删

🔴 手别欠的：约 10.3 GB

项目

大小

为啥不能动

Anaconda3

4.7 GB

删了 Python 环境全没了

网易 MuMu 模拟器

3.6 GB

数据直接丢

跟手动清理比比看？

对比项

手动清理

WorkBuddy + storage-analyzer

扫描方式

du -sh *
一个一个猜

自动遍历 + 按大小排好序

分类依据

靠经验猜这目录是干嘛的

AI 语义理解，能认出"这串UUID是B站离线缓存"

安全提示

没人提醒你

🟢🟡🔴 三级白名单帮你兜底

报告形式

终端里一堆数字

可视化 HTML + 清理命令直接复制

操作门槛

得会敲命令

一句话搞定

说点技术细节：这技能为啥靠谱

1. 全程只读，碰都不碰你的文件

扫描阶段就用了 du、ls、stat，不写不删。想删东西？得在本地网页上手动点确认。

2. 安全防线一层又一层

-
白名单：只有 🟢 级别的才能删

-
realpath 校验：防符号链接逃逸

-
HOME 边界：绝不越界

-
Token 鉴权 + DNS-rebinding 防护

-
浏览器还会弹个 confirm() 让你再确认一次

3. AI 不只是报大小，还能"看懂"目录

比如扫出来一个 UUID 目录，AI 能识别出"这是 Bilibili 离线视频缓存"，不是瞎报一串路径让你自己猜。

4. 零依赖，开箱即用

纯 Python 标准库写的，不用 pip install 任何东西，macOS 上直接跑。

复盘：从发现到出报告，到底几步？

发现磁盘不足 → 一句话学习技能 → 一句话安装（含安全审计） → 一句话扫描 → 报告出炉

四句话，全流程。

以前这事我得花半小时：查资料、装软件、逐个目录猜。现在跟 WorkBuddy 聊了几轮，报告就出来了，还带分级建议和能直接复制粘贴的清理命令。

WorkBuddy 技能生态最牛的地方就在这——不是替你操作，而是把专业工具变成一句话的事。

这是WorkBuddy 100种用法第63篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #磁盘清理 #storage-analyzer #AI技能 #macOS #存储管理 #效率工具 #自动化 #Skill安装 #系统优化

引用链接

[1]https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer

## 正文图片链接

- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMjRcrHIcIiaibdUdjiaVV1qkYoXLNGgLpfezjsJsFcicDG6KXzPhRHta1jia5Iqgcwa7DGicO1jWge0dha18Pvt1pu3cPbrT7ibD4wjI/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRPYOrq4NjxwQy82M3rDTGNibc1q5Dnmxqg8OxCIwsaJCR60HuQy4FqqW8T7BCBtkLP2ibuxuNgnCtEicqXrtTB2ZSoSQ11yVrBmrQ/640?wx_fmt=png
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMf25cHemfBm95Q1VXzaOFGqqT4U58fFoJD8AgWcKO3yyZ6GUgyO5Q14KDQMHq3sicbzeq0xX8L7p9FCO8fzPZ1v6ILkyBXDjt8/640?wx_fmt=png
- https://mmbiz.qpic.cn/mmbiz_jpg/s516EMWvbRPEaSPuiaV6mShugpAPjw9BlutsyggFRwiabPNxj2E3HndvhYHvibPdtjbVIxXVRsakoIpWXUticZQpoY74FsxeNlFCX2nqF4TAx3U/640?wx_fmt=jpeg
