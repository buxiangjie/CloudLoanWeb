# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base


class JoinUs(Base):
	recruitment = (By.LINK_TEXT, "人才招聘")

	@allure.step("检查人才招聘页面是否跳转成功")
	def check_join_us(self):
		assert self.find_element(*self.recruitment)
