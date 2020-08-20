# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import os
import platform
import allure
import sys
import yaml

# 把当前目录的父目录加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.configer import Config


class Base:

	def __init__(self, driver, url="cloudloanweb_prod"):
		self.driver = driver
		self.url = Config().get_item("URL", url)

	@allure.step("打开浏览器")
	def open(self):
		self.driver.get(self.url)

	@allure.step("查找元素")
	def find_element(self, *loc: tuple, times=20):
		try:
			WebDriverWait(self.driver, times).until(EC.visibility_of_all_elements_located(loc))
			return self.driver.find_element(*loc)
		except Exception as e:
			raise e

	def send_keys(self, *loc, text, is_clear=True):
		try:
			if is_clear is True:
				self.find_element(*loc).clear()
				self.find_element(*loc).send_keys(text)
			else:
				self.find_element(*loc).send_keys(text)
		except Exception as e:
			raise e

	@allure.step("点击按钮")
	def element_click(self, *loc: tuple):
		try:
			self.find_element(*loc).click()
		except Exception as e:
			raise e

	def excute_script(self, js: str, element=None):
		"""执行JS命令"""
		self.driver.execute_script(js, element)

	def scroll(self, x=None, y=None, element= None):
		"""滚动屏幕"""
		try:
			if element:
				self.excute_script("arguments[0].scrollIntoView();", element)
			else:
				self.excute_script(f"window.scrollBy({x},{y})")
		except Exception as e:
			raise e


class Common:

	@staticmethod
	@allure.step("获取driver地址")
	def get_driver_path():
		global fi
		if platform.system() == "Darwin":
			fi = Config().get_item("DriverPath", "Darwin")
		elif platform.system() == "Windows":
			fi = Config().get_item("DriverPath", "Windows")
		chrome_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + fi
		return chrome_path

	@staticmethod
	def get_yaml_data(file, filename: str) -> dict:
		"""读取yaml文件数据"""
		try:
			file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f'''/{file}/'''
			with open(file + filename, 'rb') as f:
				data = f.read()
			datas = yaml.load(data, Loader=yaml.FullLoader)
			return datas
		except Exception as e:
			raise e