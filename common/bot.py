#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: bot.py
@time: 2021/10/15 10:59 上午
"""
from enum import Enum
from .utils import JSONType, YamlParse, FilePathTemplate
import os
import json


class BOT(object):
    def __init__(self):
        pass

    @staticmethod
    def read_yaml():
        cur_dir = os.path.dirname(os.path.dirname(__file__)) + "/alarm_yaml/"
        f_list = os.listdir(cur_dir)

        if "config.yaml" in f_list:
            cur_dir = cur_dir + "config.yaml"
        else:
            cur_dir = cur_dir + "default.yaml"

        return YamlParse.yaml_to_json(cur_dir)


class MethodEnum(Enum):
    POST = 'POST'
    GET = 'GET'


def switch_type(open_id: str, instance: str, flag: str = "test") -> (str, JSONType, MethodEnum):

    instance = json.loads(instance)
    if "alarm_template_path" not in instance.keys():
        if flag == "alarm":
            pass
        elif flag == "chat1":
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
        elif flag == "test1":
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

    if "alarm_template_path" in instance.keys():
        alarm_template_path = instance["alarm_template_path"]
        alarm_run_command = instance["alarm_run_command"]
        alarm_flag = instance["alarm_flag"]
        url = "https://open.feishu.cn/open-apis/message/v4/send/"
        method = MethodEnum.POST
        req_body = {
            "open_id": open_id,
            "msg_type": "interactive",
            "card": {}
        }
        template_path = os.path.dirname(os.getcwd()) + "/alarm_yaml/" + alarm_template_path
        template = open(template_path, 'r+').read()
        template = json.loads(template)
        req_body["card"] = template

        return url, req_body, method


if __name__ == '__main__':
    ss = BOT.read_yaml()
    for items in ss["Temaplte"]["module"].values():
        for instance in items:
            print(instance)
