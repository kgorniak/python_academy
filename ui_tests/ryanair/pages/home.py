from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.ryanair.pages.base import BasePage


class HomePage(BasePage):

    departure_input_field_selector = (By.XPATH, "//*[@id='input-button__departure']")
    destination_input_field_selector = (By.XPATH, "//*[@id='input-button__destination']")
    close_cookies_popup_selector = (By.CLASS_NAME, "cookie-popup-with-overlay__button")
    return_trip_button_selector = (By.XPATH, "//*[@data-ref='flight-search-trip-type__return-trip']")
    one_way_trip_button_selector = (By.XPATH, "//*[@data-ref='flight-search-trip-type__one-way-trip']")
    search_button_selector = (By.CSS_SELECTOR, "div .flight-search-widget__start-search")
    drop_down_list_of_city_selector = (By.CSS_SELECTOR, ".list__airports-container fsw-airport-item")

    # dynamic selectors //div/div[@data-id='2023-02-03'] //*[@data-id='2023-02-03']/..
    today_in_calendar_selector = (By.XPATH, "//*[@data-id='argument']/..")

    def accept_cookies(self):
        self.driver.find_element(*self.close_cookies_popup_selector).click()

    def select_trip_type(self, trip_type):
        if trip_type == "one-way":
            self.driver.find_element(*self.one_way_trip_button_selector).click()
        elif trip_type == "return":
            self.driver.find_element(*self.return_trip_button_selector).click()
        else:
            Exception("Choose 'one-way' or 'return'")

    def select_departure_city(self, departure_city):
        self.driver.find_element(*self.departure_input_field_selector).click()
        self.driver.find_element(*self.departure_input_field_selector).clear()
        self.driver.find_element(*self.departure_input_field_selector).send_keys(departure_city)

    def select_destination_city(self, destination_city):
        self.driver.find_element(*self.destination_input_field_selector).clear()
        self.driver.find_element(*self.destination_input_field_selector).send_keys(destination_city)
        self.driver.find_elements(*self.drop_down_list_of_city_selector)[1].click()

    def click_search_button(self):
        self.driver.find_element(*self.search_button_selector).click()

    def choose_today_in_calendar(self):
        # day = str(date.today())
        day1 = "2023-01-30"
        day2 = "2023-02-03"
        try:
            # WebDriverWait(self.driver, self.timeout).until\
            #     (EC.element_to_be_clickable(self.parse_dynamic_selector(self.today_in_calendar_selector, day1))).click()
            self.click(self.parse_dynamic_selector(self.today_in_calendar_selector, day1))
        except (TimeoutException, ElementClickInterceptedException):
            self.click(self.parse_dynamic_selector(self.today_in_calendar_selector, day2))
        # self.driver.find_element(*self.today_in_calendar_selector).click()
