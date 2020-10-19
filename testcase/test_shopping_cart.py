# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:46
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : test_shopping_cart.py
# @Project : mryx
import unittest
from model.driver import driver
from page.classify_page import ClassifyPage
from page.home_page import HomePage
from model.commodity_operating import guess_like_shop,commodity_operating,guess_like_shop_add
from page.shopping_cart_page import ShoppingCartPage
from page.go_coudan_page import GoCoudanPage

"""购物车测试用例"""
class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = driver()

    def test_shopping_add_cart_case(self):
        """商品添加购物车"""
        hm = HomePage(self.driver)
        hm.click(hm.classify_tab_loc)        #点击分类标签
        cifp = ClassifyPage(self.driver)    #实例化商品分类页
        cifp.click(cifp.cart_view_loc)      #点击搜索框
        cifp.send_keys(cifp.search_view_loc,"牛奶")        #输入牛奶
        cifp.click(cifp.suggest_contentt_loc)             #点击特仑苏牛奶
        gls = guess_like_shop(self.driver,"特仑苏纯牛奶",cifp.result_recycler_loc)   #选择包含特仑苏纯牛奶的商品
        cifp.click(cifp.buy_now_loc,gls)                                           #点击
        cifp.click(cifp.cart_view_loc)                  #跳转购物车页面
        spcp = ShoppingCartPage(self.driver)                        #实例化购物车页面
        co = commodity_operating(self.driver,spcp.shopping_cart_recycleview_loc,"特仑苏纯牛奶")
        self.assertEqual(co[5].text,cifp.text(cifp.buy_now_loc,gls))        #断言
        co[2].click()                                                      #点击删除
        spcp.click(spcp.ensure_delete_the_goods_loc)

    def test_shopping_cart_add_case(self):
        """增加购物车商品个数"""
        hm = HomePage(self.driver)
        hm.click(hm.classify_tab_loc)  # 点击分类标签
        cifp = ClassifyPage(self.driver)  # 实例化商品分类页
        cifp.click(cifp.cart_view_loc)  # 点击搜索框
        cifp.send_keys(cifp.search_view_loc, "牛奶")  # 输入牛奶
        cifp.click(cifp.suggest_contentt_loc)  # 点击特仑苏牛奶
        gls = guess_like_shop(self.driver, "特仑苏纯牛奶", cifp.result_recycler_loc)  # 选择包含特仑苏纯牛奶的商品
        spcp = ShoppingCartPage(self.driver)  # 实例化购物车页面
        co = commodity_operating(self.driver, spcp.shopping_cart_recycleview_loc, "特仑苏纯牛奶")
        cifp.click(cifp.buy_now_loc, gls)  # 点击
        cifp.click(cifp.cart_view_loc)                  #跳转购物车页面
        number1 = co[4].text()
        co[1].click() # 点击增加
        number2 = co[4].text()
        self.assertTrue(number2 > number1)  # 断言
        for i in range(int(number2)):
            co[2].click()  # 点击删除
        spcp.click(spcp.ensure_delete_the_goods_loc)      #确认删除

    def test_shopping_cart_subtract_case(self):
        """减少购物车商品个数"""
        hm = HomePage(self.driver)
        hm.click(hm.classify_tab_loc)  # 点击分类标签
        cifp = ClassifyPage(self.driver)  # 实例化商品分类页
        cifp.click(cifp.cart_view_loc)  # 点击搜索框
        cifp.send_keys(cifp.search_view_loc, "牛奶")  # 输入牛奶
        cifp.click(cifp.suggest_contentt_loc)  # 点击特仑苏牛奶
        gls = guess_like_shop(self.driver, "特仑苏纯牛奶", cifp.result_recycler_loc)  # 选择包含特仑苏纯牛奶的商品
        spcp = ShoppingCartPage(self.driver)  # 实例化购物车页面
        co = commodity_operating(self.driver, spcp.shopping_cart_recycleview_loc, "特仑苏纯牛奶")
        cifp.click(cifp.buy_now_loc, gls)  # 点击
        cifp.click(cifp.cart_view_loc)                  #跳转购物车页面
        co[1].click()  # 点击增加
        number1 = co[4].text()
        co[2].click()
        number2 = co[4].text()
        self.assertTrue(number2 < number1)  # 断言
        co[2].click()  # 点击删除
        spcp.click(spcp.ensure_delete_the_goods_loc)  # 确认删除

    def test_add_shopping_guess_you_like_case(self):
        """购物车猜你喜欢添加商品"""
        hm = HomePage(self.driver)    #实例化商品首页
        hm.click(hm.classify_tab_loc)  # 点击分类标签
        hm.click(hm.cart_tab_loc)
        spcp = ShoppingCartPage(self.driver)  # 实例化购物车页面
        glsa = guess_like_shop_add(self.driver,1,spcp.shopping_cart_recycleview_loc)
        glsa[0].click()                                 #添加
        co = commodity_operating(self.driver, spcp.shopping_cart_recycleview_loc, glsa[1])
        self.assertEqual(glsa[1],co[5].text)
        co[2].click()  # 点击删除
        spcp.click(spcp.ensure_delete_the_goods_loc)  # 确认删除

    def test_go_shopping_cart_case(self):
        """从首页去购物车"""
        hm = HomePage(self.driver)    #实例化商品首页
        hm.click(hm.classify_tab_loc)  # 点击分类标签
        hm.click(hm.cart_tab_loc)
        spcp = ShoppingCartPage(self.driver)  # 实例化购物车页面
        self.assertEqual(spcp.text(spcp.shopping_cart_title_loc).strip(),"购物车")

    def test_go_coudan_case(self):
        """跳转到去凑单"""
        hm = HomePage(self.driver)
        hm.click(hm.classify_tab_loc)  # 点击分类标签
        cifp = ClassifyPage(self.driver)  # 实例化商品分类页
        cifp.click(cifp.cart_view_loc)  # 点击搜索框
        cifp.send_keys(cifp.search_view_loc, "牛奶")  # 输入牛奶
        cifp.click(cifp.suggest_contentt_loc)  # 点击特仑苏牛奶
        gls = guess_like_shop(self.driver, "特仑苏纯牛奶", cifp.result_recycler_loc)  # 选择包含特仑苏纯牛奶的商品
        spcp = ShoppingCartPage(self.driver)  # 实例化购物车页面
        co = commodity_operating(self.driver, spcp.shopping_cart_recycleview_loc, "特仑苏纯牛奶")
        cifp.click(cifp.buy_now_loc, gls)  # 点击
        cifp.click(cifp.cart_view_loc)                  #跳转购物车页面
        spcp.click(spcp.available_coupons_loc)                #点击可用优惠券
        spcp.click(spcp.go_coudan_loc)                        #点击去凑单
        gcp = GoCoudanPage(self.driver)
        self.assertEqual(gcp.text(gcp.go_coudan_title_loc).strip(),"凑单有优惠")
        gcp.click(gcp.return_shopping_cart_loc)       #返回购物车
        co[2].click()  # 点击删除
        spcp.click(spcp.ensure_delete_the_goods_loc)  # 确认删除

    def test_return_shopping_cart_case(self):
        """从去凑单返回"""
        hm = HomePage(self.driver)
        hm.click(hm.classify_tab_loc)  # 点击分类标签
        cifp = ClassifyPage(self.driver)  # 实例化商品分类页
        cifp.click(cifp.cart_view_loc)  # 点击搜索框
        cifp.send_keys(cifp.search_view_loc, "牛奶")  # 输入牛奶
        cifp.click(cifp.suggest_contentt_loc)  # 点击特仑苏牛奶
        gls = guess_like_shop(self.driver, "特仑苏纯牛奶", cifp.result_recycler_loc)  # 选择包含特仑苏纯牛奶的商品
        spcp = ShoppingCartPage(self.driver)  # 实例化购物车页面
        co = commodity_operating(self.driver, spcp.shopping_cart_recycleview_loc, "特仑苏纯牛奶")
        cifp.click(cifp.buy_now_loc, gls)  # 点击
        cifp.click(cifp.cart_view_loc)  # 跳转购物车页面
        spcp.click(spcp.available_coupons_loc)  # 点击可用优惠券
        spcp.click(spcp.go_coudan_loc)  # 点击去凑单
        gcp = GoCoudanPage(self.driver)    #实例化去凑单页面
        gcp.click(gcp.return_shopping_cart_loc)  # 返回购物车
        self.assertEqual(spcp.text(spcp.shopping_cart_title_loc).strip(),"购物车")
        co[2].click()  # 点击删除
        spcp.click(spcp.ensure_delete_the_goods_loc)  # 确认删除







