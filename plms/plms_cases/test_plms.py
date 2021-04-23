# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import pytest
import allure
import random

from plms.plms_pages.index import Index


@allure.feature(f"催收系统{random.random()}")
class TestPlms:

	@allure.title("首页")
	def test_index(self, drivers):
		Index(drivers).check_index()

	@allure.title("检查案件列表")
	def test_check_case_list(self, drivers, case_management):
		Index(drivers).case_list().check_case_list()

	@allure.title("检查案件详情")
	def test_check_case_detail(self, drivers, case_management):
		page_case_detail = Index(drivers).case_list().page_case_detail()
		page_case_detail.check_case_detail()

	@allure.title("检查还款计划")
	def test_check_repayment_plan(self, drivers, case_management):
		page_repayment_plan = Index(drivers).case_list().page_case_detail().page_repayment_plan()
		page_repayment_plan.check_repayment_plan()

	@allure.title("检查流转记录")
	def test_check_circulation_record(self, drivers, case_management):
		page_circulation_record = Index(drivers).case_list().page_case_detail(stu=6).page_circulation_record_detail()
		page_circulation_record.check_circulation_record()

	@allure.title("检查案件委案")
	def test_check_commission_case(self, drivers, commission_management):
		page_commission_case = Index(drivers).commission_case()
		page_commission_case.check_commission_case()

	@allure.title("检查案件委案跳转案件详情")
	def test_check_commission_switch_to_case_detail(self, drivers, commission_management):
		Index(drivers).commission_case().check_switch_to_case_detail()

	@allure.title("检查委案记录")
	def test_check_commission_record(self, drivers, commission_management):
		Index(drivers).commission_record().check_commission_record()

	@allure.title("检查还款明细")
	def test_check_repayment_detail(self, drivers, repayment_management):
		page_repayment_detail = Index(drivers).repayment_detail()
		page_repayment_detail.check_repayment_detail()

	@allure.title("检查还款明细跳转案件详情")
	def test_check_repayment_detail_switch_to_case_detail(self, drivers, repayment_management):
		page_repayment_detail = Index(drivers).repayment_detail()
		page_repayment_detail.switch_to_case_detail()

	@allure.title("检查催记")
	def test_check_collection_list(self, drivers, collection_management):
		page_collection_list = Index(drivers).collection_list()
		page_collection_list.check_collection_list()

	@allure.title("检查录音")
	def test_check_sound_record(self, drivers, collection_management):
		page_sound_record = Index(drivers).sound_record()
		page_sound_record.check_sound_record()

	@allure.title("检查策略列表")
	def test_check_strategy_list(self, drivers, assign_case_deploy):
		page_strategy_list = Index(drivers).strategy_list()
		page_strategy_list.check_strategy_list()

	@allure.title("检查企业列表")
	def test_check_company_list(self, drivers, collection_company_management):
		page_company_list = Index(drivers).company_list()
		page_company_list.check_company_list()


if __name__ == '__main__':
	pytest.main()
