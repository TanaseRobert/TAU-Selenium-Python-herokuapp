from selenium.webdriver.common.by import By


class StatusCodes404Page:

    WELCOME_MESSAGE = (By.CSS_SELECTOR, 'div[class = "example"]>p')

    URL = "https://the-internet.herokuapp.com/status_codes/404"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getMessageDisplayed(self):
        return self.browser.find_element(*self.WELCOME_MESSAGE).text