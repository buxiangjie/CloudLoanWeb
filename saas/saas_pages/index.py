# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: saas主页
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base
from saas.saas_pages.risk_config import RiskConfig
from saas.saas_pages.business_switch import BusinessSwitch
from saas.saas_pages.credit import Credit

class Index(Base):

	overview = (By.CSS_SELECTOR, "[class=title]")
	risk_config = (By.CSS_SELECTOR, "[title=风控配置]")
	business_switch = (By.CSS_SELECTOR, "[title=业务开关]")
	credit = (By.CSS_SELECTOR, "[title=授信]")

	@allure.step("检查首页标题是否显示")
	def check_index(self):
		assert self.find_element(*self.overview)

	@allure.step("跳转风控配置")
	def page_risk_config(self):
		self.element_click(*self.risk_config)
		return RiskConfig(self.driver)

	@allure.step("跳转业务开关")
	def page_business_switch(self):
		self.element_click(*self.business_switch)
		return BusinessSwitch(self.driver)

	@allure.step("跳转授信页面")
	def page_credit(self):
		self.element_click(*self.credit)
		return Credit(self.driver)