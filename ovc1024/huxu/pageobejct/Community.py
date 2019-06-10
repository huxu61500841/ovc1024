# -*- encoding:utf-8 -*-
from huxu.pageobejct.utils.BasePage import BasePage
from huxu.utils.config import Community_url
class Community(BasePage):
    url = Community_url
    page_flag_xpath = "/html/body/div[3]/div/div[1]/div/div/div/div[2]/ul[1]/li[1]/a"

    Keyword = u"我的社区"
