from selenium.webdriver.common.by import By

class PortfolioPage:

    ERROR = (By.CSS_SELECTOR, 'Not found')

    URL = "https://the-internet.herokuapp.com/portfolio/"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getErrorDisplayed(self):
        return self.browser.find_element(*self.ERROR).text