# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class Credit(Base):

	title = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查授信列表")
	def check_credit(self):
		self.find_element(*self.title)