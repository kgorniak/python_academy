from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    # noqa

from ui_tests.tests_exercise.pages.base import BasePage


class ViewProductPage(BasePage):

    quantity_input_selector = (By.ID, "quantity")
    add_to_cart_button_selector = (By.XPATH, "//*[@class='btn btn-default cart']")
    continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")

    def set_number_of_items_and_add_to_cart(self, number_of_items):
        self.driver.find_element(*self.quantity_input_selector).clear()
        self.driver.find_element(*self.quantity_input_selector).send_keys(number_of_items)
        self.driver.find_element(*self.add_to_cart_button_selector).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()
