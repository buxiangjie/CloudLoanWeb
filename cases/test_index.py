# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""

import pytest
import allure

from pages.index import Index


class TestIndex:

	@allure.feature("打开首页")
	def test_index(self, drivers):
		"""首页"""
		index = Index(drivers)
		index.open()
		index.check_index()
		assert 0

	@allure.feature("打开加入我们")
	def test_join_us(self, drivers):
		"""加入我们"""
		index = Index(drivers)
		index.open()
		join_us = index.open_join_us()
		join_us.check_join_us()

	@allure.feature("打开新闻公告")
	def test_news(self, drivers):
		"""新闻公告"""
		index = Index(drivers)
		index.open()
		news = index.open_news()
		news.check_news()

	@allure.feature("打开关于我们")
	def test_about_us(self, drivers):
		"""关于我们"""
		index = Index(drivers)
		index.open()
		about_us = index.open_about_us()
		about_us.check_about_us()

	@allure.feature("打开产品简介")
	def test_product_int(self, drivers):
		"""产品简介"""
		index = Index(drivers)
		index.open()
		product_int = index.open_product_int()
		product_int.check_product_int()

	@allure.feature("打开企业文化")
	def test_enterprise_culture(self, drivers):
		"""企业文化"""
		index = Index(drivers)
		index.open()
		enterprise_culture = index.open_enterprise_culture()
		enterprise_culture.check_enterprise_culture()


if __name__ == '__main__':
	pytest.main()
