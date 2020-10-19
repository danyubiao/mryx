# @Time : 2020/10/19 10:46
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : test_add_gwc.py
# @Project : mryx
from time import sleep
import unittest
from testcase.base_case import BaseCase
from page.add_gwc_page import AddGwcPage
from page.home_page import HomePage

class AddgwcTest(BaseCase):
    def test_add_gwc(self):
        """MRYX_ST_classification_004"""
        """测试添加购物车"""
        add = AddGwcPage(self.driver)
        add.going_fenlei()              # 进入分类页面
        add.add_gwc()                   # 点击添加购物车
        dy = add.dy_add_gwc()           # 断言添加购物车成功
        self.assertEqual(dy, "1")

    def test_add_goods(self):
        """MRYX_ST_classification_009"""
        """测试添加多个商品"""
        sort = HomePage(self.driver)
        sort.click_sort()               # 进入分类页面
        add = AddGwcPage(self.driver)
        add.add_gwc()                   # 点击添加购物车
        add.add_gwc()                   # 点击添加购物车
        add.add_gwc()                   # 点击添加购物车
        add.add_gwc()                   # 点击添加购物车
        dy = add.dy_add_gwc()           # 断言添加购物车成功
        self.assertEqual(dy, "4")
        add.gojing_gouwuche()           # 点击购物车
        add.delete_goods()              # 点击删除商品
        add.sure_delete()               # 点击确定删除按钮

if __name__ == '__main__':
    unittest.main()
