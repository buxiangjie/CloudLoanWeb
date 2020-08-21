# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 风控配置页面
"""

import allure

from common.base import Base
from selenium.webdriver.common.by import By

class RiskConfig(Base):

	basic_rules = (By.CSS_SELECTOR, ".question-title")

	@allure.step("检查风控配置")
	def check_basic_rules(self):
		assert self.find_elements(*self.basic_rules)