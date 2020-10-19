# @Time : 2020/10/17 23:57
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : test_sousuoshangping
# @Project : app测试
"""MRYX_ST_ss_002"""

from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage
from page.sousuo_page import SousuoPage
from model.driver import driver
from time import sleep
class sousuoshangping(unittest.TestCase):

    """首页搜索商品测试用例"""
    driver = driver()
    def test_002(self):
        # lp= HomePage(self.driver)
        # lp.click_sousu()
        ssp = SousuoPage(self.driver) #实例化
        ssp.sousuo_kuang()
        sleep(10)
        ssp.sousuo_anniu_dianji()
        sleep(2)
        ssp.sousuo_shuru("苹果") #调用方法
        sleep(2)
        ssp.sousuo_anniu_dianji()  # 调用方法


if __name__ == '__main__':
    unittest.main()
