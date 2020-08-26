# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 10:08:00
@describe: 资金流水
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class CapitalFlow(Base):
	capital_flow = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查资金流水")
	def check_capital_flow(self):
		assert self.find_element(*self.capital_flow)