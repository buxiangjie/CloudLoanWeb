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
	def test_check_index(self, drivers, login):
		"""检查saas首页"""
		Index(drivers).check_index()

	@allure.title("变更日志")
	@allure.severity("critical")
	def test_check_change_log(self, drivers, login, back_asset):
		"""检查变更日志"""
		page_change_log = Index(drivers).page_asset_list().page_asset_detail().page_change_log()
		page_change_log.check_change_log()

	@allure.title("操作日志")
	@allure.severity("normal")
	def test_check_operate_log(self, drivers, login):
		"""检查操作日志"""
		page_operate_log = Index(drivers).page_operate_log()
		page_operate_log.check_operate_log()

	@allure.title("操作日志详情")
	@allure.severity("normal")
	def test_check_operate_log_detail(self, drivers, login):
		"""检查操作日志详情"""
		page_operate_log_detail = Index(drivers).page_operate_log().page_operate_log_detail()
		page_operate_log_detail.check_operate_log_detail()

	@allure.title("风控配置")
	@allure.severity("blocker")
	def test_check_risk_config(self, drivers, login):
		"""检查风控配置"""
		page_risk_config = Index(drivers).page_risk_config()
		page_risk_config.check_basic_rules()

	@allure.title("业务开关")
	@allure.severity("blocker")
	def test_check_business_switch(self, drivers, login):
		"""检查业务开关"""
		page_business_switch = Index(drivers).page_business_switch()
		page_business_switch.check_business_switch()

	@allure.title("授信")
	@allure.severity("blocker")
	def test_check_credit(self, drivers, login, back_risk):
		"""检查授信页面"""
		page_credit = Index(drivers).page_credit()
		page_credit.check_credit()

	@allure.title("授信详情")
	@allure.severity("blocker")
	def test_check_credit_detail(self, drivers, login, back_risk):
		"""检查授信详情"""
		page_credit = Index(drivers).page_credit()
		page_credit_detail = page_credit.page_credit_detail()
		page_credit_detail.check_credit_detail()
		page_credit_detail.check_member_message()

	@allure.title("授信统计")
	@allure.severity("critical")
	def test_check_credit_statistics(self, drivers, login, back_risk):
		"""检查授信统计"""
		page_credit_statistics = Index(drivers).page_credit_statistics()
		page_credit_statistics.check_credit_statistics()

	@allure.title("进件")
	@allure.severity("blocker")
	def test_check_apply(self, drivers, login, back_risk):
		"""检查进件页面"""
		page_apply = Index(drivers).page_apply()
		page_apply.check_apply()

	@allure.title("进件详情")
	@allure.severity("blocker")
	def test_check_apply_detail(self, drivers, login, back_risk):
		"""检查进件详情"""
		page_apply_detail = Index(drivers).page_apply().page_apply_detail()
		page_apply_detail.check_apply_detail()

	@allure.title("进件统计")
	@allure.severity("critical")
	def test_check_apply_statistics(self, drivers, login, back_risk):
		"""检查进件统计"""
		page_apply_statistics = Index(drivers).page_apply_statistics()
		page_apply_statistics.check_apply_statistics()

	@allure.title("迁徙率")
	@allure.severity("critical")
	def test_check_migration_rate(self, drivers, login, back_risk):
		"""检查迁徙率"""
		page_migration_rate = Index(drivers).page_migration_rate()
		page_migration_rate.check_migration_rate()

	@allure.title("放款统计")
	@allure.severity("critical")
	def test_check_loan_statistics(self, drivers, login, back_capital):
		"""检查放款统计"""
		page_loan_statistics = Index(drivers).page_loan_statistics()
		page_loan_statistics.check_loan_statistics()

	@allure.title("还款统计")
	@allure.severity("critical")
	def test_check_repay_statistics(self, drivers, login, back_capital):
		"""检查还款统计"""
		page_repay_statistics = Index(drivers).page_repay_statistics()
		page_repay_statistics.check_repay_statistics()

	@allure.title("资产列表")
	@allure.severity("blocker")
	def test_check_asset_list(self, drivers, login, back_asset):
		"""检查资产列表"""
		page_asset_list = Index(drivers).page_asset_list()
		page_asset_list.check_asset_list()

	@allure.title("资产详情")
	@allure.severity("blocker")
	def test_check_asset_detail(self, drivers, login, back_asset):
		"""检查资产详情"""
		page_asset_detail = Index(drivers).page_asset_list().page_asset_detail()
		page_asset_detail.check_asset_detail()

	@allure.title("机构还款计划")
	@allure.severity("blocker")
	def test_check_repayment_plan(self, drivers, login, back_asset):
		"""检查机构还款计划"""
		page_repayment_plan = Index(drivers).page_asset_list().page_asset_detail().page_repayment_plan_list()
		page_repayment_plan.check_repayment_plan_list()

	@allure.title("在贷统计")
	@allure.severity("critical")
	def test_check_asset_loan_statistics(self, drivers, login, back_asset):
		"""检查在贷统计"""
		page_asset_loan_statistics = Index(drivers).page_asset_loan_statistics()
		page_asset_loan_statistics.check_asset_loan_statistics()


if __name__ == '__main__':
	pytest.main()
