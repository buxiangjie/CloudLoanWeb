# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-25 17:11:00
@describe: 在贷统计
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class AssetLoanStatistics(Base):
	asset_loan_statistics = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查在贷统计")
	def check_asset_loan_statistics(self):
		assert self.find_element(*self.asset_loan_statistics)