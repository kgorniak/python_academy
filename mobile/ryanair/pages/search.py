from appium.webdriver.common.appiumby import AppiumBy

from mobile.ryanair.pages.base import BasePage


class SearchPage(BasePage):

    # selectors
    origin_search_selector = (AppiumBy.ID, "et_select_origin")
    destination_search_input = (AppiumBy.ID, "et_select_destination")
    find_result_selector = (AppiumBy.ID, "tv_arrival_name")
    select_trip_details_button_selector = (AppiumBy.ID, "text_location_accept")

    def select_origin_and_destination_inputs(self):
        self.click(self.origin_search_selector)
        self.driver.find_element(*self.origin_search_selector).send_keys("Krakow")
        self.click(self.find_result_selector)
        self.click(self.destination_search_input)
        self.driver.find_element(*self.destination_search_input).send_keys("Vienna")
        self.click(self.find_result_selector)
        self.click(self.select_trip_details_button_selector)
