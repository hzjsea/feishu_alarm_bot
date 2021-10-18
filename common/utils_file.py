#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: utils_file.py.py
@time: 2021/10/18 11:14 上午
"""


class FileTemplate(object):
    def __init__(self):
        pass

    def show_cur_dir_files(self) -> str:
        import os
        paths = os.listdir(os.getcwd())
        print(paths)
        # or
        paths = os.listdir(".")
        return ""
