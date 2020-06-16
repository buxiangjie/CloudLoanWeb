# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium.webdriver.common.by import By
from common.base import Base


class News(Base):
	company_news = (By.LINK_TEXT, "公司要闻")

	def check_news(self):
		assert self.find_element(*self.company_news)
