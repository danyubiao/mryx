# @Time : 2020/10/19 10:07
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : add_gwc_page.py
# @Project : mryx

from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class AddGwcPage(BasePage):
    """MRYX_ST_classification_004封装"""

    """点击分类定位器"""
    fenlei_locator = (By.ID, "cn.missfresh.application:id/classifyTab")
    """点击添加购物车定位器封装"""
    add_gwc_locator = (By.ID, "cn.missfresh.application:id/btn_main_item_buy_now")
    """断言添加成功定位器"""
    dy_addgwc_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/cartNumTv\"]")
    """点击购物车定位器"""
    gouwuche_locator = (By.ID, "cn.missfresh.application:id/cartTab")
    """点击删除定位器"""
    delete_goods_locator = (By.ID, "cn.missfresh.application:id/tv_delete")
    """点击确定删除定位器"""
    sure_delete_locator = (By.ID, "cn.missfresh.application:id/tv_ensure")


    def going_fenlei(self):
        """封装进入分类页面方法"""
        ele = self.driver.find_element(*self.fenlei_locator)
        ele.click()

    def add_gwc(self):
        """封装添加购物车方法"""
        ele = self.driver.find_element(*self.add_gwc_locator)
        ele.click()

    def dy_add_gwc(self):
        """断言添加购物车成功方法"""
        ele = self.driver.find_element(*self.dy_addgwc_locator)
        text = ele.text
        return text

    def gojing_gouwuche(self):
        """封装点击购物车方法"""
        self.driver.find_element(*self.gouwuche_locator).click()

    def delete_goods(self):
        """封装点击删除商品方法"""
        self.driver.find_element(*self.delete_goods_locator).click()

    def sure_delete(self):
        """封装点击确定删除方法"""
        self.driver.find_element(*self.sure_delete_locator).click()


