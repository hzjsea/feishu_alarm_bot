#!/usr/bin/env python
# --coding:utf-8--
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from typing import Optional
from urllib import request
from common import APP_ID, APP_SECRET, APP_VERIFICATION_TOKEN
from common import bot
from typing import Dict

CommandType = [
    {
        "type": "chat",
        "abbr": "ct"
    },
    {
        "type": "alarm",
        "abbr": "am"
    },
    {
        "type": "test",
        "abbr": "tt"
    }
]


class RequestHandler(BaseHTTPRequestHandler):

    # 鉴权 + 传递事件 给消息发送的方法
    def do_POST(self):
        # 解析请求 body
        req_body = self.rfile.read(int(self.headers['content-length']))
        obj = json.loads(req_body.decode("utf-8"))

        # 校验 verification token 是否匹配，token 不匹配说明该回调并非来自开发平台
        token = obj.get("token", "")
        if token != APP_VERIFICATION_TOKEN:
            print("verification token not match, token =", token)
            self.response("")
            return
        # { 'uuid': '', 'event': { 'app_id': '', 'chat_type':
        # 'private', 'employee_id': '', 'is_mention': True, 'lark_version': 'lark/4.6.4', 'message_id': '',
        # 'msg_type': 'text', 'open_chat_id': '', 'open_id':
        # '', 'open_message_id': '',
        # 'parent_id': '', 'root_id': '', 'tenant_key': '', 'text': '<at open_id =
        # "" > @Shikamaru < /at> tt xx', 'text_without_at_bot': ' tt xx',
        # 'type': 'message', 'union_id': '', 'user_agent': 'Mozilla/5.0 (
        # Macintosh;Intel Mac OS X 10 _14_6) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0 .4389 .128 'Safari
        # / 537.36 Lark / 4.6 .4 LarkLocale / zh_CN ttnet SDK - Version / 4.6 .20 ', 'user_open_id
        # ':'' }, 'token': '',
        # 'ts': '.370087', 'type': 'event_callback' 根据 type 处理不同类型事件

        type = obj.get("type", "")
        if "url_verification" == type:  # 验证请求 URL 是否有效
            self.handle_request_url_verify(obj)
        elif "event_callback" == type:  # 事件回调
            # 获取事件内容和类型，并进行相应处理，此处只关注给机器人推送的消息事件
            event = obj.get("event")
            if event.get("type", "") == "message":
                self.handle_message(event)
                return
        return

    # 鉴权成功 回调消息
    def handle_request_url_verify(self, post_obj):
        # 原样返回 challenge 字段内容
        challenge = post_obj.get("challenge", "")
        rsp = {'challenge': challenge}
        self.response(json.dumps(rsp))
        return

    def response(self, body):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body.encode())

    @staticmethod
    def get_tenant_access_token():
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        headers = {
            "Content-Type": "application/json"
        }
        req_body = {
            "app_id": APP_ID,
            "app_secret": APP_SECRET
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            # print(e.read().decode())
            return ""

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("get tenant_access_token error, code =", code)
            return ""
        return rsp_dict.get("tenant_access_token", "")

    def handle_message(self, event):
        # 此处只处理 text 类型消息，其他类型消息忽略
        msg_type = event.get("msg_type", "")
        if msg_type != "text":
            print("unknown msg_type =", msg_type)
            self.response("")
            return

        # 调用发消息 API 之前，先要获取 API 调用凭证：tenant_access_token
        access_token = self.get_tenant_access_token()
        if access_token == "":
            self.response("access_token unknown error")
            return

        # 机器人 echo 收到的消息
        # 'text': '<at open_id = "ou_3bc93fdac4ddc80521734450c0c35e26" > @Shikamaru < /at> tt xx',
        # @shikamaru 机器人的名字
        # tt command
        # xx value
        try:
            text = event.get("text", "unknown_message").strip().split("</at> ")[1]
            # 和机器人无关的消息
            # text = event.get('text_without_at_bot'," nl").strip()
            abbr = "unknown_message"
            subject = text
            if text:
                text_list = text.split(" ")
                if len(text_list) >= 2:
                    abbr = str(text_list[0]).strip()
                    subject = str(text_list[1]).strip()
                else:
                    abbr = text
                self.message_classification_to_send(
                    access_token,
                    event.get("open_id"),
                    abbr,
                    subject,
                    chat_id=event.get("open_chat_id", ""),
                    chat_type=event.get("chat_type", "private")
                )
        except Exception as e:
            print("message parse error, error is ".format(e))
            self.response("")
            return

    def message_classification_to_send(self, token, open_id, abbr, subject, *args, **kwargs):

        type = ""

        for item in CommandType:
            # for循环中的唯一值
            if item["abbr"] == abbr:
                type = item["type"]
                break
            else:
                type = "normal"

        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + token
        }
        chat_type = kwargs.get('chat_type', "private")
        chat_id = kwargs.get("chat_id", " ")

        url, req_body, method = bot.switch_type(open_id=open_id, flag=type)

        if chat_type == "group":
            req_body["chat_id"] = chat_id
        elif chat_type == "private":
            req_body = req_body
        else:
            print("error, 当前不支持其他的聊天行为")

        # data = bytes(json.dumps(req_body), encoding='utf8')
        data = json.loads(req_body)
        self.send_request(url=url, headers=headers, data=data, method=method)

    @staticmethod
    def send_request(url, headers, method, data: Optional[Dict]):

        if method.value == "POST":
            req = request.Request(url=url, data=data, headers=headers, method=str(method.value))
        elif method.value == "GET":
            req = request.Request(url=url, headers=headers, method=str(method.value))
        else:
            sys.exit(0)

        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return
        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("send message error, code = ", code, ", msg =", rsp_dict.get("msg", ""))
