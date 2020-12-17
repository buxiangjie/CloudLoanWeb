# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 策略列表
"""

from common.base import Base
from selenium.webdriver.common.by import By

class StrategyList(Base):

	add_strategy = (By.XPATH, "//div[@class='mainWrap']/button/span")

	def check_strategy_list(self):
		assert self.get_text(*self.add_strategy) == "新增策略"