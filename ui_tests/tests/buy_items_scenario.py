import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.cart import CartPage
from ui_tests.pages.checkout import CheckoutPage
from ui_tests.pages.login import LoginPage
from ui_tests.pages.home import HomePage

from selenium.webdriver.common.by import By

from ui_tests.pages.products import ProductsPage


class MyTestCase(unittest.TestCase):

    product_tab_selector = (By.XPATH, "//li/a[@href='/products']")
    search_product_input_selector = (By.XPATH, "//*[@id='search_product']")
    search_product_button_selector = (By.XPATH, "//*[@id='submit_search']")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")
        self.driver.implicitly_wait(5)

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        self.home_page.close_ad_by_refresh()
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")

    def test_add_items_to_cart_and_checkout(self):
        self.home_page.close_ad_by_refresh()
        self.products_page.add_product_to_cart("men tshirt")
        self.products_page.add_product_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()

        self.assertEqual(sum(self.checkout_page.get_items_prices()), self.checkout_page.get_total_price())


if __name__ == '__main__':
    unittest.main()
