# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-21 15:26:00
@describe: 授信页面
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class Credit(Base):
	title = (By.CSS_SELECTOR, "h2[class=title]")
	credit_operate = (By.CSS_SELECTOR, "tbody > tr:nth-child(1) > td:nth-child(9) > a > i")
	product = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(4)")
	product_name = (By.CSS_SELECTOR, "li[class=select-ul-item] > img")
	search = (By.CSS_SELECTOR, "span[class=muselect-btn] > button:nth-child(1)")
	search_detail = (By.CSS_SELECTOR, "tbody > tr")

	@allure.step("检查授信列表")
	def check_credit(self):
		self.find_element(*self.title)

	@allure.step("跳转授信详情页面")
	def page_credit_detail(self):
		y = self.find_element(*self.product).text
		self.element_click(*self.credit_operate)
		return CreditDetail(self.driver, y)

	@allure.step("根据产品名称牙医贷筛选-检查筛选结果")
	def product_name_search(self):
		self.find_elements(*self.product_name)[4].click()
		self.element_click(*self.search)
		for i in self.find_elements(*self.search_detail):
			assert "牙医贷" in i.text


class CreditDetail(Base):
	def __init__(self, driver, y):
		super().__init__(driver)
		self.y = y
	credit_detail = (By.CSS_SELECTOR, "h2[class='title']")
	member_message = (By.CSS_SELECTOR, "h5[class='card-title']")

	@allure.step("检查授信详情页面")
	def check_credit_detail(self):
		assert self.find_element(*self.credit_detail)

	@allure.step("检查授信详情页面客户信息")
	def check_member_message(self):
		l = [x.text for x in self.find_elements(*self.member_message)]
		if self.y == "牙医贷":
			assert "诊所信息" in l
		elif self.y in ("罗马车贷", "罗马车贷 (新)"):
			assert "企业信息" in l