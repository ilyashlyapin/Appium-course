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
    options.app_package = 'com.mobeta.android.demodslv'
    options.app_activity = '.Launcher'

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.implicitly_wait(10)
actions = ActionChains(driver)

driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/continue_button').click()
driver.find_element(AppiumBy.ID, 'android:id/button1').click()
driver.find_elements(AppiumBy.ID,'com.mobeta.android.demodslv:id/activity_title')[0].click()
# driver.find_element(AppiumBy.ID, 'android:id/button1').click()
#driver.find_elements_by_id('com.mobeta.android.demodslv:id/activity_title')[0].click()

elements = driver.find_elements(AppiumBy.ID,'com.mobeta.android.demodslv:id/drag_handle')
actions.drag_and_drop(elements[0],elements[3]).perform()

time.sleep(2)
driver.quit()