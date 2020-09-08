# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 17:26:00
@describe: 资产列表
"""

import allure
import time

from selenium.webdriver.common.by import By
from common.base import Base


class AssetList(Base):
	asset_list = (By.CSS_SELECTOR, "h2[class=title]")
	asset_id = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(1) > a")
	start_time = (By.XPATH,
				  "//*[@id='app']/div/section/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/span[2]/span/span/input[1]")
	search = (By.XPATH, "//*[@id='app']/div/section/div/div/div/div/div[2]/div[1]/div[2]/div/div[5]/span/button[1]")
	product_name = (By.CSS_SELECTOR, ".muselect-header > div > div:nth-child(1) > div > ul > li:nth-child(12) > img")

	@allure.step("检查资产列表")
	def check_asset_list(self):
		assert self.find_element(*self.asset_list).text == "资产列表"

	@allure.step("跳转资产详情")
	def page_asset_detail(self):
		self.element_click(*self.start_time)
		time_body = self.find_elements(*(By.CSS_SELECTOR, "tbody[class=ant-calendar-tbody] >tr >td"))
		loan_start_time = time_body[0]
		loan_end_time = time_body[-1]
		loan_start_time.click()
		loan_end_time.click()
		self.element_click(*self.product_name)
		self.element_click(*self.search)
		time.sleep(1)
		self.element_click(*self.asset_id)
		return AssetDetail(self.driver)


class AssetDetail(Base):
	asset_detail = (By.CSS_SELECTOR, "h2[class=title]")
	ins_repayment_plan = (By.XPATH, "//*[@id='app']/div/section/div/div/div/div[2]/div/div[6]/div[1]/div/div")
	change_log = (By.CSS_SELECTOR, "div[class=my-gallery-class] > .card:nth-child(4)>div>div>div")

	@allure.step("检查资产详情")
	def check_asset_detail(self):
		assert self.find_element(*self.asset_detail).text == "资产详情"

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
	relief = (By.CSS_SELECTOR, "a[href*=reliefApply]")

	@allure.step("检查机构还款计划列表")
	def check_repayment_plan_list(self):
		assert self.find_element(*self.repayment_plan).text == "机构还款计划"

	@allure.step("进入减免申请页面")
	def page_relief(self):
		self.element_click(*self.relief)
		return Relief(self.driver)


class ChangeLog(Base):
	change_log = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查变更日志")
	def check_change_log(self):
		assert self.find_element(*self.change_log).text == "变更日志"


class Relief(Base):
	relief = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查减免申请")
	def check_relief(self):
		assert self.find_element(*self.relief).text == "减免申请"