import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.ryanair.pages.home import HomePage


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.ryanair.com/pl/pl")
        self.driver.implicitly_wait(5)

        self.home_page = HomePage(self.driver)
        self.home_page.accept_cookies()

    def test_search_next_flight(self):
        self.home_page.select_trip_type("one-way")
        self.home_page.select_departure_city("Lublin")
        self.home_page.select_destination_city("Dublin")
        self.home_page.choose_today_in_calendar()
        self.home_page.click_search_button()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
