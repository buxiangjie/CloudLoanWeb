# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 企业列表
"""

from selenium.webdriver.common.by import By
from common.base import Base

class CompanyList(Base):

	company_name = (By.XPATH, "//form[@class='el-form reqForm el-form--inline']/div[1]/label")

	def check_company_list(self):
		assert self.get_text(*self.company_name) == "催收公司名称："