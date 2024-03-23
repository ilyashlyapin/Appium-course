from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text_to_find, driver):

        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value="new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"" + text_to_find + "\").instance(0))").click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(1,howManySwipes+1):
            driver.swipe(540, 1900, 540, 900)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(540, 900, 540, 1900)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(750, 600, 200, 250, 1000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(250, 600, 900, 750, 1000)
