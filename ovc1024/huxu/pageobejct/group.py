# -*- encoding:utf-8 -*-

from huxu.pageobejct.utils.firefoxwebdrive import FirefoxDriver
import time
from huxu.utils.config import group_url
from huxu.pageobejct.utils.BasePage import BasePage
class group(BasePage):
    url = group_url
    page_flag_xpath = "/html/body/div[3]/nav/a"

    Keyword = u"创建小组"



