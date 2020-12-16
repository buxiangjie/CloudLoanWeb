# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""
import datetime
import os
import platform
import allure
import sys
import yaml

# 把当前目录的父目录加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import Optional, Union

from config.configer import Config


class Base:

	def __init__(self, driver, url="cloudloanweb_prod"):
		# self.driver = webdriver.Chrome()
		self.driver = driver
		self.url = Config().get_item("URL", url)

	@allure.step("打开页面")
	def open(self):
		self.driver.get(self.url)

	@allure.step("查找元素")
	def find_element(self, *loc: tuple, times=20):
		try:
			WebDriverWait(self.driver, times).until(EC.visibility_of_all_elements_located(loc))
			return self.driver.find_element(*loc)
		except Exception:
			raise

	@allure.step("查找多元素")
	def find_elements(self, *loc: tuple, times=20) -> list:
		try:
			WebDriverWait(self.driver, times).until(EC.visibility_of_all_elements_located(loc))
			return self.driver.find_elements(*loc)
		except Exception:
			raise

	@allure.step("向元素:{2},输入文本{text}")
	def send_keys(self, *loc: tuple, text: str, is_clear: bool=False):
		try:
			if is_clear is True:
				self.find_element(*loc).clear()
				self.find_element(*loc).send_keys(text)
			else:
				self.find_element(*loc).send_keys(text)
		except Exception:
			raise

	@allure.step("获取元素文本")
	def get_text(self, *loc: tuple) -> str:
		try:
			return self.find_element(*loc).text
		except Exception:
			raise

	@allure.step("点击元素:{2}")
	def element_click(self, *loc: tuple):
		try:
			self.find_element(*loc).click()
		except Exception:
			raise

	@allure.step("执行JS:{js}")
	def excute_script(self, js: str, element: bool=False):
		"""执行JS命令"""
		try:
			self.driver.execute_script(js, element)
		except Exception:
			raise

	@allure.step("滚动屏幕")
	def scroll(self, x: Optional[str], y: Optional[str], element= None):
		"""滚动屏幕"""
		try:
			if element:
				self.excute_script("arguments[0].scrollIntoView();", element)
			else:
				self.excute_script(f"window.scrollBy({x},{y})")
		except Exception:
			raise


class Common:

	@staticmethod
	@allure.step("获取driver地址")
	def get_driver_path() -> str:
		fi = ""
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
		except Exception:
			raise

	@staticmethod
	def get_new_time(when: str, what: str, num: int) -> str:
		"""
		:param when: before or after
		:param what: days,minutes,seconds,hours,weeks
		:param num: how long time
		:return: for example 2020-07-28 11:11:11
		"""
		times = datetime.datetime.now()
		new_times = ""
		if when == "after":
			if what == "days":
				new_times = times + datetime.timedelta(days=num)
			elif what == "hours":
				new_times = times + datetime.timedelta(hours=num)
			elif what == "seconds":
				new_times = times + datetime.timedelta(seconds=num)
			elif what == "minutes":
				new_times = times + datetime.timedelta(minutes=num)
			elif what == "weeks":
				new_times = times + datetime.timedelta(weeks=num)
		elif when == "before":
			if what == "days":
				new_times = times - datetime.timedelta(days=num)
			elif what == "hours":
				new_times = times - datetime.timedelta(hours=num)
			elif what == "seconds":
				new_times = times - datetime.timedelta(seconds=num)
			elif what == "minutes":
				new_times = times - datetime.timedelta(minutes=num)
			elif what == "weeks":
				new_times = times - datetime.timedelta(weeks=num)
		return str(new_times).split(".")[0]