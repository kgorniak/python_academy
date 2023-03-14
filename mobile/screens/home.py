from appium.webdriver.common.appiumby import AppiumBy

from mobile.screens.base import BasePage


class HomePage(BasePage):

    # static selectors
    button_2_selector = (AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    button_equal_selector = (AppiumBy.ACCESSIBILITY_ID, "equals")
    button_plus_selector = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="plus"]')
    result_field_selector = (AppiumBy.ID, "com.google.android.calculator:id/result_final")
    button_square_root_selector = (AppiumBy.ACCESSIBILITY_ID, "square root")
    button_expand_selector = (AppiumBy.ACCESSIBILITY_ID, "Expand")
    button_natural_logarithm_selector = (AppiumBy.ACCESSIBILITY_ID, "natural logarithm")
    button_tagent_selector = (AppiumBy.ACCESSIBILITY_ID, "tangent")

    # dynamic selectors
    digit_button_selector = (AppiumBy.ID, "digit_{argument}")

    def add_values(self, x, y):
        # self.driver.find_element(*button_2_selector).click()
        # self.driver.find_element(*button_plus_selector).click()
        # self.driver.find_element(*button_2_selector).click()
        # self.driver.find_element(*button_equal_selector).click()
        # result = int(self.driver.find_element(*result_field_selector).text)
        # button_2_value = int(self.driver.find_element(*button_2_selector).text)
        # assert result == button_2_value + button_2_value
        self.click(self.parse_dynamic_selector(self.digit_button_selector, x))
        self.click(self.button_plus_selector)
        self.click(self.parse_dynamic_selector(self.digit_button_selector, y))
        self.click(self.button_equal_selector)

    def square_root(self, x):
        self.click(self.button_square_root_selector)
        self.click(self.parse_dynamic_selector(self.digit_button_selector, x))
        self.click(self.button_equal_selector)

    def natural_logarithm(self, x):
        self.click(self.button_expand_selector)
        self.click(self.button_natural_logarithm_selector)
        self.click(self.parse_dynamic_selector(self.digit_button_selector, x))
        self.click(self.button_equal_selector)

    def tangent(self, x):
        self.click(self.button_expand_selector)
        self.click(self.button_tagent_selector)
        self.click(self.parse_dynamic_selector(self.digit_button_selector, x))
        self.click(self.button_equal_selector)

    def add_big_numbers(self, x, y, z):
        for i in str(x):
            self.click(self.parse_dynamic_selector(self.digit_button_selector, int(i)))
        self.click(self.button_plus_selector)

        for i in str(y):
            self.click(self.parse_dynamic_selector(self.digit_button_selector, int(i)))
        self.click(self.button_plus_selector)

        for i in str(z):
            self.click(self.parse_dynamic_selector(self.digit_button_selector, int(i)))

        self.click(self.button_equal_selector)

    def add_many_numbers(self, *args):
        for i in args:
            self.click(self.parse_dynamic_selector(self.digit_button_selector, i))
            self.click(self.button_plus_selector)

        self.click(self.button_equal_selector)

    def get_result(self):
        return float(self.driver.find_element(*self.result_field_selector).text)
