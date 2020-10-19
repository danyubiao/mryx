# @Time : 2020/10/19 23:19
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : chishennmo_test
# @Project : app测试


from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage
from model.driver import driver
from time import sleep
from page.fenlei_page import FenLei
from testcase.base_case import BaseCase
from page.csm_page import ChiShenMo


class ChiShen(BaseCase):
    def test_chi(self):
        wd = ChiShenMo(self.driver)  # 实例化
        wd.click_chi()  # 调用
        text = wd.chishenmo()  # 调用断言方法
        self.assertEqual(text, '精选专题')


if __name__ == '__main__':
    unittest.main()
