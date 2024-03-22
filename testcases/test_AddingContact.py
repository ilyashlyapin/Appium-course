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
    options.app_package = 'com.google.android.contacts'
    options.app_activity = 'com.google.android.apps.contacts.activities.PeopleActivity'

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.implicitly_wait(5)
driver.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/floating_action_button').click()
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']").send_keys("Harry")
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']").send_keys("12345")
driver.hide_keyboard()
driver.find_element(by=AppiumBy.XPATH, value="//*[contains(@text,'Save')]").click()
# driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/two').click()
# driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/three').click()
# driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four').click()
time.sleep(2)
driver.quit()
appium_service.stop()