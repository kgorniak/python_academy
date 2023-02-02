from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    timeout = 10

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click(self, selector):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(selector)).click()

    def parse_dynamic_selector(self, selector, new_value):
        new_selector = (selector[0], selector[1].format(argument=new_value))
        return new_selector
