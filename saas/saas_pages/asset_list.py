# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 17:26:00
@describe: 资产列表
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class AssetList(Base):
	asset_list = (By.CSS_SELECTOR, "h2[class=title]")
	asset_id = (By.CSS_SELECTOR, "td[class=text-center] > a")
	start_time = (By.XPATH, "//*[@id='app']/div/section/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/span[2]/span/span/input[1]")
	search = (By.XPATH, "//*[@id='app']/div/section/div/div/div/div/div[2]/div[1]/div[2]/div/div[5]/span/button[1]")


	@allure.step("检查资产列表")
	def check_asset_list(self):
		assert self.find_element(*self.asset_list)

	@allure.step("跳转资产详情")
	def page_asset_detail(self):
		self.element_click(*self.start_time)
		time_body = self.find_elements(*(By.CSS_SELECTOR, "tbody[class=ant-calendar-tbody] >tr >td"))
		loan_start_time = time_body[0]
		loan_end_time = time_body[-1]
		loan_start_time.click()
		loan_end_time.click()
		self.element_click(*self.search)
		n = self.find_elements(*self.asset_id)[0]
		n.click()
		return AssetDetail(self.driver)


class AssetDetail(Base):
	asset_detail = (By.CSS_SELECTOR, "h2[class=title]")
	ins_repayment_plan = (By.XPATH, "//*[@id='app']/div/section/div/div/div/div[2]/div/div[6]/div[1]/div/div")
	change_log = (By.CSS_SELECTOR, "div[class=my-gallery-class] > .card:nth-child(4)>div>div>div")

	@allure.step("检查资产详情")
	def check_asset_detail(self):
		assert self.find_element(*self.asset_detail)

	@allure.step("进入机构还款计划列表")
	def page_repayment_plan_list(self):
		self.element_click(*self.ins_repayment_plan)
		return RepaymentPlanList(self.driver)

	@allure.step("进入变更日志")
	def page_change_log(self):
		self.element_click(*self.change_log)
		return ChangeLog(self.driver)


class RepaymentPlanList(Base):
	repayment_plan = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查机构还款计划列表")
	def check_repayment_plan_list(self):
		assert self.find_element(*self.repayment_plan)

class ChangeLog(Base):
	change_log = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查变更日志")
	def check_change_log(self):
		assert self.find_element(*self.change_log)