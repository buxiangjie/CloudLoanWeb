# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:20:00
@describe: 分账
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class Split(Base):

	split = (By.CSS_SELECTOR, "h2[class=title")

	@allure.step("检查分账")
	def check_split(self):
		assert self.find_element(*self.split)