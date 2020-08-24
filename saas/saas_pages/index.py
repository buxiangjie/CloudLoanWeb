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
from saas.saas_pages.credit_statistics import CreditStatistics
from saas.saas_pages.apply import Apply
from saas.saas_pages.apply_statistics import ApplyStatistics
from saas.saas_pages.migration_rate import MigrationRate
from saas.saas_pages.loan_statistics import LoanStatistics

class Index(Base):

	overview = (By.CSS_SELECTOR, "[class=title]")
	risk_config = (By.CSS_SELECTOR, "[title=风控配置]")
	business_switch = (By.CSS_SELECTOR, "[title=业务开关]")
	risk = (By.CSS_SELECTOR, "[title=风控]")
	credit = (By.CSS_SELECTOR, "[title=授信]")
	credit_statistics = (By.CSS_SELECTOR, "[title=授信统计]")
	apply = (By.CSS_SELECTOR, "[title=进件]")
	apply_statistics = (By.CSS_SELECTOR, "[title=进件统计]")
	migration_rate = (By.CSS_SELECTOR, "[title=迁徙率]")
	capital_operation = (By.CSS_SELECTOR, "[title=资金运营]")
	loan_statistics = (By.CSS_SELECTOR, "a[title=放款统计]")
	repay_statistics = (By.CSS_SELECTOR, "a[title=还款统计]")

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

	@allure.step("点击菜单栏风控按钮")
	def click_risk_menu(self):
		self.element_click(*self.risk)

	@allure.step("跳转授信页面")
	def page_credit(self):
		self.element_click(*self.risk)
		self.element_click(*self.credit)
		return Credit(self.driver)

	@allure.step("跳转授信统计")
	def page_credit_statistics(self):
		self.click_risk_menu()
		self.element_click(*self.credit_statistics)
		return CreditStatistics(self.driver)

	@allure.step("跳转进件")
	def page_apply(self):
		self.click_risk_menu()
		self.element_click(*self.apply)
		return Apply(self.driver)

	@allure.step("跳转进件统计")
	def page_apply_statistics(self):
		self.click_risk_menu()
		self.element_click(*self.apply_statistics)
		return ApplyStatistics(self.driver)

	@allure.step("跳转迁徙率")
	def page_migration_rate(self):
		self.click_risk_menu()
		self.element_click(*self.migration_rate)
		return MigrationRate(self.driver)

	@allure.step("点击菜单栏资金运营按钮")
	def click_capital_operation(self):
		self.element_click(*self.capital_operation)

	@allure.step("跳转放款统计")
	def page_loan_statistics(self):
		self.element_click(*self.loan_statistics)
		return LoanStatistics(self.driver)