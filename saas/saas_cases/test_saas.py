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

	@allure.title("saas首页")
	@allure.severity("blocker")
	def test_check_index(self, drivers, saas_index):
		"""检查saas首页"""
		Index(drivers).check_index()

	@allure.title("风控配置")
	@allure.severity("blocker")
	def test_check_risk_config(self, drivers, saas_index):
		"""检查风控配置"""
		page_risk_config = Index(drivers).page_risk_config()
		page_risk_config.check_basic_rules()

	@allure.title("业务开关")
	@allure.severity("blocker")
	def test_check_business_switch(self, drivers, saas_index):
		"""检查业务开关"""
		page_business_switch = Index(drivers).page_business_switch()
		page_business_switch.check_business_switch()

	@allure.title("授信列表")
	@allure.severity("blocker")
	def test_check_credit(self, drivers, saas_index):
		"""检查授信页面"""
		page_credit = Index(drivers).page_credit()
		page_credit.check_credit()

if __name__ == '__main__':
	pytest.main()
