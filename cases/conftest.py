# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import os
import pytest
import base64
import allure
import shutil

from datetime import datetime
from common.base import Common
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from py._xmlgen import html


# def pytest_html_report_title(report):
# 	"""修改文件标题"""
# 	report.title = "CloudLoan Test Report"


# def pytest_configure(config):
# 	"""修改环境信息"""
# 	config._metadata['ProjectName'] = "CloudLoanWeb"
# 	config._metadata['ProjectAddress'] = "https://www.github.com/buxiangjie/CloudLoanWeb"
# 	config._metadata['JAVA_HOME'] = "0"
# 	config._metadata.pop("JAVA_HOME")

# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
# 	cells.insert(2, html.th('Description'))
# 	cells.pop()
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
# 	cells.insert(2, html.td(report.description))
# 	cells.pop()


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
			screen_img = _capture_screenshot()
			if screen_img:
				htmls = f'''<div><img src="data:image/png;base64,{screen_img}"
						alt="screenshot" style="width:1024px;height:768px;"
						οnclick="window.open(this.src)" align="right"/></div>'''
				extra.append(pytest_html.extras.html(htmls))
		report.extra = extra
		# report.description = str(item.function.__doc__)


def _capture_screenshot():
	"""截图保存为base64"""
	now_time = datetime.now().strftime("%Y%m%d%H%M%S")
	if not os.path.exists("./screenshot"):
		os.makedirs("screenshot")
	screen_path = os.path.join("screenshot", f"{now_time}.png")
	driver.save_screenshot(screen_path)
	allure.attach.file(screen_path, f"测试失败截图...{now_time}", allure.attachment_type.PNG)
	with open(screen_path, 'rb') as f:
		imagebase64 = base64.b64encode(f.read())
	return imagebase64.decode()


@pytest.fixture(scope='function', autouse=True)
@allure.step("打开浏览器")
def drivers(request):
	global driver
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--window-size=1920,1080')
	driver = webdriver.Chrome(options=chrome_options, executable_path=Common.get_driver_path)
	print(f"浏览器{driver}")

	@allure.step("关闭浏览器")
	def fn():
		driver.quit()
		if os.path.exists("./screenshot"):
			shutil.rmtree("./screenshot")
	request.addfinalizer(fn)
	return driver