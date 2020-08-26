# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:30:00
@describe: 债转
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class Swap(Base):

	swap = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查债转")
	def check_swap(self):
		assert self.find_element(*self.swap)