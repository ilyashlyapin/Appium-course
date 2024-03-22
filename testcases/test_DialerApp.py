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
    options.platformVersion = '13'
    options.udid = 'b4c0762b'
    options.app_package = 'com.google.android.dialer'
    options.app_activity = 'com.android.dialer.main.impl.MainActivity'

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


# options = AppiumOptions()
# options.platform_name = 'mac'
# options.automation_name = 'chrome'
# set_capability API allows to provide any custom option
# calls to it could be chained
# options.set_capability('chrome', 'chrome')
# desired_caps = dict(
#
#
#     deviceName='Android',
#     platformName='Android',
#     browserName='Chrome'
#
# )
appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_fab').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/one').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/two').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/three').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four').click()
time.sleep(2)
driver.quit()
appium_service.stop()
