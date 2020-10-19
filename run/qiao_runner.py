# -*- coding: utf-8 -*-
# @Time : 2020/10/19 22:20
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : qiao_runner.py
# @Project : appium_test

import unittest
import time
from conf.config import CASE_PATH, REPORT_PATH
from BeautifulReport import BeautifulReport

"""执行所有用例的"""

# 创建测试集
suite = unittest.defaultTestLoader.discover(CASE_PATH, 'cart_testcases.py')
# 创建执行器
runner = BeautifulReport(suite)
# 执行
filename = "{}{}.html".format("mryx-report-", time.strftime("%Y%m%d%H%M"))
runner.report(description='每日优鲜【购物车】测试报告',
              filename=filename,
              report_dir=REPORT_PATH)
