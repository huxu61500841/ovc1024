# -*- encoding:utf-8 -*-

from huxu.pageobejct.utils.BasePage import BasePage
from huxu.utils.config import Article_url

class Article(BasePage):
    url =Article_url
    page_flag_xpath = "/html/body/div[3]/nav/a"

    Keyword = u"发布文章"