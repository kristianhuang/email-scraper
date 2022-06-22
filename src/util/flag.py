#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File: flag.py
@Desc: None
"""
import argparse


class Flag(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="google 邮箱爬虫", usage="python main.py keyword [-s]")
        self.args = None

    def register(self):
        self.parser.add_argument("keyword", type=str, help="keyword in Google")
        self.parser.add_argument("-s", "--silence", help="是否以静默模式运行爬虫",
                                 default=False, action="store_true")
        self.args = self.parser.parse_args()

        return self
