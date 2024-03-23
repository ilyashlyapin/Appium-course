import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.options.ios import XCUITestOptions
from appium.options.common import AppiumOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton


from testcases.scroll_util import ScrollUtil

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

element_mama = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мама")
action = ActionChains(driver)
action.click_and_hold(element_mama)
action.pause(2)
action.release(element_mama)
action.perform()

# ScrollUtil.scrollToTextByAndroidUIAutomator("Ilia Sh", driver)
# driver.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/floating_action_button').click()
# driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
#                     value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Twilio Spain").instance(0))').click()
# driver.swipe(540,1900,540,900)
# driver.swipe(540,1900,540,900)
# driver.swipe(540,1900,540,900)
# driver.swipe(540,1900,540,900)

# ScrollUtil.swipeUp(4,driver)
# ScrollUtil.swipeDown(4,driver)
# driver.swipe(540,900,540,1900)
# driver.swipe(540,900,540,1900)
# driver.swipe(540,900,540,1900)
# driver.swipe(540,900,540,1900)



# driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/three').click()
# driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four').click()
time.sleep(2)
driver.quit()
appium_service.stop()
