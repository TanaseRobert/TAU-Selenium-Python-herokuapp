from selenium.webdriver.common.by import By

class InternalServerErrorPage:

    NEWS = (By.CSS_SELECTOR, 'html >body >h1')

    URL = "https://the-internet.herokuapp.com/forgot_password"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getNews(self):
        return self.browser.find_element(*self.NEWS).text
