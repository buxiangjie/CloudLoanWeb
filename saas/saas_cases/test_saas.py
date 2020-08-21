# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 测试用例
"""
import allure
import pytest

from saas.saas_pages.index import Index


@allure.feature("SAAS系统测试")
class TestSaas:

	def test_check_index(self, drivers, saas_index):
		"""检查saas首页"""
		Index(drivers).check_index()


if __name__ == '__main__':
	pytest.main()
