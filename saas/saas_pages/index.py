# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base

class Index(Base):

	overview = (By.LINK_TEXT, "总览")

	def check_index(self):
		assert self.find_element(*self.overview)