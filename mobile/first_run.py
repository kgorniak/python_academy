import os

from appium import webdriver

# Returns abs path relative to this file and not cwd
from appium.webdriver.common.appiumby import AppiumBy

app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_capabilities = {}
desired_capabilities["platformName"] = "Android"
desired_capabilities["app"] = app_path
desired_capabilities["newCommandTimeout"] = 300

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities)

# selector_point = (AppiumBy.ACCESSIBILITY_ID, "left or right parenthesis")
# driver.find_element(*selector_point).click()
result_field_selector = (AppiumBy.ID, "com.google.android.calculator:id/result_final")
button_2_selector = (AppiumBy.ID, "com.google.android.calculator:id/digit_2")
button_equal_selector = (AppiumBy.ACCESSIBILITY_ID, "equals")
button_plus_selector = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="plus"]')
# button_rad_selector = (AppiumBy.ID, "com.google.android.calculator:id/toggle_mode")
# button_collapse = (AppiumBy.ID, "com.google.android.calculator:id/collapse_expand")
#
# driver.find_element(*button_2_selector)
# driver.find_element(*button_equal_selector)
# driver.find_element(*button_plus_selector)
# driver.find_element(*button_collapse).click()
# driver.find_element(*button_rad_selector).click()


####################################################################################################


driver.find_element(*button_2_selector).click()
driver.find_element(*button_plus_selector).click()
driver.find_element(*button_2_selector).click()
driver.find_element(*button_equal_selector).click()
result = int(driver.find_element(*result_field_selector).text)
button_2_value = int(driver.find_element(*button_2_selector).text)
assert result == button_2_value + button_2_value
