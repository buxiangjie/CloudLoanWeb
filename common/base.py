# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Bash:

	def __init__(self, driver):
		self.driver = webdriver.Chrome()

	def __open(self, url):
		self.driver.get(url)

	def open(self, url):
		self.__open(url)

	def find_element(self, *loc, time=20):
		try:
			WebDriverWait(self.driver, time).until(self.driver.find_element(loc))
			return self.find_element(loc)
		except Exception as e:
			raise str(e)

	def quit(self):
		self.quit()

	def close(self):
		self.close()

