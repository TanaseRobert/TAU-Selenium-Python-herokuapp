from selenium.webdriver.common.by import By

class AboutPage:

    ERROR = (By.CSS_SELECTOR, 'h1')

    URL = "https://the-internet.herokuapp.com/about/"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getMessageDisplayed(self):
        return self.browser.find_element(*self.ERROR).text