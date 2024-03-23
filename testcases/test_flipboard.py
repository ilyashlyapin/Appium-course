import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.options.ios import XCUITestOptions
from appium.options.common import AppiumOptions
from selenium.webdriver.common.action_chains import ActionChains

from testcases.scroll_util import ScrollUtil

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platformVersion = '13'
    options.udid = 'b4c0762b'
    options.app_package = 'flipboard.app'
    options.app_activity = 'flipboard.activities.LaunchActivityAlias'

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ID, value='flipboard.app:id/icon_button_text').click()

driver.find_elements(by=AppiumBy.ID, value='flipboard.app:id/topic_picker_topic_row_topic_tag')[0].click()
driver.find_elements(by=AppiumBy.ID, value='flipboard.app:id/topic_picker_topic_row_topic_tag')[1].click()
driver.find_elements(by=AppiumBy.ID, value='flipboard.app:id/topic_picker_topic_row_topic_tag')[2].click()
driver.find_element(by=AppiumBy.ID, value='flipboard.app:id/topic_picker_continue_button').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="flipboard.app:id/icon_button_text" and @text="Skip for Now"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Accept"]').click()
time.sleep(2)
ScrollUtil.swipeUp(4,driver)
time.sleep(2)
ScrollUtil.swipeDown(4,driver)
time.sleep(2)
ScrollUtil.swipeLeft(2,driver)
time.sleep(2)
ScrollUtil.swipeRight(2,driver)

time.sleep(2)
driver.quit()
