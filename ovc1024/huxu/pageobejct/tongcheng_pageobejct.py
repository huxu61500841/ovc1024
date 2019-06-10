# -*- encoding:utf-8 -*-

from huxu.pageobejct.utils.firefoxwebdrive import FirefoxDriver
import time
from huxu.utils.config import tongcheng_url
from huxu.pageobejct.utils.BasePage import BasePage
class tongcheng(BasePage):
    page_flag_xpath="/html/body/div[3]/div[2]/div[1]/div[1]/div[1]"
    url=tongcheng_url
    Keyword = u"同城用户"



