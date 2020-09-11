# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:25:00
@describe: 分账报表
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class SplitReport(Base):

	split_report = (By.CSS_SELECTOR, "h2[class=title")
	select_report_type = (By.CSS_SELECTOR, "#react-select-4--value-item")

	@allure.step("检查分账报表")
	def check_split_report(self):
		assert self.find_element(*self.split_report)