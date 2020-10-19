# @Time : 2020/10/17 23:12
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : paixun_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class PaixuPage(BasePage):
    """排序方法封装"""
    """点击分类定位器"""
    fenlei_locator = (By.ID, "cn.missfresh.application:id/classifyTab")
    """封装价格排序定位器"""
    price_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_price\"]")

    def going_fenlei(self):
        """封装分类页面"""
        ele = self.driver.find_element(*self.fenlei_locator)
        ele.click()

    def click_price(self):
        """封装排序方法"""
        ele = self.driver.find_element(*self.price_locator)
        ele.click()

    """MRYX_ST_classification_002封装"""
    """封装按销量排序定位器"""
    sales_locator = (By.ID, "cn.missfresh.application:id/tv_sales_count")
    def click_sales(self):
        ele = self.driver.find_element(*self.sales_locator)
        ele.click()