# @Time : 2020/10/19 23:28
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : bai_run
# @Project : app测试
import unittest
import time
from conf.config import  REPORT_PATH
from BeautifulReport import BeautifulReport
from testcase.chishennmo_test import ChiShen
from testcase.sousuo_test import SousuoTest
from testcase.test_fenlei import FenLei1
from testcase.test_gouwuche import GouWuChe
from testcase.test_shouye import Visit_The_Home
from testcase.test_sousuoshangping import SouSuoShangPing
from testcase.test_wode import WoDe1
"""执行所有用例"""

# 创建测试集
suite = unittest.TestSuite()
testa1 = ChiShen('test_chi')
testa2 =  SousuoTest("test_sousuo")
testb1 = FenLei1("test_fenlei")
testb2 = GouWuChe("test_gouwu")
testc1 = Visit_The_Home("test_001")
testc2 = SouSuoShangPing("test_002")
testd1 = WoDe1("test_wode")

suite.addTests((testa1, testa2, testb1, testb2, testc1, testc2, testd1))

# 创建执行器
runner = BeautifulReport(suite)
# 执行
filename = "{}{}.html".format("ECShop-report-",time.strftime("%Y%m%d%H%M"))
runner.report(description="每日优鲜APP测试报告",
              filename=filename,
              report_dir=REPORT_PATH)

