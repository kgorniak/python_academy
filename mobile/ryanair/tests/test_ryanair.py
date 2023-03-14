import os
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from mobile.ryanair.helpers import create_driver
from mobile.ryanair.pages.home import HomePage
from mobile.ryanair.pages.search import SearchPage


class RyanairTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver("Android", "Ryanair_Discovery_2.3.1_Apkpure.apk")
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)

    def test_search_cheapest_fly(self):
        self.home_page.click_search_input()
        self.search_page.select_origin_and_destination_inputs()


if __name__ == '__main__':
    unittest.main()
