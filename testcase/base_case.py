# -*- coding: utf-8 -*-
# @Time : 2020/10/15 22:43
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : base_case.py
# @Project : App_autotest
import unittest
from model.driver import driver
from page.base_page import BasePage


class BaseCase(unittest.TestCase):
    """用例的基类"""

    def setUp(self) -> None:
        self.driver = driver()

