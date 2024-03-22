import time
from pathlib import Path

import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.options.ios import XCUITestOptions
from appium.options.common import AppiumOptions
from selenium.webdriver.common.action_chains import ActionChains

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platformVersion = '11'
    options.udid = 'emulator-5554'
    options.app = 'C:\\Users\\User\\OneDrive\\Desktop\\Amazon Shopping_28.6.0.100.apk'

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.implicitly_wait(5)
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='2').click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='plus').click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='4').click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='equals').click()
# result = driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/result_final').text
# print(result)
# assert int(result) == 6

time.sleep(2)
driver.quit()
appium_service.stop()
