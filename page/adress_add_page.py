# -*- coding: utf-8 -*-
# @Time : 2020/10/17 22:51
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : adress_add_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from model.driver import webdriver_remote
from selenium.webdriver.remote.webelement import WebElement
from page.base_page import BasePage

"""添加地址页面"""
class AdressAddPage(BasePage):

    """定位器"""

    """收件人"""
    edit_address_receiver_loc = (By.ID,"cn.missfresh.application:id/et_edit_address_receiver")

    """女"""
    sex_lady_loc = (By.ID,"cn.missfresh.application:id/rg_sex_lady")

    """男"""
    sex_sir_loc = (By.ID,"cn.missfresh.application:id/rg_sex_sir")

    """手机号码"""
    edit_address_tel_loc = (By.ID,"cn.missfresh.application:id/et_edit_address_tel")

    """地址"""
    edit_detail_address_loc = (By.ID,"cn.missfresh.application:id/tv_edit_detail_address")

    """门牌号"""
    edit_doorplate_loc = (By.ID,"cn.missfresh.application:id/et_edit_doorplate")

    """家标签"""
    home_address_tags_loc = (By.ID,"cn.missfresh.application:id/rb_home_address_tags")

    """父母家标签"""
    parent_address_tags_loc = (By.ID,"cn.missfresh.application:id/rb_parent_address_tags")

    """公司标签"""
    company_address_tags_loc = (By.ID,"cn.missfresh.application:id/rb_company_address_tags")

    """学校标签"""
    school_address_tags_loc = (By.ID,"cn.missfresh.application:id/rb_school_address_tags")

    """其它标签"""
    other_address_tags_loc = (By.ID,"cn.missfresh.application:id/rb_other_address_tags")

    """保存地址"""
    save_address_loc = ("cn.missfresh.application:id/btn_save_address")