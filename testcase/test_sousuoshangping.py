# @Time : 2020/10/17 23:57
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : test_sousuoshangping
# @Project : app测试
"""MRYX_ST_ss_002"""


import unittest
from page.sousuo_page import SousuoPage
from time import sleep
from model.driver import driver
from page.sousuo_page import SousuoPage


class SouSuoShangPing(unittest.TestCase):

    """首页搜索商品测试用例"""

    def test_002(self):
        # lp= HomePage(self.driver)
        # lp.click_sousu()
        ssp = SousuoPage(driver()) #实例化
        ssp.sousuo_kuang()
        sleep(10)
        ssp.sousuo_shuru("苹果") #调用方法
        sleep(2)
        ssp.sousuo_anniu_dianji()  # 调用方法
        ssp.duanyan_sousu() # 调用断言方法
        text = ssp.duanyan_sousu()
        self.assertEqual(text,"陕西高原红富士苹果4个720g起")

if __name__ == '__main__':
    unittest.main()
