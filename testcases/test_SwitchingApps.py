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
    options.no_reset = True
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


appium_service = AppiumService()

driver = create_android_driver()
driver.implicitly_wait(10)
time.sleep(5)



def test_start_activity_other_app(other_app, other_app_activity) -> None:
    driver.execute_script(
        'mobile: startActivity',
        {
            'component': f'{other_app}/{other_app_activity}',
        },
    )


test_start_activity_other_app('com.google.android.contacts',
                              'com.google.android.apps.contacts.activities.PeopleActivity')
#
# driver.find_elements(AppiumBy.ID, 'com.android.mms:id/subject')[0].click()
#
# messages = driver.find_elements_by_id('com.android.mms:id/text_view')
# text = messages[len(messages) - 1].text
# print(text[83:89])

time.sleep(5)
driver.quit()
