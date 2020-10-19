# @Time : 2020/10/17 20:42
# @Author : 30037
# @Email : 960364395@qq.com
# @File : config.py
# @Project : missfresh

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '5.1.1',
    'appPackage': 'cn.missfresh.application',
    'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
    'noReset': True,
    'automationName': 'Uiautomator2'
}