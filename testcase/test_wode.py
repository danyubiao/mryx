# @Time : 2020/10/19 21:45
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : test_wode
# @Project : app测试
"""MRYX_ST_djwd_006"""

from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage
from model.driver import driver
from time import sleep
from page.fenlei_page import FenLei
from testcase.base_case import BaseCase
from page.wode_page import WoDe


class WoDe1(BaseCase):
    """点击我的"""

    def test_wode(self):
        wd = WoDe(self.driver)  # 实例化
        wd.click_wode()  # 调用
        text = wd.duanyan()#调用断言方法
        self.assertEqual(text, '登录/注册')


if __name__ == '__main__':
    unittest.main()
