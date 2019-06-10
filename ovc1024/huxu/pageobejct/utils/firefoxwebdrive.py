from huxu.utils.Singleton import Singleton
from selenium import webdriver
@Singleton
class FirefoxDriver():

    __driver = None

    def __init__(self):
        if self.__driver == None:
            self.__driver = webdriver.Firefox()

    def get_driver(self):
        return self.__driver




