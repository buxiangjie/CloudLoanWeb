# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 09:33:00
@describe: 债转合同确认
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class SwapContractConfirm(Base):

	swap_contract_confirm = (By.CSS_SELECTOR, "h2[class=title]")

	@allure.step("检查债转合同确认")
	def check_swap_contract_confirm(self):
		assert self.find_element(*self.swap_contract_confirm)