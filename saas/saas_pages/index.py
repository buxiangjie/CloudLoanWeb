# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: saas主页
"""
import time
import allure

from selenium.webdriver.common.by import By
from common.base import Base
from saas.saas_pages.business_switch import BusinessSwitch
from saas.saas_pages.credit import Credit
from saas.saas_pages.apply import Apply
from saas.saas_pages.loan_statistics import LoanStatistics
from saas.saas_pages.repay_statistics import RepayStatistics
from saas.saas_pages.asset_list import AssetList
from saas.saas_pages.operate_log import OperateLog
from saas.saas_pages.repayment import Repayment
from saas.saas_pages.split_report import SplitReport
from saas.saas_pages.capital_flow import CapitalFlow
from saas.saas_pages.swap import Swap
from saas.saas_pages.swap_contract_confirm import SwapContractConfirm
from saas.saas_pages.profit_shareing import ProfitShareing
from saas.saas_pages.profit_shareing_2019 import ProfitShareing2019
from saas.saas_pages.quote_center import QuoteCenter
from saas.saas_pages.channel_product_quote import ChannelProductQuote


class Index(Base):
	overview = (By.CSS_SELECTOR, "h2[class=title]")
	business_switch = (By.CSS_SELECTOR, "a[title=业务开关]")
	credit = (By.CSS_SELECTOR, "a[title=授信]")
	apply = (By.CSS_SELECTOR, "a[title=进件]")
	loan_statistics = (By.CSS_SELECTOR, "a[title=借款统计]")
	repay_statistics = (By.CSS_SELECTOR, "a[title=放款统计]")
	asset_list = (By.CSS_SELECTOR, "a[href*='assetsList']")
	man = (By.CSS_SELECTOR, "ul:nth-child(3) > li:nth-child(1) > a")
	operate_log = (By.CSS_SELECTOR, "ul:nth-child(3) > li:nth-child(1) > div >button")
	repayment = (By.CSS_SELECTOR, "a[title=还款]")
	split_report = (By.CSS_SELECTOR, "a[title=分账报表]")
	swap = (By.CSS_SELECTOR, "a[title=债转]")
	swap_contract_confirm = (By.CSS_SELECTOR, "a[title=债转合同确认]")
	profit_shareing = (By.CSS_SELECTOR, "a[title=分润]")
	profit_shareing_2019 = (By.CSS_SELECTOR, "a[title=分润2019]")
	capital_flow = (By.CSS_SELECTOR, "a[title=资金流水]")
	quote_center = (By.CSS_SELECTOR, "a[href*='manageList']")
	channel_product_quote = (By.CSS_SELECTOR, "a[title=渠道产品额度]")

	def show_menu(self, menu_name: str):
		"""
		:param menu_name: 业务查询=0,财务统计=1,业务管理=2,业务统计=3
		"""
		self.excute_script(f"document.getElementsByClassName('collapse')[{menu_name}].className='collapse show'")

	def hidden_menu(self, menu_name: str):
		"""
		:param menu_name: 业务查询=0,财务统计=1,业务管理=2,业务统计=3
		"""
		self.excute_script(f"document.getElementsByClassName('collapse')[{menu_name}].className='collapse'")

	@allure.step("检查首页标题是否显示")
	def check_index(self):
		assert self.find_element(*self.overview)

	@allure.step("跳转业务开关")
	def page_business_switch(self):
		self.show_menu("2")
		time.sleep(1)
		self.element_click(*self.business_switch)
		return BusinessSwitch(self.driver)

	@allure.step("跳转授信页面")
	def page_credit(self):
		self.show_menu("0")
		time.sleep(1)
		self.element_click(*self.credit)
		return Credit(self.driver)

	@allure.step("跳转进件")
	def page_apply(self):
		self.show_menu("0")
		time.sleep(1)
		self.element_click(*self.apply)
		return Apply(self.driver)

	@allure.step("跳转借款统计")
	def page_loan_statistics(self):
		self.show_menu("3")
		time.sleep(1)
		self.element_click(*self.loan_statistics)
		return LoanStatistics(self.driver)

	@allure.step("跳转放款统计")
	def page_repay_statistics(self):
		self.show_menu("3")
		time.sleep(1)
		self.element_click(*self.repay_statistics)
		return RepayStatistics(self.driver)

	@allure.step("跳转资产列表")
	def page_asset_list(self):
		self.show_menu("0")
		time.sleep(1)
		self.element_click(*self.asset_list)
		return AssetList(self.driver)

	@allure.step("跳转操作日志")
	def page_operate_log(self):
		self.driver.refresh()
		self.element_click(*self.man)
		self.element_click(*self.operate_log)
		return OperateLog(self.driver)

	@allure.step("跳转还款")
	def page_repayment(self):
		self.show_menu("3")
		time.sleep(1)
		self.element_click(*self.repayment)
		return Repayment(self.driver)

	@allure.step("跳转分账报表")
	def page_split_report(self):
		self.show_menu("1")
		time.sleep(1)
		self.element_click(*self.split_report)
		return SplitReport(self.driver)

	@allure.step("跳转债转")
	def page_swap(self):
		self.show_menu("0")
		self.element_click(*self.swap)
		return Swap(self.driver)

	@allure.step("跳转债转合同确认")
	def page_swap_contract_confirm(self):
		self.show_menu("1")
		time.sleep(1)
		self.element_click(*self.swap_contract_confirm)
		return SwapContractConfirm(self.driver)

	@allure.step("跳转分润")
	def page_profit_shareing(self):
		self.show_menu("1")
		self.element_click(*self.profit_shareing)
		return ProfitShareing(self.driver)

	@allure.step("跳转分润2019")
	def page_profit_shareing_2019(self):
		self.show_menu("1")
		self.element_click(*self.profit_shareing_2019)
		return ProfitShareing2019(self.driver)

	@allure.step("跳转资金流水")
	def page_capital_flow(self):
		self.show_menu("1")
		self.element_click(*self.capital_flow)
		return CapitalFlow(self.driver)

	@allure.step("跳转额度中心/用户额度")
	def page_quote_center(self):
		self.show_menu("0")
		time.sleep(1)
		self.element_click(*self.quote_center)
		return QuoteCenter(self.driver)

	@allure.step("跳转渠道产品额度")
	def page_channel_product_quote(self):
		self.show_menu("2")
		time.sleep(1)
		self.element_click(*self.channel_product_quote)
		return ChannelProductQuote(self.driver)
