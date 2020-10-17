# @Time : 2020/10/17 15:36
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : base_case
# @Project : app测试
"""测试用例基类"""

import unittest
from model.driver import driver


class BaseCase(unittest.TestCase):
    driver = driver()


if __name__ == '__main__':
    unittest.main()