# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 还款明细
"""

import pytest
import time

from common.base import Base
from selenium.webdriver.common.by import By
from plms.plms_pages.case_list import CaseDetail

class RepaymentDetail(Base):

	recover_amount = (By.XPATH, "//div[@class='mainWrap']/div[2]/div[1]/span[1]")
	recover_amount_2 = (By.XPATH, "//div[@class='mainWrap']/div[2]/div[1]/span[2]")
	case_id = (By.XPATH, "//tbody/tr[1]/td[3]/div/span")
	repayment_list = (By.XPATH, "//tbody")

	def check_repayment_detail(self):
		time.sleep(0.5)
		assert self.get_text(*self.recover_amount) == "回收金额汇总："
		if float(self.get_text(*self.recover_amount_2).replace(",", '')) > 0:
			for i in self.find_elements(*self.repayment_list):
				assert len(i.text) > 0

	def switch_to_case_detail(self):
		if float(self.get_text(*self.recover_amount_2)) > 0:
			self.element_click(*self.case_id)
			CaseDetail(self.driver).check_case_detail()
		else:
			pytest.xfail()