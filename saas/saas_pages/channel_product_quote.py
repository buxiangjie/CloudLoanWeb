# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-26 13:41:00
@describe: 渠道产品额度
"""

import allure

from selenium.webdriver.common.by import By
from common.base import Base

class ChannelProductQuote(Base):
	channel_product_quote = (By.CSS_SELECTOR, "h2[class=title]")
	adjustment_channel_quote_button = (By.XPATH, "//*[@id='DataTables_Table_4']/tbody/tr[1]/td[9]/span")
	confirm = (By.CSS_SELECTOR, "div[class=modal-btns] > button:nth-child(2)")
	back_button = (By.CSS_SELECTOR, "button[class=confirm]")
	confirm_text = (By.CSS_SELECTOR, "div[data-allow-outside-click=false] > h2")

	@allure.step("检查渠道产品额度")
	def check_channel_product_quote(self):
		assert self.find_element(*self.channel_product_quote)

	@allure.step("调整渠道额度")
	def adjustment_channel_quote(self):
		self.element_click(*self.adjustment_channel_quote_button)
		self.element_click(*self.confirm)
		assert self.find_element(*self.confirm_text).text == "渠道额度调整完成!"
		self.element_click(*self.back_button)