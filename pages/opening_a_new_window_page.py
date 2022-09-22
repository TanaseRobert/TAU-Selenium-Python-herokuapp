from selenium.webdriver.common.by import By

class OpeningWindowPage:

    TITLE_PAGE = (By.CSS_SELECTOR, 'div > h3')
    CLICK_BUTTON = (By.XPATH, '//*[@id="content"]/div/a')
    MIDDLE_PAGE = (By.CSS_SELECTOR, 'a[target="_blank"]')

    URL = "https://the-internet.herokuapp.com/windows"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def isClickButtonDisplayed(self):
        return self.browser.find_element(*self.CLICK_BUTTON).is_displayed()

    def clickButton(self):
        self.browser.find_element(*self.CLICK_BUTTON).click()

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_PAGE).text

    def isElementalDisplayed(self):
        return self.browser.find_element(*self.MIDDLE_PAGE).is_displayed()

    def clickElemental(self):
        self.browser.find_element(*self.MIDDLE_PAGE).click()
