
# -*- encoding:utf-8 -*-
from huxu.pageobejct.utils.firefoxwebdrive import FirefoxDriver
import time
from huxu.utils.config import LOGIN_PAGE_URL
from huxu.utils.config import tongcheng_url

class BasePage():
    page_flag_xpath=None

    url=None
    Keyword=None

    def __init__(self):
        self.driver = FirefoxDriver().get_driver()
        time.sleep(5)

    @property
    def page_flag(self):
        element = self.driver.find_element_by_xpath(self.page_flag_xpath)
        return element

    def denglv(self,user,password):
        a = FirefoxDriver().get_driver()
        a.get(LOGIN_PAGE_URL)
        time.sleep(5)
        denglv = FirefoxDriver().get_driver().find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/div/form/div[1]/input")
        denglv.send_keys(user)
        passwords = FirefoxDriver().get_driver().find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/div/form/div[2]/input")
        passwords.send_keys(password)
        FirefoxDriver().get_driver().find_element_by_xpath("//*[@id='comm-submit']").click()
        time.sleep(5)

    def Keyword_test(self):

         self.driver.get(self.url)
         time.sleep(5)
         if self.page_flag.text==self.Keyword:
             return True
         else:
             return False

