import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    product_tab_selector = (By.XPATH, "//li/a[@href='/products']")
    search_product_input_selector = (By.XPATH, "//*[@id='search_product']")
    search_product_button_selector = (By.XPATH, "//*[@id='submit_search']")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")
        self.driver.implicitly_wait(5)

    def test_find_unicorn_products(self):

        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.refresh()
        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.find_element(*self.search_product_input_selector).send_keys("unicorn")
        self.driver.find_element(*self.search_product_button_selector).click()

        elements = (By.XPATH, "//*[@class='single-products']")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(elements))
        self.assertEqual(len(elements), 2)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
