# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:27
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : dyb_run.py
# @Project : mryx
"""这是但钰彪的运行
测试用例有
    logout_login_test.py 登录注销 ^
    test_login.py 登录测试
    test_activity_news.py 活动消息
    test_add_shopping_address.py 添加收货地址测试
    test_customer_service.py 客服与服务的测试
    test_points_mall.py 积分商城测试
    test_income_withdrawal.py 收益不足一元提现  ^
    test_good_ticket.py 优惠券测试 ^
    test_help_get_free.py 助力免费测试
    test_order_status.py 订单页面滑动测试 ^
    """
from conf.config import REPORT_PATH
import unittest
import time
from BeautifulReport import BeautifulReport
from testcase.logout_login_test import LogoutLogingTest
from testcase.test_activity_news import TestActivityNews
from testcase.test_add_shopping_address import TestAddShoppingAddress
from testcase.test_login import TestLogin
from testcase.test_customer_service import TestCuetomerService
from testcase.test_points_mall import TestPointsMall
from testcase.test_income_withdrawal import TestIncomeWithdrawal
from testcase.test_good_ticket import TestGoodTicket
from testcase.test_help_get_free import TestHelpGetFree
from testcase.test_order_status import TestOrderStatus
from testcase.test_login_no import TestLoginNo

suite = unittest.TestSuite()
test11 = (TestLoginNo("test_MRYX_ST_usr_0011")) #
test1 = (TestLogin("test_MRYX_ST_usr_001")) #
tast2 = (LogoutLogingTest("test_MRYX_ST_usr_002")) #
test3 = (TestAddShoppingAddress("test_MRYX_ST_usr_003"))
test4 = (TestCuetomerService("test_MRYX_ST_usr_004")) #
test5 = (TestActivityNews("test_MRYX_ST_usr_005")) #
test6 = (TestPointsMall("text_MRYX_ST_usr_006")) #@
test8 = (TestIncomeWithdrawal("test_MRYX_ST_usr_008")) #@
test9 = (TestGoodTicket("test_MRYX_ST_usr_009"))
test10 = (TestHelpGetFree("test_MRYX_ST_usr_010"))
test12 = (TestOrderStatus("test_MRYX_ST_usr_012"))

tests = (test1,tast2,test4,test5,test11)
suite.addTests(tests)
runner = BeautifulReport(suite)
strTime = time.strftime("%Y%m%d%H%M")
file_name = "mysx_dyb_"+strTime+".html"
runner.report(description="每日优鲜测试用例",
              log_path=REPORT_PATH,
              filename=file_name
              )
