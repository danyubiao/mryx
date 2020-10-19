# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:27
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : dyb_run.py
# @Project : mryx
"""这是但钰彪的运行
测试用例有
    logout_login_test.py 登录注销
    test_activity_news.py 活动消息
    test_add_shopping_address.py 添加收货地址测试
    test_customer_service.py 客服与服务的测试
    test_points_mall.py 积分商城测试
    """
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

