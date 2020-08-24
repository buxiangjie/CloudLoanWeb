# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-24 16:50:00
@describe: 迁徙率
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class MigrationRate(Base):

	migration_rate = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查迁徙率")
	def check_migration_rate(self):
		assert self.find_element(*self.check_migration_rate)