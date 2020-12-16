# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from common.base import Base
from selenium.webdriver.common.by import By
from plms.plms_pages.case_list import CaseDetail

class CommissionCase(Base):
	"""
	案件委案页面
	"""
	no_commission_amount = (By.XPATH, "//div[@class='mainWrap']/div[2]/div/span[1]")
	case_status_box = (By.XPATH, "//form/div[12]/div/div/div/div/label[1]/span[1]") #待分发
	search_button = (By.XPATH, "//div[@class='elFormItemBtn']/div/div/button[1]/span")
	commission_list = (By.XPATH, "//tbody")
	case_id = (By.XPATH, "//tbody/tr[1]/td[2]/div/span")

	def check_commission_case(self):
		self.element_click(*self.case_status_box)
		self.element_click(*self.search_button)
		assert self.get_text(*self.no_commission_amount) == "未委案金额汇总："
		for i in self.find_elements(*self.commission_list):
			assert len(i.text) > 0

	def check_switch_to_case_detail(self):
		self.element_click(*self.case_id)
		CaseDetail(self.driver).check_case_detail()
