# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 17:15:00
@describe: 还款统计
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class RepayStatistics(Base):

	repay_statistics = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查还款统计")
	def check_repay_statistics(self):
		assert self.find_element(*self.repay_statistics)