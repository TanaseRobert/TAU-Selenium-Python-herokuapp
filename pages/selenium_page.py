from selenium.webdriver.common.by import By

class SeleniumPage:

    WELCOME_TEXT = (By.CSS_SELECTOR, 'h2[class = "subheader"]')

    URL = "http://elementalselenium.com/"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getWelcomeMessage(self):
        return self.browser.find_element(*self.WELCOME_TEXT).text

