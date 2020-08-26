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

	@allure.step("检查渠道产品额度")
	def check_channel_product_quote(self):
		assert self.find_element(*self.channel_product_quote)