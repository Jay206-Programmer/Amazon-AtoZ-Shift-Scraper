#* Library Import
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#* Relative Import
from wrappers import *

class DriverUtility:
    
    def __init__(self, url):
        self.__driver = webdriver.Edge()
        self.__driver.get(url)
    
    def get_driver(self):
        return self.__driver
    
    def find(self, by, value, **kwargs):
        if "wait" in kwargs:
            timeout = kwargs.get("timeout", 15)
            poll_frequency = kwargs.get("poll_frequency", 0.5)
            return WebDriverWait(self.__driver,timeout,poll_frequency) \
                    .until(lambda d: d.find_element(by, value))
        else:
            return self.__driver.find_element(by, value)
    
    @operation
    def find_and_write(self, by, identifier, value, **kwargs):
        self.find(by, identifier, **kwargs).send_keys(value)
    
    @operation
    def find_and_click(self, by, identifier, **kwargs):
        self.find(by, identifier, **kwargs).click()