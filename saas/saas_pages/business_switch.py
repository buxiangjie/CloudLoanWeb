# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 业务开关页面
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class BusinessSwitch(Base):
	take_effect = (By.CSS_SELECTOR, ".btn-primary")

	@allure.step("检查业务开关")
	def check_business_switch(self):
		assert self.find_element(*self.take_effect)