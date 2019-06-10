# -*- encoding:utf-8 -*-

import unittest
from huxu.pageobejct.utils.firefoxwebdrive import FirefoxDriver
from huxu.pageobejct.login import login
from huxu.pageobejct.utils.loginpage import LoginPage
import time
class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #    login().logins("615800841@qq.com","huxu0315")
    #
    #
    #     # self.assertEqual(True, False)




    def test_loginPage(self):
        loginss=LoginPage()
        #调用方法
        loginss.open_and_chenk()
        #输入用户名，密码
        loginss.denglv("615800841@qq.com","huxu0315")

        #期望值
        esc=u"用户登录"
        #实际值,测试能否进入登录页面，找到关键字进行判断
        # a= loginss.open_and_chenk()
        # self.assertEqual(a,esc)
if __name__ == '__main__':
    unittest.main()
