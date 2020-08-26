# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:54:00
@describe: 分润2019
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class ProfitShareing2019(Base):
	profit_shareing_2019 = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查分润2019")
	def check_profit_shareing_2019(self):
		assert self.find_element(*self.profit_shareing_2019)