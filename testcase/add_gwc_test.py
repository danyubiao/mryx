# @Time : 2020/10/19 10:46
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : add_gwc_test.py
# @Project : mryx
from time import sleep
import unittest
from testcase.base_case import BaseCase
from page.add_gwc_page import AddGwcPage

class AddgwcTest(BaseCase):
    def test_add_gwc(self):
        """MRYX_ST_classification_004"""
        """测试添加购物车"""
        add = AddGwcPage(self.driver)
        sleep(5)
        # 进入分类页面
        add.going_fenlei()
        sleep(5)
        # 点击添加购物车
        add.add_gwc()
        # 断言添加购物车成功
        dy = add.dy_add_gwc()
        self.assertEqual(dy, "1")


if __name__ == '__main__':
    unittest.main()
