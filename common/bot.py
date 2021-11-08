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
import subprocess

class BOT(object):
    def __init__(self):
        pass

    @staticmethod
    def read_yaml():
        cur_dir = os.getcwd() + "/alarm_yaml/"
        f_list = os.listdir(cur_dir)

        if "config.yaml" in f_list:
            cur_dir = cur_dir + "config.yaml"
        else:
            cur_dir = cur_dir + "default.yaml"

        return YamlParse.yaml_to_json(cur_dir)


class MethodEnum(Enum):
    POST = 'POST'
    GET = 'GET'

def subprocess_getoutput(stmt):
    print(stmt)
    result = subprocess.getoutput(stmt)
    return result

def switch_type(open_id: str, instance: str, subject: str, flag: str = "test") -> (str, JSONType, MethodEnum):

    instance = json.loads(instance)

    if "alarm_template_path" in instance.keys():
        alarm_template_path = instance.get("alarm_template_path", "")
        alarm_run_command = instance.get("alarm_run_command", "")
        alarm_flag = instance.get("alarm_flag", False)
        url = "https://open.feishu.cn/open-apis/message/v4/send/"
        method = MethodEnum.POST
        req_body = {
            "open_id": open_id,
            "msg_type": "interactive",
            "card": {}
        }

        if alarm_template_path is not None and alarm_flag:
            template_path = os.getcwd() + "/alarm_yaml/" + alarm_template_path
            template = open(template_path, 'r+').read()
            template = json.loads(template)
            req_body["card"] = template

        if alarm_run_command is not None and alarm_flag:
            # find cmd director
            cmd_file = os.path.dirname(os.getcwd()) + "/feishu_alarm_bot/cmd/" + alarm_run_command

            if subject:
                res = subprocess_getoutput(f"bash {cmd_file} {subject}")
            else:
                res = subprocess_getoutput(f"bash {cmd_file}")


            tmp = json.loads(res)["data"]["valueRange"]["values"][0]
            try:
                xx = "\n".join([str(a) for a in tmp])
            except Exception as e:
                print(e)
                xx = res
            req_body["card"]["i18n_elements"]["zh_cn"][1]["content"] = xx


        return url, req_body, method



# import os
# import subprocess
# import json
#
# def subprocess_getoutput(stmt):
#     result = subprocess.getoutput(stmt)
#     # 执行失败不需要特殊处理，因为该方法无法判断失败成功，只负责将结果进行返回
#     return result
#
#
# cmd_file = os.path.dirname(os.getcwd()) + "/feishu_alarm_bot/cmd/" + "a.sh"
# subject = "192.168.14.101"
# if subject:
#     res = subprocess_getoutput(f"bash {cmd_file} {subject}")
#     #res = os.popen(f"bash {cmd_file} {subject}")
#     # res = os.system(f"bash {cmd_file} {subject}")
# else:
#     res = subprocess_getoutput(f"bash {cmd_file}")
#     #res = os.popen(f"bash {cmd_file}")
#     # res = os.system(f"bash {cmd_file}")
#
# print(type(res))
# print(res)

# print(json.loads(res))