# @Time : 2020/10/17 17:00
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : fenlei_page.py
# @Project : mryx

from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class FenleiPage(BasePage):
    """进入搜索页面定位器"""

    """MRYX_ST_classification_001"""
    """点击分类定位器"""
    fenlei_locator = (By.ID, "cn.missfresh.application:id/classifyTab")
    """点击搜索定位器"""
    fenlei_sousuo_locator = (By.ID, "cn.missfresh.application:id/tv_search_text") #新增收货地址定位
    """输入搜索内容定位器"""
    shuru_sousuo_locator = (By.XPATH, "//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/search_view\"]")
    """点击搜索定位器"""
    dianji_sousuo_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_search\"]")
    """断言购物车定位器"""
    zonghe_duanyan_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/composite_tv\"]")

    def going_fenlei(self):
        """封装分类页面"""
        ele = self.driver.find_element(*self.fenlei_locator)
        ele.click()

    def going_sousuo(self):
        """封装分类搜索"""
        ele = self.driver.find_element(*self.fenlei_sousuo_locator)
        ele.click()

    def input_sousuo(self,shangpin):
        """封装输入搜索内容"""
        ele = self.driver.find_element(*self.shuru_sousuo_locator)
        ele.clear()
        ele.send_keys(shangpin)

    def click_sousuo(self):
        """封装点击搜索"""
        ele = self.driver.find_element(*self.dianji_sousuo_locator)
        ele.click()

    def get_zonghe(self):
        ele = self.driver.find_element(*self.zonghe_duanyan_locator)
        text = ele.text
        return text

    """MRYX_ST_classification_007封装"""
    """封装删除搜索历史定位器"""
    clear_sousuo_locator = (By.ID, "cn.missfresh.application:id/clear_his_view")
    """确定删除搜索历史定位器"""
    sure_clear_locator = (By.ID, "cn.missfresh.application:id/submit_tv")
    """断言删除历史搜索成功"""
    rmss_locator = (By.ID, "cn.missfresh.application:id/hot_tip_tv")

    def click_clear(self):
        """封装删除搜索历史方法"""
        ele = self.driver.find_element(*self.clear_sousuo_locator)
        ele.click()

    def click_sure(self):
        ele = self.driver.find_element(*self.sure_clear_locator)
        ele.click()

    def get_rmss(self):
        ele = self.driver.find_element(*self.rmss_locator)
        text = ele.text

#封装定位器
    fenlei_location =(By.ID,"cn.missfresh.application:id/classifyTab")
#获取分类断言定位
    fenlei_duanyan_locator=(By.ID,"cn.missfresh.application:id/tv_category_name")

     #点击分类跳转
    def click_dianji(self):
        self.click(self.fenlei_location)

    def duanyan_fenlei(self):
        element= self.driver.find_element(*self.fenlei_duanyan_locator)
        text= element.text
        return text