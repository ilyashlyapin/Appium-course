import time

from appium import webdriver
from appium.webdriver import appium_service
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.options.ios import XCUITestOptions
from appium.options.common import AppiumOptions
from selenium.webdriver.support.select import Select

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platformVersion = '13'
    options.udid = 'b4c0762b'
    options.browser_name = 'Chrome'

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.get("https://wikipedia.org")
# print(driver.title)
# webdriver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")
# driver.find_element_by_name("q").send_keys("Hello Appium !!!")
# driver.find_element(by=AppiumBy.XPATH, value="//*[@id='L2AGLb']").is_displayed()
# driver.find_element(by=AppiumBy.XPATH, value="//*[@id='L2AGLb']").click()
# driver.find_element(by=AppiumBy.XPATH, value="//*[@name='q']").send_keys("Hello Appium!!!")
dropdown = driver.find_element(by=AppiumBy.CSS_SELECTOR, value='#searchLanguage')

select = Select(dropdown)
select.select_by_value("en")

options = driver.find_elements(by=AppiumBy.TAG_NAME, value='option')
print(len(options))
for option in options:
    print('Text is: ',option.text,' Lang is: ',option.get_attribute('Lang'))
# options = driver.find_elements_by_tag_name('option')
#
# print(len(options))
#
# for option in options:
#     print("Text is : ",option.text," Lang is: ",option.get_attribute('Lang'))

time.sleep(2)
driver.quit()

appium_service.stop()