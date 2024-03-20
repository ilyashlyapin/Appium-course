import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.options.ios import XCUITestOptions
from appium.options.common import AppiumOptions

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

def create_android_driver(custom_opts = None):
    options = UiAutomator2Options()
    options.platformVersion = '13'
    options.udid = 'b4c0762b'
    options.browser_name = 'Chrome'

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


driver = create_android_driver()
driver.get("http://google.com")
# print(driver.title)
# webdriver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")
#driver.find_element_by_name("q").send_keys("Hello Appium !!!")
driver.find_element(by=AppiumBy.XPATH, value="//*[@id='L2AGLb']").is_displayed()
driver.find_element(by=AppiumBy.XPATH, value="//*[@id='L2AGLb']").click()
driver.find_element(by=AppiumBy.XPATH, value="//*[@name='q']").send_keys("Hello Appium!!!")
time.sleep(2)
driver.quit()