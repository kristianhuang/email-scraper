#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File: spider.py
@Desc: None
"""
import re

from bs4 import BeautifulSoup


class Spider(object):

    def __init__(self):
        self.page = None
        self.listDom = None

    def setSource(self, page: str):
        self.page = BeautifulSoup(page, "lxml")
        self.listDom = self.page.find_all("div", class_="VwiC3b")

        return self

    def crawlEmails(self):
        """
        crawling emails.

        :return: emails.
        """
        pat = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,8}'
        emails = []
        for el in self.listDom:
            match = re.findall(pat, el.get_text())
            if len(match) > 0:
                emails = emails + list(set(match))

        return emails

    def haveNextPage(self):
        """
        count page total.

        :return: page total
        """
        nextPage = self.page.find("span", style="display:block;margin-left:53px")

        return nextPage
