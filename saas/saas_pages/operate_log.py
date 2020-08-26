# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-25 16:37:00
@describe: 操作日志
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class OperateLog(Base):
	operate_log = (By.CSS_SELECTOR, "h2[class=title]")
	operate = (By.CSS_SELECTOR, "table[role=grid] > tbody > tr:nth-child(1) > td:nth-child(6) > a > i")

	@allure.step("检查操作日志")
	def check_operate_log(self):
		assert self.find_element(*self.operate_log)

	@allure.step("进入操作日志详情")
	def page_operate_log_detail(self):
		self.element_click(*self.operate)
		return OperateLogDetail(self.driver)

class OperateLogDetail(Base):
	operate_log_detail = (By.CSS_SELECTOR, "h5[class=card-title]")

	@allure.step("检查操作日志详情")
	def check_operate_log_detail(self):
		assert self.find_element(*self.operate_log_detail)