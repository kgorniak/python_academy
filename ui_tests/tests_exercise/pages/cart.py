from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa

from ui_tests.tests_exercise.pages.base import BasePage


class CartPage(BasePage):

    cart_tab_selector = (By.XPATH, "//*[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    empty_cart_selector = (By.ID, "empty_cart")
    close_checkout_modal_selector = (By.CLASS_NAME, "close-checkout-modal")
    delete_item_button_selector = (By.CLASS_NAME, "cart_quantity_delete")

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button_selector).click()

    def check_if_empty_cart(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.empty_cart_selector))
        except TimeoutException:
            return False

    def check_if_login_modal_visible(self):
        try:
            return WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.close_checkout_modal_selector))
        except TimeoutException:
            return False

    def remove_all_items_from_cart(self):
        delete_buttons = self.driver.find_elements(*self.delete_item_button_selector)
        for button in delete_buttons:
            button.click()
