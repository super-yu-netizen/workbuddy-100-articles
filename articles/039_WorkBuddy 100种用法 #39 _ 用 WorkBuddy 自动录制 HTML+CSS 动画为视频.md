# WorkBuddy 100种用法 #39 | 用 WorkBuddy 自动录制 HTML+CSS 动画为视频

- 合集序号：39
- 公众号：我与ai的那些事
- 发布日期：2026-05-09
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648328808&idx=1&sn=83af7e0b6b1bf4f25fd29ca30ad8df3e&chksm=883032afbf47bbb9070c0b926b0409b676e8c76023e8e32e76a8c3148c5baa7ef83e0043c375#rd
- 正文字数：2236
- 正文图片：1

## 摘要

用WorkBuddy自动将HTML动画转为MP4视频。借助Playwright录制网页动画，配合ffmpeg转码，无需手动录屏，20秒动画1分钟搞定，效率提升10倍。

## 正文

你是否遇到过这种情况：精心制作了一个HTML+CSS动画页面，却不知道如何把它变成视频？今天分享一个实用技巧：用WorkBuddy自动完成从HTML到MP4的全过程。

问题场景

昨天我让workBuddy制作一个"AI Weekly"的新闻速递视频，用HTML+CSS实现了20秒的动画效果：

-
✨ 片头标题弹入动画

-
📰 5条新闻依次滑入

-
🎨 渐变色背景+粒子效果

-
⏱️ 自动时间轴切换

问题来了：如何在公众号文章中展示这个动画？

-
方案A：直接放HTML链接（用户需要点击跳转，体验差）

-
方案B：录制屏幕（手动操作繁琐，效果不稳定）

-
方案C：用WorkBuddy自动录制（一键完成，专业效果）✅

解决过程

第一步：准备HTML文件

我已经有一个完整的HTML动画文件（ai-weekly-fixed.html），包含：

-
1920x1080分辨率（标准视频尺寸）

-
20秒自动循环动画

-
多个场景自动切换

第二步：让WorkBuddy安装工具

我说：

"帮我把这个HTML动画录制成视频"

WorkBuddy会自动：

-
检测系统环境（检查ffmpeg、Playwright）

-
安装缺失的依赖（npm install playwright）

-
创建录制脚本

第三步：自动录制

WorkBuddy会生成一个Node.js脚本（record-video.js）：

const { chromium } = require('playwright');

(async () => {
const browser = await chromium.launch({
headless: false,
args: ['--start-maximized']
});

const context = await browser.newContext({
viewport: { width: 1920, height: 1080 },
recordVideo: {
dir: '/path/to/output/',
size: { width: 1920, height: 1080 }
}
});

const page = await context.newPage();
await page.goto('file:///path/to/ai-weekly-fixed.html');

// 等待动画完成
await page.waitForTimeout(21000);

await context.close();
await browser.close();
})();

运行脚本：

node record-video.js

WorkBuddy会自动：

-
打开浏览器

-
加载HTML页面

-
录制20秒动画

-
保存为webm格式

第四步：转换为MP4

Playwright录制的是webm格式，需要转换为MP4：

ffmpeg -i input.webm -c:v libx264 -preset fast -crf 22 output.mp4

最终效果：

-
✅ 文件大小：1.4MB

-
✅ 视频时长：20秒

-
✅ 分辨率：1920x1080

-
✅ 可直接插入公众号文章

关键步骤

传统方式 vs WorkBuddy方式

步骤

传统方式

WorkBuddy方式

安装工具

手动查文档、装依赖

自动检测并安装

编写脚本

查API文档、调试代码

自动生成可用脚本

录制视频

手动操作、容易出错

一键运行、稳定可靠

格式转换

查ffmpeg命令参数

自动执行并验证

WorkBuddy的核心能力

-
环境感知：自动检测系统已安装的 tools

-
依赖管理：自动安装缺失的 npm 包

-
脚本生成：根据需求生成可执行的代码

-
错误处理：遇到问题时自动调试和修复

-
格式转换：自动调用ffmpeg转换视频格式

适用场景

这个技巧不仅适用于HTML动画，还可以用于：

-
数据可视化展示：将D3.js/Chart.js图表录制成视频

-
产品演示：录制网页交互流程

-
教程制作：自动录制操作步骤

-
动画原型验证：快速预览HTML动画效果

-
多分辨率适配：批量录制不同尺寸的版本

tip

如果你也想自己实现，关键步骤是：

-

HTML动画设计原则

-
固定分辨率（1920x1080）

-
使用CSS动画（@keyframes）

-
JavaScript控制时间轴切换

-
避免依赖外部资源

-

Playwright录制配置

const context = await browser.newContext({
viewport: { width: 1920, height: 1080 },
recordVideo: {
dir: './output/',
size: { width: 1920, height: 1080 }
}
});

-

ffmpeg转换参数

ffmpeg -i input.webm \
-c:v libx264 \
-preset fast \
-crf 22 \
-c:a aac \
output.mp4

最推荐的方式：直接跟WorkBuddy说"帮我把这个HTML动画录制成视频"，剩下的都交给他。

写在最后

以前：

-
😓 手动录制需要5-10分钟

-
😓 容易录错时长或分辨率

-
😓 需要安装多个工具并学习使用

现在：

-
✅ 一键完成，耗时不到1分钟

-
✅ 自动匹配HTML设计分辨率

-
✅ WorkBuddy处理所有技术细节

📢 互动环节

这是「WorkBuddy 100种用法」系列第 39 篇，日更中！

如果这篇文章对你有帮助：

-
点赞 让更多人看到

-
在看 支持持续更新

-
分享 给需要的朋友

有任何问题或想法，欢迎在评论区交流！

关注我，每日解锁 WorkBuddy 新玩法！

#WorkBuddy100种用法 #AI工具 #HTML动画 #视频制作 #AICoding #自动化 #前端开发 #效率提升 #Playwright #ffmpeg #视频录制

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNlBSdQFficsC5luStAYjYwghVI0hywSfKNRrRGuAtP45WfLE3w7iaJDVcFD9b3ORBtREknqZxY6lOJeKzAh0MCqDSvwt8q26uicc/640?wx_fmt=png
