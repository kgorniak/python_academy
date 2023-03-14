import os
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def create_driver(platform, app_name):
    app_name = "Ryanair_Discovery_2.3.1_Apkpure.apk"
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

    desired_capabilities = {}
    desired_capabilities["platformName"] = platform
    desired_capabilities["app"] = app_path
    desired_capabilities["newCommandTimeout"] = 300
    desired_capabilities['autoGrantPermissions'] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities)

    return driver
