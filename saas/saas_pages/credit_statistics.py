# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 授信统计
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class CreditStatistics(Base):

	credit_statistics = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查授信统计")
	def check_credit_statistics(self):
		assert self.find_element(*self.credit_statistics)