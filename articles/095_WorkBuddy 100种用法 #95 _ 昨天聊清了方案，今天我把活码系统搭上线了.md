# WorkBuddy 100种用法 #95 | 昨天聊清了方案，今天我把活码系统搭上线了

- 合集序号：95
- 公众号：我与ai的那些事
- 发布日期：2026-07-04
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzA4OTE4MjYzMg==&mid=2648330094&idx=1&sn=43e3e0d40c699334c76439c6d35d9e0d&chksm=883037a9bf47bebf4a8d2ffea13469d387deb6873755fe8545df29cc0fe81862040681e22e90#rd
- 正文字数：3837
- 正文图片：8

## 摘要

昨天和WorkBuddy捋清活码方案，今天直接动手落地：一句话需求生成Flask项目，三轮调试CSS，6.5天过期缓冲，AWS部署遇端口墙用nginx绕行，最终线上跑通付款+加群两步活码系统。

## 正文

上一篇WorkBuddy 100种用法 #94 | 微信群码7天就过期？我拉着WorkBuddy把活码引流这事彻底捋清了，文末我说："下一步，就是把这套东西搭出来。" 这篇就是那个"下一步"。

一句话总结：我让 WorkBuddy 直接动手，从零写代码、部署上线、反复调样式，最后跑出了一个能用的活码系统。

一、提需求：把昨天的方案变成代码

我没有写需求文档，也没有画原型图。我就说了一句话：

"把你昨天给我的方案实现一下——对外活码页、后台上传新群码（手机端能操作）、定时提醒调度器，把这三个帮我实现一下。"

WorkBuddy 已经带着昨天对话的完整上下文，直接开干。

它建了一个 Flask 项目，四个文件各司其职：

文件

干什么

app.py

主程序，对外活码页 + 后台上传 + API

config.py

配置：过期天数、管理密码、企业微信 Webhook

store.py

数据存储，JSON 文件记录上传时间和过期状态

scheduler.py

APScheduler 定时任务，每 6 小时检查一次是否快过期

外加两个 HTML 页面：

-
• index.html——用户扫码看到的活码展示页

-
• admin.html——后台管理页，手机端上传群码

整个项目结构清晰到我不需要解释第二遍。

二、第一个坑：管理后台样式渲染问题

代码跑起来了，上传功能也通了。但我打开管理后台一看——样式炸了。

上传区域的虚线边框死活显示不出来，HTML 注释嵌在 <style> 里导致后续 CSS 全部失效。

我截图发给 WorkBuddy："你自己看一下这个样式正确吗？"

它检查了一遍说改好了，我一看——还是不对。

又来一轮，还是不对。

三轮之后，WorkBuddy 换了思路：不再用 border 或 outline，改用 box-shadow: inset 0 0 0 2px 来模拟边框。

这一招终于管用了。

💡 教训：CSS 的 border 和 outline 在某些渲染条件下会出问题，box-shadow: inset 是更稳定的替代方案。WorkBuddy 试了三次才找到这个解法——AI 也会在同一个坑里摔几次，但它会换策略，不会死磕。

三、过期逻辑：从 7 天改成 6.5 天

默认过期时间设的是 7 天，和微信规则一致。但我实际用下来发现一个问题：

从你在微信里生成群码，到手动上传到后台，中间有时间差。

比如你下午 3 点生成群码，晚上 10 点才想起来上传——这 7 个小时已经消耗掉了。等你上传完，群码实际只剩 6 天多就过期了。

如果系统还按 7 天算提醒时间，提醒会晚来半天，群码可能已经失效。

所以我把过期天数改成了 6.5 天，留出半天的缓冲。

WorkBuddy 秒改，顺便把进度条和倒计时显示的逻辑都同步调整了。

四、部署上线：AWS EC2 上的波折

代码本地跑通了，下一步是部署到服务器。

我有一台 AWS EC2（us-east-2 区域），之前配过 SSH 短链接，终端敲 ssh aws 直接登。

4.1 上传代码 + 装依赖

scp -r huoma aws:/home/ubuntu/
ssh aws "cd huoma && pip3 install -r requirements.txt"

