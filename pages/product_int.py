# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base


class ProductInt(Base):
	product_overview = (By.LINK_TEXT, "业务概览")

	def check_product_int(self):
		assert self.find_element(*self.product_overview)
