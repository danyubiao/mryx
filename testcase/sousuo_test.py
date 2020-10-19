# @Time : 2020/10/17 16:23
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : sousuo_test.py
# @Project : mryx
import unittest
from page.fenlei_page import FenleiPage
from testcase.base_case import BaseCase

class SousuoTest(BaseCase):
    def test_sousuo(self):
        """MRYX_ST_classification_001"""
        """搜索测试"""
        sousuo = FenleiPage(self.driver)
        # 进入分类页面
        sousuo.going_fenlei()
        # 进入搜索页面
        sousuo.going_sousuo()
        sousuo.input_sousuo("水果")      # 输入搜索内容
        sousuo.click_sousuo()           # 点击搜索输入框
        dy = sousuo.get_zonghe()        # 断言找到“综合”文本
        self.assertEqual(dy, "综合")

    def test_clear_sousuo(self):
        """MRYX_ST_classification_007"""
        """删除搜索测试"""
        sc = FenleiPage(self.driver)
        sc.going_fenlei()           # 进入分类页面
        sc.going_sousuo()           # 进入搜索页面
        sc.click_clear()            # 点击删除历史搜索
        sc.click_sure()             # 点击确定删除
        dy = sc.get_rmss()          # 断言删除搜索历史
        self.assertEqual(dy, "热门搜索")

if __name__ == '__main__':
    unittest.main()