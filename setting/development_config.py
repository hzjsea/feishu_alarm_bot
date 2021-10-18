#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: development_config.py.py
@time: 2021/10/15 4:51 下午
"""
from pydantic import BaseSettings


class Config(BaseSettings):
    APP_ID: str = ""
    APP_SECRET: str = ""
    APP_VERIFICATION_TOKEN: str = ""


config = Config()
