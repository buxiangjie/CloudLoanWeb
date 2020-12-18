# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 委案记录
"""

import time

from common.base import Base
from selenium.webdriver.common.by import By

class CommissionRecord(Base):

	commised_amount = (By.XPATH, "//div[@class='mainWrap']/div[2]/div[1]/span[1]")

	def check_commission_record(self):
		time.sleep(1)
		assert self.get_text(*self.commised_amount) == "已委案金额汇总："