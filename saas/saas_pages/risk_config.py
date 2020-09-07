# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 风控配置页面
"""

import allure
import time

from common.base import Base
from selenium.webdriver.common.by import By

class RiskConfig(Base):

	basic_rules = (By.CSS_SELECTOR, ".question-title")
	save_button = (By.CSS_SELECTOR, "div[class=card-body] > button:nth-child(1)")
	define_save_button = (By.CSS_SELECTOR, "div[class=sa-confirm-button-container]")
	success_text = (By.CSS_SELECTOR, "div[data-has-cancel-button=false] > p")
	i_know = (By.CSS_SELECTOR, "div[class=sa-confirm-button-container] > button")

	@allure.step("检查风控配置")
	def check_basic_rules(self):
		assert self.find_elements(*self.basic_rules)

	@allure.step("保存风控配置")
	def save_basic_rules(self):
		self.element_click(*self.save_button)
		time.sleep(1)
		self.element_click(*self.define_save_button)
		assert self.find_element(*self.success_text).text == "保存成功"
		self.element_click(*self.i_know)