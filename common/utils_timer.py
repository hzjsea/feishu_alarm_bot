#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: utils_timer.py.py
@time: 2021/10/15 2:39 下午
"""

import time
import datetime


class TimerTemplate(object):
    def __init__(self):
        pass

    @staticmethod
    def cur_date(self):
        # 2018-05-08 16:53:30.101000
        return datetime.datetime.now()

    @staticmethod
    def date_to_str(self):
        # 2018-05-08 16:54
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def str_to_date(self):
        pass

