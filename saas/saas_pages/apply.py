# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 16:30:00
@describe: 进件
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class Apply(Base):
	apply = (By.CSS_SELECTOR, "h2[class=title]")
	product = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(4)")
	apply_operate = (By.CSS_SELECTOR, "i[class='fa fa-eye']")
	start_time = (By.CSS_SELECTOR, "input[placeholder=开始日期]")
	end_time = (By.CSS_SELECTOR, "input[placeholder=结束日期]")
	search = (By.XPATH, "//*[@id='app']/div/section/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/span/button[1]")

	@allure.step("检查进件")
	def check_apply(self):
		assert self.find_element(*self.apply)

	@allure.step("跳转进件详情")
	def page_apply_detail(self):
		self.element_click(*self.start_time)
		time_body = self.find_elements(*(By.CSS_SELECTOR, "section > div > div > div > div > div.container-fluid > div:nth-child(1) > div.minHeight-header.thin-card-tool.card-header > div > div:nth-child(4) > div > div > div > table > tbody > tr>td"))
		apply_start_time = time_body[0]
		apply_start_time.click()
		self.element_click(*self.end_time)
		end_time_body = self.find_elements(*(By.CSS_SELECTOR, "section > div > div > div > div > div.container-fluid > div:nth-child(1) > div.minHeight-header.thin-card-tool.card-header > div > div:nth-child(5) > div > div > div > table > tbody > tr > td"))
		apply_end_time = end_time_body[-1]
		apply_end_time.click()
		self.element_click(*self.search)
		n = self.find_elements(*self.apply_operate)[0]
		n.click()
		return ApplyDetail(self.driver)


class ApplyDetail(Base):
	apply_detail = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查进件详情")
	def check_apply_detail(self):
		assert self.find_element(*self.apply_detail)
