# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import pytest
import os

from config.configer import Config
from selenium import webdriver
from pages.index import Index


class TestIndex:

	def setup_method(self):
		chrome_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/drivers/chromedriver"
		self.driver = webdriver.Chrome(executable_path=chrome_path)

	def teardown_method(self):
		self.driver.quit()

	def test_index(self):
		index = Index(self.driver)
		index.open()
		index.check_index()

	def atest_join_us(self):
		index = Index(self.driver)
		index.open()
		join_us = index.open_join_us()
		join_us.check_join_us()

	def test_news(self):
		index = Index(self.driver)
		index.open()
		news = index.open_news()
		news.check_news()


if __name__ == '__main__':
	pytest.main()
