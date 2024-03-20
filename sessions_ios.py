import unittest
from appium import webdriver
from os import path
from appium.webdriver.common.appiumby import AppiumBy

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
appium_server_url = 'http://localhost:4723'

capabilities = dict(
    platformName='iOS',
    platformVersion='15.0',
    deviceName='iPhone SE (2nd generation)',
    automationName='XCUITest',
    app=APP
)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=CAPS
)
driver.quit()