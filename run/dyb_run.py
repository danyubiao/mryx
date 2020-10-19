# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:27
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : dyb_run.py
# @Project : mryx
"""这是但钰彪的运行"""
from conf.config import TESTCASE_PATH,REPORT_PATH
import unittest
import time
from BeautifulReport import BeautifulReport

discover = unittest.defaultTestLoader.discover(TESTCASE_PATH,"test_good*.py")
strTime = time.strftime("%Y%m%d%H%M")
file_name = "mysx_dyb_"+strTime+".html"
BeautifulReport(discover).report(description = "每日优鲜测试用例",
                                 log_path = REPORT_PATH,
                                 filename = file_name)