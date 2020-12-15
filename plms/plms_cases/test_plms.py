# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import pytest
import allure

from plms.plms_pages.index import Index



@allure.feature("催收系统")
class TestPlms:

	@allure.title("首页")
	def test_index(self, drivers):
		Index(drivers).check_index()

	@allure.title("检查案件列表")
	def test_check_case_list(self, drivers, case_management):
		Index(drivers).case_list().check_case_list()

	@allure.title("检查列表内容")
	def test_check_case_list_detail(self, drivers, case_management):
		Index(drivers).case_list().check_case_list_detail()


if __name__ == '__main__':
	pytest.main()