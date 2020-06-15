# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base


class JoinUs(Base):
	recruitment = (By.LINK_TEXT, "人才招聘")

	def check_join_us(self):
		raise self.find_element(*self.recruitment)
