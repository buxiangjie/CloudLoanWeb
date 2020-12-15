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


class Index(Base):
	system_index = (By.XPATH, "//span[@class='no-redirect']")
	case_list_button = (By.LINK_TEXT, "案件列表")
	commission_case = (By.LINK_TEXT, "案件委案")

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
		self.element_click(*self.commission_case)
		return CommissionCase(self.driver)
