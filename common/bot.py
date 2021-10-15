#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: bot.py
@time: 2021/10/15 10:59 上午
"""
from enum import Enum
from .utils import JSONType


class MethodEnum(Enum):
    POST = 'POST'
    GET = 'GET'


def switch_type(open_id: str, flag: str = "test") -> (str, JSONType, MethodEnum):
    url = ""
    req_body = {}
    method = MethodEnum.POST

    if flag == "alarm":
        pass
    elif flag == "chat":
        # 获取群号， 但是在聊天 send接口中也有 对应的是 chat_id 字段 必须放在req_body{} 一层下面
        # url = "https://open.feishu.cn/open-apis/chat/v4/list"
        # self.send_request(url=url, headers=headers, data=None,method=MethodEnum.GET)

        url = "https://open.feishu.cn/open-apis/message/v4/send/"
        req_body = {
            "open_id": open_id,
            "msg_type": "post",
            # "chat_id":"oc_75073e8c0265baab97ddb0082f4b260c",
            "content": {
                "post": {
                    "zh_cn": {
                        # "title": "无对应指令,指令列表如下",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "un_escape": True,
                                    "text": "你好"
                                },
                                {
                                    "tag": "at",
                                    # "user_id": "ou_21cdbb2f082181e4bd7e1625fcfd1082" # open_id
                                    "user_id": open_id
                            }
                            ]
                        ]
                    },

                }
            }
        }
        method = MethodEnum.POST
    elif flag == "normal":
        url = "https://open.feishu.cn/open-apis/message/v4/send/"
        req_body = {
            "open_id": open_id,
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "无对应指令,指令列表如下",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "un_escape": True,
                                    "text": "wm tt ct"
                                }
                            ]
                        ]
                    },

                }
            }
        }
        method = MethodEnum.POST
    elif flag == "test":
        url = "https://open.feishu.cn/open-apis/message/v4/send/"
        req_body = {
            "open_id": open_id,
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "我是一个标题",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": "着火啦"
                                },
                            ],
                        ]
                    }
                }
            }
        }
        method = MethodEnum.POST
    return url, req_body, method
