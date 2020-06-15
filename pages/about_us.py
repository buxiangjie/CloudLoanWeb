# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base


class AboutUs(Base):
	company_profile = (By.LINK_TEXT, "公司简介")

	def check_about_us(self):
		raise self.find_element(*self.company_profile)
