# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 16:40:00
@describe: 进件统计
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class ApplyStatistics(Base):

	apply_statistics = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查进件统计")
	def check_apply_statistics(self):
		assert self.find_element(*self.apply_statistics)