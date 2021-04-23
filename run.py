# -*- coding: UTF-8 -*-
"""
@auth:buxiangjie
@date:2020-05-12 11:26:00
@describe: 
"""
import sys
from multiprocessing import Pool

import pytest

from common.base import Common


# noinspection PySimplifyBooleanCheck
def get_browser(platform: list):
	plat = []
	env = Common.get_yaml_data("config", "env.yaml")
	for i in platform:
		if env[i]["browser"] is not None:
			for b in env[i]["browser"]:
				browser = [i, b]
				plat.append(browser)
	print("运行环境:", plat)
	return plat


def run_case(case: list):
	pytest.main(
		["-vsq", f"{sys.argv[3]}", "--alluredir=results", f"--env={sys.argv[1]}", "--reruns=3", f"--platform={case[0]}",
		 f"--browser={case[1]}"])


def run_pool(cases: list):
	pool = Pool(len(cases))
	for case in cases:
		pool.apply_async(run_case, (case,))
	pool.close()
	pool.join()


if __name__ == '__main__':
	run_pool(get_browser(sys.argv[2].split(",")))
