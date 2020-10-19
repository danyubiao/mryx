# @Time : 2020/10/19 10:46
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : add_gwc_test.py
# @Project : mryx

from page.base_page import BasePage
from model.driver import driver
from time import sleep
import unittest
from appium.webdriver.common.mobileby import MobileBy as By
from testcase.base_case import BaseCase
from page.add_gwc_page import AddGwcPage

class AddgwcTest(AddGwcPage):
    def test_add_gwc(self):
        """MRYX_ST_classification_004"""
        """测试添加购物车"""