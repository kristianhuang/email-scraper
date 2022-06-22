#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File: webdriver.py
@Desc: None
"""
import os

from rich import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from src.spider import Spider


class WebDriver(object):
    url = "https://www.google.com.hk"

    def __init__(self):
        self.driver = self.__intDriver()
        self.sp = Spider()
        self.emails = []

    def run(self, keyword: str):
        print("[bold green]抓取中[/bold green]:smiley:")
        self.driver.get(self.url)
        try:
            self.__handleSearch(keyword)
            self.__findEmails()
            print(self.emails)
        except Exception as e:
            pass
        self.driver.quit()
        self.driver.close()

        return self.emails

    def __findEmails(self):
        try:
            emails = self.sp.setSource(self.driver.page_source).crawlEmails()
            if len(emails) > 0:
                self.emails = self.emails + emails
            nextPage = self.driver.find_element(By.ID, "pnnext")
            nextPage.click()
            self.__findEmails()
        except Exception as e:
            pass

    def __handleSearch(self, keywords: str):
        """
        search for keywords in Google.

        :param keywords: keywords.
        :return: None
        """
        inputEl = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        inputEl.send_keys(keywords)
        inputEl.send_keys(Keys.ENTER)

    def __intDriver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # options.add_argument("--headless")  # 无头模式
        options.add_argument("--disable-gpu")  # 禁止弹窗
        options.add_argument('--incognito')  # 无痕隐身
        options.add_experimental_option("excludeSwitches", ['enable-logging', "enable-automation"])  # 禁止打印日志.规避检测
        options.add_argument('blink-settings=imagesEnabled=false')  # 禁止图片
        # options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--log-level=3")  # 关闭日志打印
        driver = webdriver.Chrome(executable_path=ChromeDriverManager(log_level=40).install(),
                                  options=options)
        with open(f'{os.path.dirname(__file__)}/../stealth.min.js') as f:
            js = f.read()
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })

        return driver
