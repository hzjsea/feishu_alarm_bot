# feishu_alarm_bot
飞书报警机器人 支持Yaml配置报警信息

> 机器人分为两种机器人，一种是无法提供交互环境的 只能作为监控出现 ,另外一种是可以提供交互环境, 可以设置不同的任务需求，更加灵活，但需要提供一个回调地址， 前者叫做自定义机器人

具体可以看这里
https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN

## 基于会话的机器人
创建应用文档
https://open.feishu.cn/document/home/interactive-session-based-robot/introduction
开发者平台
https://open.feishu.cn/app/cli_a0f784bae739900e/overview

添加回调地址
![](https://noback.upyun.com/2021-10-14-16-07-50.png!)

权限管理
![](https://noback.upyun.com/2021-10-14-16-10-30.png!)

事件订阅 回调地址和前面一样
![](https://noback.upyun.com/2021-10-14-16-11-01.png!)

开发文档
https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/coding
https://sf3-cn.feishucdn.com/obj/website-img/093b18e5189ad423a378b616b1bf94c3_Tbosxo7mus.py

消息卡片定义
https://open.feishu.cn/tool/cardbuilder?from=ttrlbot3

json to yaml
https://onlineyamltools.com/convert-json-to-yaml

## 环境设置
设置环境参数，下载文件之后创建一个env文件
```bash
APP_ID = ""
APP_SECRET = ""
APP_VERIFICATION_TOKEN = ""

```


## 权限管理

APP_ID  和 APP_SECRET 在`凭证与基础信息`获得
APP_VERIFICATION_TOKEN 在 `事件订阅` 中获得