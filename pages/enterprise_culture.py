# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base


class EnterpriseCulture(Base):
	culture_and_mission = (By.LINK_TEXT, "文化及使命")

	def check_enterprise_culture(self):
		raise self.find_element(*self.culture_and_mission)
