# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-20 13:35
@describe: 
"""

import os
import pytest
import allure
import sys
import time
import random

# 把当前目录的父目录加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from datetime import datetime
from selenium import webdriver
from common.base import Base
from common.base import Option
from common.login import Login

from plms.plms_pages.index import Index


def pytest_addoption(parser):
	parser.addoption("--env", default="qa", help="运行环境")
	parser.addoption("--platform", default="win", help="运行系统类型")
	parser.addoption("--browser", default="chrome", help="浏览器名称")


@pytest.fixture(scope="session")
def env(request):
	return request.config.getoption("--env")


@pytest.fixture(scope="session")
def platform(request):
	return request.config.getoption("--platform")


@pytest.fixture(scope="session")
def browser(request):
	return request.config.getoption("--browser")


def pytest_collectstart(collector):
	collector._nodeid = f"{collector._nodeid}_{random.random()}"


def pytest_itemcollected(item):
	item._nodeid = f"{item._nodeid}_{random.random()}"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
	"""
	当测试失败的时候，自动截图，展示到html报告中
	:param item:
	:return:
	"""
	pytest_html = item.config.pluginmanager.getplugin('html')
	outcome = yield
	report = outcome.get_result()
	extra = getattr(report, 'extra', [])
	if report.when == 'call' or report.when == "setup":
		xfail = hasattr(report, 'wasxfail')
		if (report.skipped and xfail) or (report.failed and not xfail):
			_capture_screenshot()


def _capture_screenshot():
	"""截图保存为base64"""
	now_time = datetime.now().strftime("%Y%m%d%H%M%S")
	if not os.path.exists("./screenshot"):
		os.makedirs("screenshot")
	screen_path = os.path.join("screenshot", f"{now_time}.png")
	driver.save_screenshot(screen_path)
	allure.attach.file(screen_path, f"测试失败截图...{now_time}", allure.attachment_type.PNG)


@pytest.fixture(scope="session", autouse=True)
@allure.step("打开浏览器")
def drivers(request, platform, browser):
	global driver
	plat = Option(platform, browser)
	try:
		driver = webdriver.Remote(
			# 设定Node节点的URL地址，后续将通过访问这个地址连接到Node计算机
			command_executor=plat.PLATFORM,  # 要和节点机显示的ip地址一样
			desired_capabilities=plat.DESIRED,
			options=plat.OPTION
		)
	except Exception as e:
		raise e

	@allure.step("关闭浏览器")
	def fn():
		driver.quit()

	request.addfinalizer(fn)
	return driver


# @allure.step("登录神卫跳转SAAS系统")
# @pytest.fixture(scope="session", autouse=True)
# def login(drivers, env):
# 	Base(driver=drivers, url=env).open()
# 	Login(driver=drivers, url=env).login(env)

@allure.step("登录{0}环境催收系统")
@pytest.fixture(scope="session", autouse=True)
def login_plms(env, drivers):
	Base(driver=driver, url=env).open()
	Login(driver=driver, url=env).login_plms(env)


@allure.step("展开案件管理下拉列表")
@pytest.fixture(scope="function")
def case_management(env):
	time.sleep(1)
	Index(driver=driver, url=env).show_menu("0")


@allure.step("展开委案管理下拉列表")
@pytest.fixture(scope="function")
def commission_management(env):
	Index(driver=driver, url=env).show_menu("1")


@allure.step("展开还款管理下拉列表")
@pytest.fixture(scope="function")
def repayment_management(env):
	Index(driver=driver, url=env).show_menu("2")


@allure.step("展开催记管理下拉列表")
@pytest.fixture(scope="function")
def collection_management(env):
	Index(driver=driver, url=env).show_menu("3")


@allure.step("展开分案策略配置下拉列表")
@pytest.fixture(scope="function")
def assign_case_deploy(env):
	Index(driver=driver, url=env).show_menu("4")


@allure.step("展开催收公司管理下拉列表")
@pytest.fixture(scope="function")
def collection_company_management(env):
	Index(driver=driver, url=env).show_menu("5")
