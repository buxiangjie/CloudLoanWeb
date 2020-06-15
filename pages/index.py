# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""
from common.base import Base
from selenium.webdriver.common.by import By


class Index(Base):
	index = (By.LINK_TEXT, "首页")
	about_us = (By.LINK_TEXT, "关于我们")
	product_int = (By.LINK_TEXT, "产品简介")
	news = (By.LINK_TEXT, "新闻公告")
	enterprise_culture = (By.LINK_TEXT, "企业文化")
	join_us = (By.LINK_TEXT, "加入我们")

	def check_index(self):
		assert self.find_element(self.index)

	def open_about_us(self):
		return self.element_click(self.about_us)

	def open_product_int(self):
		return self.element_click(self.product_int)

	def open_news(self):
		return self.element_click(self.news)

	def open_enterprise_culture(self):
		return self.enterprise_culture

	def open_join_us(self):
		return self.join_us
