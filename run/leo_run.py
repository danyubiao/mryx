# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:30
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : leo_run.py
# @Project : mryx
from BeautifulReport import BeautifulReport
import time
from conf import config
import unittest


"""运行测试用例并生成报告"""
filname = "{}{}".format("mryx_report",time.strftime("%Y%m%d%H%M"))
testsuite = unittest.defaultTestLoader.discover(config.TESTCASE_PATH, "test_shopping_cart.py")
BeautifulReport(testsuite).report(
    description='每日优鲜购物车',
    report_dir=config.REPORT_PATH,
    filename = filname
)