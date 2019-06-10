# -*- encoding:utf-8 -*-
from junyi.utils.webdriver.firefoxdriver import FirefoxDriver
from junyi.config import USEGROUP_PAGE_URL
import time

class UserGroupCreatePage():

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        element = self.__driver.find_element_by_xpath("/*[@class='fs24")
        return element
        # return self.create_group_button

    def check_if_page_open(self):
        time.sleep(5)
        if self.page_flag.text == u"用户登录":
            return True
        else:
            return False

