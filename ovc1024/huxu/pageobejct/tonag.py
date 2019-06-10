# -*- encoding:utf-8 -*-

from huxu.pageobejct.utils.BasePage import BasePage
from huxu.utils.config import tonag_url
class TOnag(BasePage):
    url = tonag_url
    page_flag_xpath = "/html/body/div[3]/div/div[1]/div/div/div[1]/form/div/div/button"

    Keyword = u"唠叨一下"