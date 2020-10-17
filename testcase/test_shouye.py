# @Time : 2020/10/17 14:57
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : test_shouye
# @Project : app测试
"""MRYX_ST_home_001"""
from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage

class Visit_The_Home_Page(BaseCase):
    """访问首页测试用例"""
    def test_001(self):
        lp= HomePage(self.driver)
        text = lp.get_home()
        self.assertEqual(text,"分类")
if __name__ == '__main__':
    unittest.main()