Flask + APScheduler，两个依赖，秒装完。

4.2 systemd 服务

WorkBuddy 帮我写了一个 systemd service 文件，让应用开机自启、崩了自动重启：

[Unit]
Description=Huoma Live QR System
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/xxx
ExecStart=/usr/bin/python3 app.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target

4.3 端口问题：进不去的 AWS 控制台

活码应用跑在 5050 端口，但 AWS 安全组只开了 3000。

正常操作应该是去 AWS 控制台开端口。但——我登不进去。

注册邮箱一直提示"没有这个账号"，试了好几个邮箱都不对。区域也搞混了，最后从浏览器地址栏里解析出来是 us-east-2 区域，但登录还是卡住。

WorkBuddy 看到这个情况，没让我继续死磕控制台，而是换了个思路：

"你服务器上 3000 端口已经开了，对吧？那不用开新端口，用 nginx 反向代理，把 3000 的请求按路径转发到不同服务。"

一端口多用，路径分流：

路径

转发到

服务

/

127.0.0.1:5050

活码系统

/new-api/

127.0.0.1:3001

new-api（另一个服务）

nginx 配置：

server {
listen 3000;
server_name _;

location / {
proxy_pass http://127.0.0.1:5050;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
}

location /new-api/ {
proxy_pass http://127.0.0.1:3001/;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
}
}

同时把 new-api 的 Docker 端口映射从 3000:3000 改成 3001:3000，腾出 3000 给 nginx。

不用碰 AWS 控制台，不用开新端口，问题解决。

💡 这里 WorkBuddy 做了一个关键判断：与其卡在"打不开的控制台"，不如用已有的资源换一条路。这是"绕"不是"躲"——目标是一样的，路径换了。

五、活码页升级：加收款码

活码系统跑起来之后，我加了个需求：在活码展示页加一个收款码。

流程设计成两步：

-
1. 扫码付款 99

-
2. 扫码加群

中间放一条醒目的红色警告：未付款直接加群者，一律拉黑。

这个页面 WorkBuddy 前后改了好几版：

-
• 第一版：付款码 + 群码上下排列，中间有箭头

-
• 第二版：去掉金额数字（用户不想显示具体金额在码下方）

-
• 第三版：标题里加红色 "99" 数字

-
• 第四版：去掉顶部"加入社群"标题

-
• 第五版：警告卡片移到最上面，去掉箭头

收款码图片我直接在微信里截的，发给 WorkBuddy，它放到 static/pay-qr.png，页面自动引用。

最终页面结构：

┌──────────────────────────┐
│ ⚠️ 请先完成付款，再扫码加群 │
│ 未付款直接加群者，一律拉黑 │ ← 红色醒目卡片
├──────────────────────────┤
│ ① 扫码付款 99 │
│ │
│ [ 微信收款码 ] │
│ 👆 长按二维码 → 识别 → 付款 │
├──────────────────────────┤
│ ② 扫码加群 │
│ │
│ [ 群二维码 ] │
│ 👆 长按二维码 → 识别 → 进群 │
│ ✅ 群码有效，剩余 X 天 │
└──────────────────────────┘

六、几个值得说的细节

6.1 过期提醒怎么触达？

scheduler.py 里用 APScheduler 每 6 小时跑一次检查，发现群码距离过期不到 1 天，就通过企业微信 Webhook 推一条消息到我手机上。

不用盯后台，到点自动提醒。

6.2 后台上传体验

admin.html 是手机端友好的——我在微信里生成新群码后，直接手机打开后台页面，选图上传，秒生效。

不用开电脑，不用 SSH，不用碰代码。

6.3 群码备份

每次上传新群码，系统会同时存一份带时间戳的备份（qr_20260704_223000.png），方便回溯。

七、回过头看这轮实操

环节

我做的

WorkBuddy 做的

需求

一句话说清三个功能

写出完整 Flask 项目

调试

截图反馈"样式不对"

三轮排查，最终用 box-shadow 解决

过期逻辑

提出 6.5 天的缓冲需求

秒改配置 + 同步进度条逻辑

部署

提供 SSH 访问方式

写 systemd + nginx 配置

