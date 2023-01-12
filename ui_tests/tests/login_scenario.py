from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://automationexercise.com/")

driver.find_element(By.XPATH, "//li/a[@href='/login']").click()
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("seleniumremote@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("tester")
driver.find_element(By.XPATH, "//button[@data-qa='login-button']").submit()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a/i[@class='fa fa-user']")))
# driver.find_element(By.XPATH, "//a/i[@class='fa fa-user']")
