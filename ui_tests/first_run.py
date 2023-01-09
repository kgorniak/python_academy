from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")

# driver.find_element(By.CLASS_NAME, "logo pull-left")
driver.find_element(By.LINK_TEXT, "Cart")
driver.find_element(By.ID, "susbscribe_email")
# driver.find_element(By.CLASS_NAME, "fa fa-angle-right")
driver.find_element(By.CLASS_NAME, "brands_products")
driver.find_element(By.ID, "footer")
