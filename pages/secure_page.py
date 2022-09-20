from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class SecurePage:
    # locators
    WELCOME_TEXT = (By.CSS_SELECTOR, 'h4')
    SUCCESS_LOGIN = (By.CSS_SELECTOR, '[class ="flash success"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[class^="button"]')

    # URL
    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getWelcomeMessage(self):
        return self.browser.find_element(*self.WELCOME_TEXT).text

    def getGoodNews(self):
        return self.browser.find_element(*self.SUCCESS_LOGIN).text

    def isLogoutDisplayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def getButton(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).text

    def clickLogoutButton(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()
