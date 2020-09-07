# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 业务开关页面
"""

import allure
import time

from selenium.webdriver.common.by import By
from common.base import Base


class BusinessSwitch(Base):
	take_effect = (By.CSS_SELECTOR, ".btn-primary")
	effect_button = (By.CSS_SELECTOR, "div[class=card-body] > button:nth-child(1)")
	confirm_effect_button = (By.CSS_SELECTOR, "div[class=sa-confirm-button-container] > button:nth-child(1)")
	effect_success_text = (By.CSS_SELECTOR, "div[data-custom-class] > p")
	i_know = (By.CSS_SELECTOR, "div[class=sa-confirm-button-container] > button")

	@allure.step("检查业务开关")
	def check_business_switch(self):
		assert self.find_element(*self.take_effect)

	@allure.step("生效业务开关")
	def effect_business_switch(self):
		self.element_click(*self.effect_button)
		time.sleep(1)
		self.element_click(*self.confirm_effect_button)
		time.sleep(1)
		assert self.find_element(*self.effect_success_text).text == "生效成功"
		self.element_click(*self.i_know)

