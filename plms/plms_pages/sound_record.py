# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 录音
"""

import time

from selenium.webdriver.common.by import By
from common.base import Base

class SoundRecord(Base):

	sound_record_id = (By.XPATH, "//form[@class='el-form reqForm el-form--inline']/div[1]/label")

	def check_sound_record(self):
		time.sleep(1)
		assert self.get_text(*self.sound_record_id) == "录音ID："