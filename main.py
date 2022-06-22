#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File: main.py
@Desc: None
"""

from src.util import excel, flag
from src.webdriver import WebDriver

if __name__ == '__main__':
    f = flag.Flag()
    f.register()

    wd = WebDriver()
    datas = wd.run(f.args.keyword.replace("-", " "))
    excel.save(f"keyword-{f.args.keyword}", datas)
