# -*- encoding:utf-8 -*-

from huxu.pageobejct.utils.BasePage import BasePage
from huxu.utils.config import search_url

class search(BasePage):
    url = search_url
    page_flag_xpath = "/html/body/div[3]/div/div[2]/div/div/div[2]/form/div/div/button"

    Keyword = u"搜索"
