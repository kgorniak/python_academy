from selenium.webdriver.common.by import By

from ui_tests.pages.base import BasePage


class CheckoutPage(BasePage):

    cart_total_price_selector = (By.CLASS_NAME, "cart_total_price")

    def get_items_prices(self):
        prices_elements = self.driver.find_elements(*self.cart_total_price_selector)
        prices_items = prices_elements[:-1]
        prices_list = []
        for element in prices_items:
            single_price = int(element.text.split()[1])
            prices_list.append(single_price)
        return prices_list

    def get_total_price(self):
        prices_elements = self.driver.find_elements(*self.cart_total_price_selector)
        cart_total_sum = prices_elements[-1]
        sum_int = int(cart_total_sum.text.split()[1])
        return sum_int
