# -*- coding: utf-8 -*-
# @Time : 2020/10/17 15:36
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_base.py
# @Project : mryx

import unittest
from model.driver import app_mrsx

class TestBase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = app_mrsx()


    def tearDown(self) -> None:
        pass