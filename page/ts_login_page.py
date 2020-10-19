# @Time : 2020/10/19 16:11
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : ts_login_page.py
# @Project : mryx

from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class TsLoginPage(BasePage):
    """MRYX_ST_classification_005封装"""
    """点击商品定位器"""
    goods_locator = (By.XPATH, "//android.view.View[@resource-id=\"cn.missfresh.application:id/recycler_view\"]/android.widget.RelativeLayout[3]")
    """点击立即购买定位器"""
    buy_locator = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("立即购买")')
    """断言提示登录"""
    assert_login_locator = (By.ID, "cn.missfresh.application:id/btn_login")

    def click_goods(self):
        """封装点击商品方法"""
        self.driver.find_element(*self.goods_locator).click()

    def click_buy(self):
        """封装点击立即购买方法"""
        self.driver.find_element(*self.buy_locator).click()

    def assert_login(self):
        ele = self.driver.find_element(*self.assert_login_locator)
        text = ele.text
        return text

    """MRYX_ST_classification_010封装"""
    """分享定位器"""
    share_goods_locator = (By.ID, "cn.missfresh.application:id/img_share")
    """断言分享定位器"""
    dy_share_locator = (By.ID, "cn.missfresh.application:id/btn_share_cancle")
    def share_goods(self):
        """封装点击分享方法"""
        self.driver.find_element(*self.share_goods_locator).click()

    def assert_share(self):
        """断言分享方法"""
        ele = self.driver.find_element(*self.dy_share_locator)
        text = ele.text
        return text
