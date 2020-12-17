# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-12-11 13:30:00
@describe: 催收首页
"""

import allure

from common.base import Base
from selenium.webdriver.common.by import By

from plms.plms_pages.case_list import CaseList
from plms.plms_pages.commission_case import CommissionCase
from plms.plms_pages.commission_record import CommissionRecord
from plms.plms_pages.repayment_detail import RepaymentDetail
from plms.plms_pages.collection_list import CollectionList
from plms.plms_pages.sound_record import SoundRecord
from plms.plms_pages.strategy_list import StrategyList
from plms.plms_pages.company_list import CompanyList


class Index(Base):
	system_index = (By.XPATH, "//span[@class='no-redirect']")
	case_list_button = (By.LINK_TEXT, "案件列表")
	commission_case_button = (By.LINK_TEXT, "案件委案")
	commission_record_button = (By.LINK_TEXT, "委案记录")
	repayment_detail_button = (By.LINK_TEXT, "还款明细")
	collection_list_button = (By.LINK_TEXT, "催记")
	sound_record_button = (By.LINK_TEXT, "录音")
	strategy_list_button = (By.LINK_TEXT, "策略列表")
	company_list_button = (By.LINK_TEXT, "企业列表")

	def show_menu(self, menu_name: str):
		"""
		:param menu_name: 案件管理=0,委案管理=1,还款管理=2,催记管理=3,分案策略配置=4,催收公司管理=5
		:return:
		"""
		self.excute_script(f"document.getElementsByClassName('el-menu el-menu--inline')[{menu_name}].style='background-color: rgb(24, 51, 94);'")

	def hidden_menu(self, menu_name: str):
		"""
		:param menu_name: 案件管理=0,委案管理=1,还款管理=2,催记管理=3,分按策略配置=4,催收公司管理=5
		:return:
		"""
		self.excute_script(f"document.getElementsByClassName('el-menu el-menu--inline')[{menu_name}].style='background-color: rgb(24, 51, 94);'")

	@allure.step("检查首页")
	def check_index(self):
		assert self.find_element(*self.system_index)

	@allure.step("跳转案件列表")
	def case_list(self):
		self.element_click(*self.case_list_button)
		return CaseList(self.driver)

	@allure.step("跳转案件委案")
	def commission_case(self):
		self.element_click(*self.commission_case_button)
		return CommissionCase(self.driver)

	@allure.step("跳转委案记录")
	def commission_record(self):
		self.element_click(*self.commission_record_button)
		return CommissionRecord(self.driver)

	@allure.step("跳转还款明细")
	def repayment_detail(self):
		self.element_click(*self.repayment_detail_button)
		return RepaymentDetail(self.driver)

	@allure.step("跳转催记")
	def collection_list(self):
		self.element_click(*self.collection_list_button)
		return CollectionList(self.driver)

	@allure.step("跳转录音")
	def sound_record(self):
		self.element_click(*self.sound_record_button)
		return SoundRecord(self.driver)

	@allure.step("跳转策略列表")
	def strategy_list(self):
		self.element_click(*self.strategy_list_button)
		return StrategyList(self.driver)

	@allure.step("跳转企业列表")
	def company_list(self):
		self.element_click(*self.company_list_button)
		return CompanyList(self.driver)