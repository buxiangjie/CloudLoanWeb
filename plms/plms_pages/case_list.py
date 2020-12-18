# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 案件列表
"""

import time

from common.base import Base
from selenium.webdriver.common.by import By
from typing import Optional


class CaseList(Base):
	"""
	案件列表页面
	"""
	summary_of_current_overdue_amounts = (By.XPATH, "//div[@class='boxWrap']/span[1]")
	off_time_button = (By.XPATH, "//i[@class='el-input__icon el-range__close-icon']")
	search_button = (By.XPATH, "//button[@type='button'][1]/span")
	list_table = (By.XPATH, "//table[@class='el-table__body']/tbody")
	case_id_button = (By.XPATH, "//table[@class='el-table__body']/tbody/tr[1]/td[2]/div/span")
	case_status_button = (By.XPATH, "//table[@class='el-table__body']/tbody/tr[1]/td[6]")
	case_status_box = (By.XPATH, "//form/div[12]/div/div/div/div/label[6]/span[1]")

	def check_case_list(self, stu: Optional[int] = None):
		"""
		检查案件列表的当前逾期金额汇总以及案件列表中是否有内容,如果无内容则断言失败
		"""
		if stu is not None:
			self.case_status_box = (By.XPATH, f"//form/div[12]/div/div/div/div/label[{stu}]/span[1]")
			self.element_click(*self.case_status_box)
		self.element_click(*self.off_time_button)
		self.element_click(*self.search_button)
		time.sleep(1)
		assert len(self.find_elements(*self.list_table)[0].text) > 0
		assert self.get_text(*self.summary_of_current_overdue_amounts) == "当前逾期金额汇总："

	def page_case_detail(self, stu: Optional[int] = None):
		"""
		:return: 返回案件详情页面对象
		"""
		self.check_case_list(stu)
		self.element_click(*self.case_id_button)
		time.sleep(1)
		return CaseDetail(self.driver)


class CaseDetail(Base):
	"""
	案件详情页面
	"""
	circulation_record = (By.XPATH, "//div[@id='circulationRecord']/div[1]/span[2]")
	asset_detail = (By.XPATH, "//div[@id='assetDetails']/div[1]/span")
	repayment_plan_detail = (By.XPATH, "//div[@id='repayPlan']/div[1]/span[2]")

	def check_case_detail(self):
		"""
		检查案件详情内容
		:return:
		"""
		assert self.get_text(*self.asset_detail) == "资产详情"

	def page_repayment_plan(self):
		"""
		:return: 返回还款计划页面对象
		"""
		self.element_click(*self.repayment_plan_detail)
		return RepaymentPlan(self.driver)

	def page_circulation_record_detail(self):
		"""
		:return: 返回流转记录页面对象
		"""
		self.element_click(*self.circulation_record)
		return CirculationRecord(self.driver)


class RepaymentPlan(Base):
	"""
	还款计划页面
	"""
	count_cur_amount = (By.XPATH, "//div[@class='box1 box']/div[2]/div[1]")
	plan_list = (By.XPATH, "//tbody")

	def check_repayment_plan(self):
		assert float(self.get_text(*self.count_cur_amount).replace(',', '')) > 0
		for i in self.find_elements(*self.plan_list):
			assert len(i.text) > 0


class CirculationRecord(Base):
	"""
	流转记录页面
	"""
	circulation_record = (By.XPATH, "//span[@class='no-redirect']")
	circulation_record_list = (By.XPATH, "//tbody")

	def check_circulation_record(self):
		for i in self.find_elements(*self.circulation_record_list):
			assert len(i.text) > 0
