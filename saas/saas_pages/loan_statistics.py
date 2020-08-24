# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 17:00:00
@describe: 放款统计
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class LoanStatistics(Base):

	loan_statistics = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查放款统计")
	def check_loan_statistics(self):
		assert self.find_element(*self.loan_statistics)