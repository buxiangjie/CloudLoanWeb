# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-08-20 13:35
@describe: 
"""

import os
import pytest
import base64
import allure
import shutil

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sys

# 把当前目录的父目录加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

def pytest_addoption(parser):
	parser.addoption("--env", default="saas_qa", help="script run enviroment")

@pytest.fixture(scope="session")
def env(request):
	return request.config.get_option("--env")


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

@pytest.fixture()
@allure.step("打开浏览器")
def drivers(request):
	global driver
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--window-size=1920,1080')
	driver = webdriver.Chrome(options=chrome_options)

	@allure.step("关闭浏览器")
	def fn():
		driver.quit()
		if os.path.exists("./screenshot"):
			shutil.rmtree("./screenshot")
	request.addfinalizer(fn)
	return driver
