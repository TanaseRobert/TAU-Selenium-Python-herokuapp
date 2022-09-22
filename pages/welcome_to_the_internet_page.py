from selenium.webdriver.common.by import By

class WelcomeToTheInternetPage:

    HEADING = (By.CSS_SELECTOR, 'h1[class="heading"]')

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getHeadingMessage(self):
        return self.browser.find_element(*self.HEADING).text