from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.tests_exercise.pages.cart import CartPage
from ui_tests.tests_exercise.pages.checkout import CheckoutPage
from ui_tests.tests_exercise.pages.home import HomePage
from ui_tests.tests_exercise.pages.login import LoginPage
from ui_tests.tests_exercise.pages.products import ProductsPage
from ui_tests.tests_exercise.pages.view_product import ViewProductPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://automationexercise.com/")
    context.driver.implicitly_wait(5)

    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.view_product_page = ViewProductPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)

    context.home_page.close_ad_by_refresh()


def after_scenario(context, scenario):
    context.driver.quit()
