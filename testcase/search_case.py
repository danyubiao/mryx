# @Time : 2020/10/18 21:15
# @Author : 30037
# @Email : 960364395@qq.com
# @File : search_case.py
# @Project : mryx

from testcase.base_case import BaseCase
from page.classify_page import ClassifyPage
from page.search_page import SearchPage
from time import sleep
from page.home_page import HomePage
from appium.webdriver.common.mobileby import MobileBy as By

"""搜索商品"""
class SearchCase(BaseCase):

    def setUp(self) -> None:
        hp = HomePage(self.driver)
        sleep(2)
        hp.click(hp.adress_locator)
        sleep(1)
        hp.click(hp.city_locator)
        sleep(1)
        hp.click(hp.beijing_locator)
        sleep(1)
        hp.click(hp.return_locator)
        sleep(1)
        hp.click(hp.classify_locator)
        sleep(2)

    #点击热门搜索,用例编号：MRYX_ST_classification_016
    def test_search(self):
        #实例化分类页
        cp = ClassifyPage(self.driver)
        #点击搜索框
        cp.click(cp.search_locator)
        sleep(1)
        #获取搜索页面的大框框
        sep = SearchPage(self.driver)
        frame = cp.find_element(sep.frame_locator)
        #找到热门搜索
        elements = frame.find_elements(By.CLASS_NAME,'android.widget.TextView')
        print(elements)
        text = "a"
        for i in range(len(elements)):
            if elements[i].text == "热门搜索":
                #点击热门搜索下的第一个商品
                text = elements[i+1].text
                elements[i+1].click()
                sleep(2)
                break

        #断言
        assert1 = sep.text(sep.goods_text_locator1)
        assert2 = sep.text(sep.goods_text_locator2)
        assert3 = sep.text(sep.goods_text_locator3)
        assert4 = sep.text(sep.goods_text_locator4)
        self.assertIn(text, assert1)
        self.assertIn(text, assert2)
        self.assertIn(text, assert3)
        self.assertIn(text, assert4)


