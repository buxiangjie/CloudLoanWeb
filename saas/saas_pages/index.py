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
from saas.saas_pages.risk_config import RiskConfig
from saas.saas_pages.business_switch import BusinessSwitch
from saas.saas_pages.credit import Credit
from saas.saas_pages.credit_statistics import CreditStatistics
from saas.saas_pages.apply import Apply
from saas.saas_pages.apply_statistics import ApplyStatistics
from saas.saas_pages.migration_rate import MigrationRate
from saas.saas_pages.loan_statistics import LoanStatistics
from saas.saas_pages.repay_statistics import RepayStatistics
from saas.saas_pages.asset_list import AssetList
from saas.saas_pages.operate_log import OperateLog
from saas.saas_pages.asset_loan_statistics import AssetLoanStatistics
from saas.saas_pages.split import Split
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
	risk_config = (By.CSS_SELECTOR, "a[title=风控配置]")
	business_switch = (By.CSS_SELECTOR, "a[title=业务开关]")
	risk = (By.CSS_SELECTOR, "div[title=风控]")
	credit = (By.CSS_SELECTOR, "a[title=授信]")
	credit_statistics = (By.CSS_SELECTOR, "a[title=授信统计]")
	apply = (By.CSS_SELECTOR, "a[title=进件]")
	apply_statistics = (By.CSS_SELECTOR, "a[title=进件统计]")
	migration_rate = (By.CSS_SELECTOR, "a[title=迁徙率]")
	capital_operation = (By.CSS_SELECTOR, "div[title=资金运营]")
	loan_statistics = (By.CSS_SELECTOR, "a[title=放款统计]")
	repay_statistics = (By.CSS_SELECTOR, "a[title=还款统计]")
	asset = (By.CSS_SELECTOR, "div[title=资产]")
	asset_list = (By.CSS_SELECTOR, "a[href*='assetsList']")
	asset_loan_statistics = (By.CSS_SELECTOR, "a[title=在贷统计]")
	man = (By.CSS_SELECTOR, "ul:nth-child(3) > li:nth-child(1) > a")
	operate_log = (By.CSS_SELECTOR, "ul:nth-child(3) > li:nth-child(1) > div >button")
	finance = (By.CSS_SELECTOR, "div[title=财务]")
	split = (By.CSS_SELECTOR, "a[title=分账]")
	split_report = (By.CSS_SELECTOR, "a[title=分账报表]")
	swap = (By.CSS_SELECTOR, "a[title=债转]")
	swap_contract_confirm = (By.CSS_SELECTOR, "a[title=债转合同确认]")
	profit_shareing = (By.CSS_SELECTOR, "a[title=分润]")
	profit_shareing_2019 = (By.CSS_SELECTOR, "a[title=分润2019]")
	capital_flow = (By.CSS_SELECTOR, "a[title=资金流水]")
	member_quota_management = (By.CSS_SELECTOR, "div[title='用户/额度管理']")
	quote_center = (By.CSS_SELECTOR, "a[href*='manageList']")
	channel_product_quote = (By.CSS_SELECTOR, "a[title=渠道产品额度]")

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

	def show_menu(self, menu_name: str):
		"""
		:param menu_name: 风控=0,资金运营=1,资产=2,财务=3,用户/额度管理=4
		"""
		self.excute_script(f"document.getElementsByClassName('collapse')[{menu_name}].className='collapse show'")

	def hidden_menu(self, menu_name: str):
		"""
		:param menu_name: 风控=0,资金运营=1,资产=2,财务=3,用户/额度管理=4
		"""
		self.excute_script(f"document.getElementsByClassName('collapse')[{menu_name}].className='collapse'")

	@allure.step("跳转授信页面")
	def page_credit(self):
		self.show_menu("0")
		self.element_click(*self.credit)
		return Credit(self.driver)

	@allure.step("跳转授信统计")
	def page_credit_statistics(self):
		self.show_menu("0")
		self.element_click(*self.credit_statistics)
		return CreditStatistics(self.driver)

	@allure.step("跳转进件")
	def page_apply(self):
		self.show_menu("0")
		self.element_click(*self.apply)
		return Apply(self.driver)

	@allure.step("跳转进件统计")
	def page_apply_statistics(self):
		self.show_menu("0")
		self.element_click(*self.apply_statistics)
		return ApplyStatistics(self.driver)

	@allure.step("跳转迁徙率")
	def page_migration_rate(self):
		self.show_menu("0")
		self.element_click(*self.migration_rate)
		return MigrationRate(self.driver)

	@allure.step("跳转放款统计")
	def page_loan_statistics(self):
		self.show_menu("1")
		self.element_click(*self.loan_statistics)
		return LoanStatistics(self.driver)

	@allure.step("跳转还款统计")
	def page_repay_statistics(self):
		self.show_menu("1")
		self.element_click(*self.repay_statistics)
		return RepayStatistics(self.driver)

	@allure.step("跳转资产列表")
	def page_asset_list(self):
		self.show_menu("2")
		self.element_click(*self.asset_list)
		return AssetList(self.driver)

	@allure.step("跳转操作日志")
	def page_operate_log(self):
		self.driver.refresh()
		self.element_click(*self.man)
		self.element_click(*self.operate_log)
		return OperateLog(self.driver)

	@allure.step("跳转在贷统计")
	def page_asset_loan_statistics(self):
		self.show_menu("2")
		self.element_click(*self.asset_loan_statistics)
		return AssetLoanStatistics(self.driver)

	@allure.step("跳转分账")
	def page_split(self):
		self.show_menu("3")
		self.element_click(*self.split)
		return Split(self.driver)

	@allure.step("跳转分账报表")
	def page_split_report(self):
		self.show_menu("3")
		self.element_click(*self.split_report)
		return SplitReport(self.driver)

	@allure.step("跳转债转")
	def page_swap(self):
		self.show_menu("3")
		self.element_click(*self.swap)
		return Swap(self.driver)

	@allure.step("跳转债转合同确认")
	def page_swap_contract_confirm(self):
		self.show_menu("3")
		self.element_click(*self.swap_contract_confirm)
		return SwapContractConfirm(self.driver)

	@allure.step("跳转分润")
	def page_profit_shareing(self):
		self.show_menu("3")
		self.element_click(*self.profit_shareing)
		return ProfitShareing(self.driver)

	@allure.step("跳转分润2019")
	def page_profit_shareing_2019(self):
		self.show_menu("3")
		self.element_click(*self.profit_shareing_2019)
		return ProfitShareing2019(self.driver)

	@allure.step("跳转资金流水")
	def page_capital_flow(self):
		self.show_menu("3")
		self.element_click(*self.capital_flow)
		return CapitalFlow(self.driver)

	@allure.step("跳转额度中心")
	def page_quote_center(self):
		time.sleep(1)
		self.show_menu("4")
		time.sleep(1)
		self.element_click(*self.quote_center)
		return QuoteCenter(self.driver)

	@allure.step("跳转渠道产品额度")
	def page_channel_product_quote(self):
		time.sleep(1)
		self.show_menu("4")
		self.element_click(*self.channel_product_quote)
		return ChannelProductQuote(self.driver)
