#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File: flag.py
@Desc: None
"""
import argparse


class Flag(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="google 邮箱爬虫", usage="python main.py keyword")
        self.args = None

    def register(self):
        self.parser.add_argument("keyword", type=str, help="keyword in Google")
        self.args = self.parser.parse_args()

        return self
