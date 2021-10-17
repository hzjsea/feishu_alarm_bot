#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: development_config.py.py
@time: 2021/10/15 4:51 下午
"""
from pydantic import BaseSettings


class Config(BaseSettings):
    APP_ID: str = "cli_a0f784bae739900e"
    APP_SECRET: str = "doG12QNrsWTTB20zQMmHmhCrxhgBdSPU"
    APP_VERIFICATION_TOKEN: str = "BlkeeevdFlYi8dj9IJGXAbGYmbdrFNCo"


config = Config()
