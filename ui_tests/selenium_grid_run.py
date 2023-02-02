from selenium import webdriver
from selenium.webdriver.common.by import By


desired_capabilities = {
    "browserName": "firefox"
}

driver = webdriver.Remote("http://192.168.1.13:4444", desired_capabilities=desired_capabilities)

driver.get("https://automationexercise.com/")

# driver.find_element(By.CLASS_NAME, "logo pull-left")
driver.find_element(By.LINK_TEXT, "Cart")
driver.find_element(By.ID, "susbscribe_email")
# driver.find_element(By.CLASS_NAME, "fa fa-angle-right")
driver.find_element(By.CLASS_NAME, "brands_products")
driver.find_element(By.ID, "footer")

driver.quit()
