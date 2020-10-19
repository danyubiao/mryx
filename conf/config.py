# -*- coding: utf-8 -*-
# @Time : 2020/10/17 9:49
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : config.py
# @Project : mryx
# 连接设备的信息
import os

desired_capabilites = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'automationName': 'UiAutomator1',
    'noReset': True,
    'unicodeKeyboard':True
}

MY_FULL_PATH = os.path.abspath(__file__) # 当前绝对文件地址
MRYX_PATH = MY_FULL_PATH.strip("confgin.py").strip("conf\\") # 工程地址
REPORT_PATH = os.path.join(MRYX_PATH,"report") # 报告地址
TESTCASE_PATH = os.path.join(MRYX_PATH,"testcase") # 测试用例存放地址
RESOURCES_PATH = os.path.join(MRYX_PATH,"resources") # 资源地址


