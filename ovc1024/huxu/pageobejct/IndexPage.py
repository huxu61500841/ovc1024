# -*- encoding:utf-8 -*-

from huxu.pageobejct.utils.BasePage import BasePage
from huxu.utils.config import INDEX_PAGE_URL

class INdexPage(BasePage):
    url=INDEX_PAGE_URL
    page_flag_xpath = "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]"
    Keyword =u"最新签到用户"