# encoding:utf-8

from huxu.pageobejct.utils.firefoxwebdrive import FirefoxDriver
from huxu.utils.config import LOGIN_PAGE_URL
import time
class LoginPage():
    def __init__(self):
        self.__driver=FirefoxDriver().get_driver()
        time.sleep(6)

    @property
    def page_flag(self):
        element=self.__driver.find_element_by_xpath("//*[@class='fs24']")
        return element

    @property
    def input_email_element(self):
        input_emailt=self.__driver.find_element_by_name('email')
        time.sleep(6)
        return input_emailt
    @property
    def input_passwd_element(self):
        input_passwd=self.__driver.find_element_by_name('pwd')
        time.sleep(6)
        return input_passwd
    @property
    def submit_login_elemen(self):
        submit_login=self.__driver.find_element_by_id("comm-submit")
        time.sleep(6)
        return submit_login

    def denglv(self,email,password):
        self.input_email_element.send_keys(email)
        self.input_passwd_element.send_keys(password)
        self.submit_login_elemen.click()

    def open_and_chenk(self):
        self.__driver.get(LOGIN_PAGE_URL)

        return self.page_flag.text
