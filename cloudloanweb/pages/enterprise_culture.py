# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base


class EnterpriseCulture(Base):
	culture_and_mission = (By.XPATH, "//div[@class='mission']/div")

	def check_enterprise_culture(self):
		assert self.get_text(*self.culture_and_mission) == "公司使命"
