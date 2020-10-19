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
    mys_income_withdrawal_page.py 收益不足一元提现  ^
    test_good_ticket.py 优惠券测试 ^
    test_help_get_free.py 助力免费测试
    """
from conf.config import TESTCASE_PATH,REPORT_PATH
import unittest
import time
from BeautifulReport import BeautifulReport
from testcase.logout_login_test import LogoutLogingTest


suite = unittest.TestSuite()
suite.addTest(LogoutLogingTest("test_MRYX_ST_usr_002"))
runner = BeautifulReport(suite)
strTime = time.strftime("%Y%m%d%H%M")
file_name = "mysx_dyb_"+strTime+".html"
runner.report(description="每日优鲜测试用例",
              log_path=REPORT_PATH,
              filename=file_name
              )
