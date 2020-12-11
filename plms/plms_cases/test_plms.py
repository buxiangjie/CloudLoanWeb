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
	def test_index(self, drivers, login_plms):
		Index(drivers).check_index()


if __name__ == '__main__':
	pytest.main()