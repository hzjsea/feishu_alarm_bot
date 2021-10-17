#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: utils_timer.py.py
@time: 2021/10/15 2:39 下午
"""

import datetime


class TimerTemplate(object):
    def __init__(self):
        pass

    @staticmethod
    def cur_date():
        """
        :return: 2018-05-08 16:53:30.10100 :type datetime.datetime
        """
        return datetime.datetime.now()

    @staticmethod
    def format_date():
        """
        :return: 2018-05-08 16:54 :type str
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def date_cal():
        """
        多加一天
        :return: 2021-10-14 15:29:03.93906 :type datetime.datetime
        """
        return datetime.datetime.now() + datetime.timedelta(days=1)

    @staticmethod
    def str_to_date():
        now = datetime.datetime.now()  # datetime.datetime (type
        t = now.strftime("%Y-%m-%d %H:%M")  # str
        dt = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M")  # datetime.datetime (type
        print(now, dt)


if __name__ == '__main__':
    print(TimerTemplate.str_to_date())
    print(type(datetime.datetime.now()))
    TimerTemplate.str_to_date()
