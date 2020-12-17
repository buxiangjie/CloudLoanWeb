# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 催记
"""

from selenium.webdriver.common.by import By
from common.base import Base

class CollectionList(Base):

	import_collect_record = (By.XPATH, "//div[@class='btnWrap greenColor']/span")

	def check_collection_list(self):
		assert self.get_text(*self.import_collect_record) == "催记导入"