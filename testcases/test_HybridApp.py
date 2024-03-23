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
    options.app_package = 'com.android.chrome'
    options.app_activity = 'com.google.android.apps.chrome.Main'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


appium_service = AppiumService()

driver = create_android_driver()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ID, 'com.android.chrome:id/signin_fre_dismiss_button').click()
driver.find_element(AppiumBy.ID, 'com.android.chrome:id/no_button').click()
driver.find_element(AppiumBy.ID, 'com.android.chrome:id/ack_button').click()

driver.get('http://google.com')
time.sleep(2)
# contexts = driver.contexts
#
# for context in contexts:
#     print(context)
#
# driver.switch_to.context('WEBVIEW_chrome')

webview = driver.contexts[1]
action = ActionChains(driver)
driver.switch_to.context(webview)
cookie_accept_button = driver.find_element(AppiumBy.XPATH, value="//*[@id='L2AGLb']")
# making a variable from finding a button
action.click(on_element=cookie_accept_button)  # defining an action from ActionsChains
action.perform()  # performing the defined action

driver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")

time.sleep(2)
driver.quit()