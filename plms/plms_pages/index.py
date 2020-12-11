# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-12-11 13:30:00
@describe: 催收首页
"""

import allure

from common.base import Base
from selenium.webdriver.common.by import By


class Index(Base):
	system_index = (By.XPATH, "//span[@class='no-redirect']")

	def show_menu(self, menu_name: str):
		"""
		:param menu_name: 案件管理=0,委案管理=1,还款管理=2,催记管理=3,分按策略配置=4,催收公司管理=5
		:return:
		"""
		self.excute_script(
			f"""
				document.getElementsByClassName('el-menu el-menu--inline')
				[{menu_name}].style="'background-color: rgb(24, 51, 94);'
			"""
		)

	def hidden_menu(self, menu_name: str):
		"""
		:param menu_name: 案件管理=0,委案管理=1,还款管理=2,催记管理=3,分按策略配置=4,催收公司管理=5
		:return:
		"""
		self.excute_script(
			f"""
				document.getElementsByClassName('el-menu el-menu--inline')
				[{menu_name}].style="'background-color: rgb(24, 51, 94);'
			"""
		)

	@allure.step("检查首页")
	def check_index(self):
		assert self.find_element(*self.system_index)
