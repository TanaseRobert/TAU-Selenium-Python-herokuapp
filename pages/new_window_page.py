from selenium.webdriver.common.by import By

class NewWindowPage:

    TITLE_PAGE = (By.XPATH, '//div/ h3')

    URL = "https://the-internet.herokuapp.com/windows/new"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getHeading(self):
        return self.browser.find_element(*self.TITLE_PAGE).text