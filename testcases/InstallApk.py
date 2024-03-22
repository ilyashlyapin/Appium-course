import time
from pathlib import Path

import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.common import AppiumOptions
from selenium.webdriver.common.action_chains import ActionChains

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platformVersion = '11'
    options.udid = 'b4c0762b'
    options.app_package = 'com.amazon.mShop.android.shopping'
    options.app_activity = 'com.amazon.mShop.home.HomeActivity'
    options.auto_grant_permissions = True

    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

appium_service = AppiumService()
appium_service.start()

driver = create_android_driver()
driver.implicitly_wait(5)
# allowButton = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
# allowButton.click()
# action = ActionChains(driver)
# action.click(on_element=permission_allow_button)
# action.perform()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Listo")').click()
# driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Listo"]').click()
# driver.find_element(by=AppiumBy.ID,value='com.amazon.mShop.android.shopping:id/sso_continue').click()
# driver.find_element(by=AppiumBy.ID,value='com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
# wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')))
# driver.find_element(by=AppiumBy.ID,value='com.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys('shoes')
driver.press_keycode(66)


# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='4').click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='equals').click()
# result = driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/result_final').text
# print(result)
# assert int(result) == 6

time.sleep(6)
driver.quit()
appium_service.stop()
