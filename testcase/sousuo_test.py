# @Time : 2020/10/17 16:23
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : sousuo_test.py
# @Project : mryx

from page.base_page import BasePage
from model.driver import driver
from time import sleep
import unittest
from appium.webdriver.common.mobileby import MobileBy as By
from page.fenlei_page import SousuoPage
from testcase.base_case import BaseCase

class SousuoTest(BaseCase):
    def test_sousuo(self):
        """MRYX_ST_classification_001"""
        """搜索测试"""
        sousuo = SousuoPage(self.driver)
        # 进入分类页面
        sleep(2)
        sousuo.going_fenlei()
        # 进入搜索页面
        sleep(1)
        sousuo.going_sousuo()
        # 输入搜索内容
        sleep(1)
        sousuo.input_sousuo("水果")
        # 点击搜索输入框
        sousuo.click_sousuo()
        # 断言找到“综合”文本
        dy = sousuo.get_zonghe()
        self.assertEqual(dy, "综合")


if __name__ == '__main__':
    unittest.main()