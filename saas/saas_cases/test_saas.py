# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""
import allure
import pytest

from saas.saas_pages.index import Index
from saas.saas_pages.login import Login
from common.base import Base


@allure.feature("SAAS系统测试")
class TestSaas:

	@allure.step("登录神卫跳转SAAS系统")
	@pytest.fixture(scope="function")
	def saas_index(self, drivers, env):
		Base(driver=drivers, url=env).open()
		Login(driver=drivers, url=env).login(env)

	def test_check_index(self, drivers, saas_index):
		Index(drivers).check_index()

if __name__ == '__main__':
	pytest.main()