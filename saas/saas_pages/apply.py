# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 16:30:00
@describe: 进件
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class Apply(Base):

	apply = (By.CSS_SELECTOR, "h2[class=title]")
	product = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(4)")
	apply_operate = (By.CSS_SELECTOR, "i[class='fa fa-eye']")

	@allure.step("检查进件")
	def check_apply(self):
		assert self.find_element(*self.apply)

	@allure.step("跳转进件详情")
	def page_apply_detail(self):
		n = self.find_elements(*self.apply_operate)[0]
		n.click()
		return ApplyDetail(self.driver)

class ApplyDetail(Base):

	apply_detail = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查进件详情")
	def check_apply_detail(self):
		assert self.find_element(*self.apply_detail)