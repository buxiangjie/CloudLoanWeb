# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 登录神卫
"""

from selenium.webdriver.common.by import By
from common.base import Base
from common.base import Common

class Login(Base):

	account_number = (By.CSS_SELECTOR, "input[placeholder='请输入账号']")
	password = (By.CSS_SELECTOR, "input[type='password']")
	sms_code = (By.CSS_SELECTOR, "input[placeholder='请输入短信验证码']")
	login_button = (By.CSS_SELECTOR, "[type=button]:nth-child(1)")

	def login(self, env: str):
		user_data = Common.get_yaml_data("config", "user_data.yaml")
		self.send_keys(*self.account_number, text=user_data[env]["username"])
		self.send_keys(*self.password, text=user_data[env]["password"])
		self.send_keys(*self.sms_code, text="1")
		self.element_click(*self.login_button)