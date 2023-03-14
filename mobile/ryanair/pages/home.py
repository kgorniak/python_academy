from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from mobile.ryanair.pages.base import BasePage


class HomePage(BasePage):

    # selectors
    input_search_selector = (AppiumBy.ID, "btn_where_to_fly")

    def click_search_input(self):
        self.click(self.input_search_selector)
        self.click(self.input_search_selector)
        # try:
        #     self.click(self.input_search_selector)
        # except TimeoutException:
        #     print("błąd")