端口问题

说"控制台登不进去"

立刻换方案，nginx 路径分流

页面迭代

逐步提修改意见

每次秒改 + 部署验证

整个过程没有一步是卡死的。遇到问题就反馈，WorkBuddy 就改，改完就部署验证，验证完继续下一个问题。

像是和一个随叫随到的全栈开发搭子配对编程。

八、我的几点感受

① AI 写代码不怕改，怕的是你说不清要什么

"样式不对"这种反馈，WorkBuddy 需要试几次才能命中。但"把过期天数从 7 改成 6.5"这种明确指令，它一次就对。

越具体的反馈，修得越快。

② 遇到墙就绕，别死磕

AWS 控制台登不进去，正常思路是"一定要登进去"。但 WorkBuddy 的思路是"你的目标不是登控制台，是让 5050 端口能从外网访问"——那换个端口就行了。

目标导向，不是路径导向。

③ 迭代比一次性完美更重要

活码页面前后改了五六版，每一版只调一个小地方。如果一开始就让我写一份完整的设计稿再开工，反而慢。边用边调，用着用着就知道该改哪了。

④ "先跑起来"是最重要的里程碑

第一版有 bug 没关系，样式丑没关系——先让它在服务器上跑起来，能上传能展示能提醒，剩下的都是优化。这比在本地追求完美然后一直不敢上线强一百倍。

最后

从一句话需求到线上可用的系统，中间经历了代码编写、样式调试、逻辑优化、服务器部署、端口问题绕行、页面迭代——每一步都有 WorkBuddy 在旁边干具体的事。

方案是想的，系统是做的。想清楚很重要，做出来更重要。

这是WorkBuddy 100种用法第95篇，持续日更，每篇都是真实场景。

关注我，一起探索WorkBuddy的更多玩法。

#WorkBuddy #活码系统 #Flask #AWS部署 #私域引流 #AI写代码 #实战教程 #社群运营

## 正文图片链接

- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMmfyibKNRCxppdm2wlRhBdslVmW3CsLgrDArhg8NzH77Shyb3TwOcYFKNXJbcQLibW8OB9pCIAxhjlCdNYRcYrBOPIib02xBce1s/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMic8uvKmAFEZrnyY8icDOTdiaibyzRwzkVaYibQgjRepSV6FqqUhvMiaUKxtdZ17EI2icockzEPqViceiaeb22ibPibtxtPxLiafic79WMREIk/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRMD5h3O7wdo9zgNHjwficqPARicATdNbtBIX8UT2LwGwt4Q11L1mNjYEFLcTnWVNEv85L7LdmPZ4iaJ17gfZwgQ06z7syMS7p7cbY/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNqNN5gXQ82L3MCtiatcolbwibicpJK1Ufa3AKyxwu4UVrGMUEicpibqO6iaZEltnf0icvSmAdgpAyj4hiasmbhoBt0aVWtKQJAwQ2agl4/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRP28kBibd1hkTJc3q3c46QT2CbbC5VDBvic7iap7dOPTYzjJ6HaKTzXmbW9A13ib2ttYNMwYyXH58GcWwDneWqdvYtAZnFNibIRaK8Y/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRN1wkKR1ibLFyD4Ysia56xnSBD0fL5qxZnCrjJEPfE9ibeFcNxbZgRGiaf678b8eMBib4vKrLM1QicWQNDUkEtFtAy1DvNYZWViaBdUN8/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/mmbiz_png/s516EMWvbRNuOQ6Jpn05PzDhRLhwfzsr7r55n13JSTVRRcIelr4PqHUv5TTxSXQib4k0r1Tib43qSxJg1mIrFr28N2OLMeO9fcUq96E3ur6Lg/640?wx_fmt=png&from=appmsg
- https://mmbiz.qpic.cn/sz_mmbiz_png/s516EMWvbRMOmuK4PIGfJxic1GdbXC4JDuKV9c8pYb6JRNAiaicKDrHg0ovqp1YMwvAIP8sEvaHU0zRbt19aR1JyibrRj8QpIZ9oVaAMjAicothM/640?wx_fmt=png&from=appmsg
