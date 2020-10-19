# @Time : 2020/10/19 10:07
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : add_gwc_page.py
# @Project : mryx

from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class AddGwcPage(BasePage):
    """添加购物车方法封装"""

    """点击分类定位器"""
    fenlei_locator = (By.ID, "cn.missfresh.application:id/classifyTab")
    """点击添加购物车定位器封装"""
    add_gwc_locator = (By.XPATH, "//android.view.View[@resource-id=\"cn.missfresh.application:id/recycler_view\"]"
                                "/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/"
                                "android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/"
                                "android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    """断言添加成功定位器"""
    dy_addgwc_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_main_item_product_count\"]")

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
