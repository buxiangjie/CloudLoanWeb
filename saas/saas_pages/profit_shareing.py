# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:35:00
@describe: 分润
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class ProfitShareing(Base):
	profit_shareing = (By.CSS_SELECTOR, "h2[class=title]")
	view_reconciliation = (By.CSS_SELECTOR, "a[href*='dividedDetail']")

	@allure.step("分润")
	def check_profit_shareing(self):
		assert self.find_element(*self.profit_shareing)

	@allure.step("跳转对账")
	def page_reconciliation(self):
		self.element_click(*self.view_reconciliation)
		return Reconciliation(self.driver)

class Reconciliation(Base):

	profit_shareing = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查分润对账")
	def check_profit_shareing_reconciliation(self):
		assert self.find_element(*self.profit_shareing)