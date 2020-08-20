# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import allure

from common.base import Base
from selenium.webdriver.common.by import By
from cloudloanweb.pages.join_us import JoinUs
from cloudloanweb.pages.enterprise_culture import EnterpriseCulture
from cloudloanweb.pages.news import News
from cloudloanweb.pages.product_int import ProductInt
from cloudloanweb.pages.about_us import AboutUs


class Index(Base):
	index = (By.LINK_TEXT, "首页")
	about_us = (By.LINK_TEXT, "关于我们")
	product_int = (By.LINK_TEXT, "产品简介")
	news = (By.LINK_TEXT, "新闻公告")
	enterprise_culture = (By.LINK_TEXT, "企业文化")
	join_us = (By.LINK_TEXT, "加入我们")

	@allure.step("检查首页是否成功打开")
	def check_index(self):
		assert self.find_element(*self.index)

	@allure.step("点击关于我们")
	def open_about_us(self):
		self.element_click(*self.about_us)
		return AboutUs(self.driver)

	@allure.step("点击产品简介")
	def open_product_int(self):
		self.element_click(*self.product_int)
		return ProductInt(self.driver)

	@allure.step("点击新闻公告")
	def open_news(self):
		self.element_click(*self.news)
		return News(self.driver)

	@allure.step("点击企业文化")
	def open_enterprise_culture(self):
		self.excute_script("arguments[0].click();", self.find_element(*self.enterprise_culture))
		return EnterpriseCulture(self.driver)

	@allure.step("点击加入我们")
	def open_join_us(self):
		self.excute_script("arguments[0].click();", self.find_element(*self.join_us))
		return JoinUs(self.driver)
