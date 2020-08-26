# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 13:38:00
@describe: 额度中心
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class QuoteCenter(Base):
	quote_center = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查额度中心")
	def check_quote_center(self):
		assert self.find_element(*self.quote_center)