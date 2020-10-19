# @Time : 2020/10/19 21:53
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : ling_runner.py
# @Project : mryx

import unittest
import time
from conf.config import case_path, report_path
from BeautifulReport import BeautifulReport
from testcase.test_add_gwc import AddgwcTest
from testcase.test_paixu import PaixuTest
from testcase.test_sousuo import SousuoTest
from testcase.test_ts_login import TishiTest
"""执行所有用例"""

# 创建测试集
suite = unittest.TestSuite()
testa1 = AddgwcTest("test_add_goods")
testa2 = AddgwcTest("test_add_gwc")
testb1 = PaixuTest("test_price")
testb2 = PaixuTest("test_sales")
testc1 = SousuoTest("test_clear_sousuo")
testc2 = SousuoTest("test_sousuo")
testd1 = TishiTest("test_ts_login")
testd2 = TishiTest("test_share_goods")
suite.addTests((testa1, testa2, testb1, testb2, testc1, testc2, testd1, testd2))

# 创建执行器
runner = BeautifulReport(suite)
# 执行
filename = "{}{}.html".format("ECShop-report-",time.strftime("%Y%m%d%H%M"))
runner.report(description="每日优鲜APP测试报告",
              filename=filename,
              report_dir=report_path)