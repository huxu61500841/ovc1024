from huxu.utils.config import LOGIN_PAGE_URL
from huxu.pageobejct.utils.firefoxwebdrive import FirefoxDriver

class login():
    @classmethod
    def logins(cls,email,password):
        __driver=FirefoxDriver().get_driver()
        __driver.get(LOGIN_PAGE_URL)
        user= __driver.find_element_by_name("email")
        user.send_keys(email)
        passwords=__driver.find_element_by_name("pwd")
        passwords.send_keys(password)
        denglv=__driver.find_element_by_id("comm-submit")
        denglv.click()
