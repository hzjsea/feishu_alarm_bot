#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: utils_psutil.py.py
@time: 2021/10/18 2:12 下午
"""

import psutil

if __name__ == '__main__':
    import psutil

    print(psutil.cpu_times(percpu=False))
    print(psutil.net_connections())

