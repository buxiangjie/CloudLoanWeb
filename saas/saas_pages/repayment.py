# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:20:00
@describe: 还款(原分账)
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class Repayment(Base):

	repayment = (By.CSS_SELECTOR, "h2[class=title")

	@allure.step("检查还款")
	def check_repayment(self):
		assert self.find_element(*self.repayment)