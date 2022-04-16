#* Library Import
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#* Relative Import
from wrappers import *

class DriverUtility:
    
    def __init__(self, url):
        
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        # options.add_argument('--headless')
        self.__driver = webdriver.Edge(options = options)
        self.__driver.get(url)
    
    def get_driver(self):
        return self.__driver
    
    def find(self, by, identifier, **kwargs):
        if "wait" in kwargs:
            timeout = kwargs.get("timeout", 20)
            poll_frequency = kwargs.get("poll_frequency", 0.5)
            return WebDriverWait(self.__driver,timeout,poll_frequency) \
                    .until(lambda d: d.find_element(by, identifier))
        else:
            return self.__driver.find_element(by, identifier)
    
    @operation
    def find_and_write(self, by, identifier, value, **kwargs):
        self.find(by, identifier, **kwargs).send_keys(value)
    
    @operation
    def find_and_click(self, by, identifier, **kwargs):
        self.find(by, identifier, **kwargs).click()
        
    def get_page_source(self):
        return self.__driver.find_element(By.TAG_NAME, "body").get_attribute('innerHTML')
    
    