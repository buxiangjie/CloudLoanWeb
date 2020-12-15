# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 案件列表
"""

from common.base import Base
from selenium.webdriver.common.by import By

class CaseList(Base):

	summary_of_current_overdue_amounts = (By.XPATH, "//div[@class='boxWrap']/span[1]")
	off_time_button = (By.XPATH, "//i[@class='el-input__icon el-range__close-icon']")
	search_button = (By.XPATH, "//button[@type='button'][1]/span")

	def check_case_list(self):
		self.element_click(*self.off_time_button)
		self.element_click(*self.search_button)
		assert self.get_text(*self.summary_of_current_overdue_amounts) == "当前逾期金额汇总："
