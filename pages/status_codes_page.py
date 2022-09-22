from selenium.webdriver.common.by import By

class StatusCodesPage:

    TITLE_PAGE = (By.CSS_SELECTOR, "div > h3")
    MIDDLE_PAGE = (By.CSS_SELECTOR, 'a[target="_blank"]')
    BUTTON_200 = (By.CSS_SELECTOR, 'a[href = "status_codes/200"]')
    BUTTON_301 = (By.CSS_SELECTOR, 'a[href = "status_codes/301"]')
    BUTTON_404 = (By.CSS_SELECTOR, 'a[href = "status_codes/404"]')
    BUTTON_500 = (By.CSS_SELECTOR, 'a[href = "status_codes/500"]')

    URL = "https://the-internet.herokuapp.com/status_codes"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_PAGE).text

    def isElementalDisplayed(self):
        return self.browser.find_element(*self.MIDDLE_PAGE).is_displayed()

    def clickElemental(self):
        self.browser.find_element(*self.MIDDLE_PAGE).click()

    def click200Button(self):
        self.browser.find_element(*self.BUTTON_200).click()

    def is200ButtonDisplayed(self):
        return self.browser.find_element(*self.BUTTON_200).is_displayed()

    def click301Button(self):
        self.browser.find_element(*self.BUTTON_301).click()

    def is301ButtonDisplayed(self):
        return self.browser.find_element(*self.BUTTON_301).is_displayed()

    def click404Button(self):
        self.browser.find_element(*self.BUTTON_404).click()

    def is404ButtonDisplayed(self):
        return self.browser.find_element(*self.BUTTON_404).is_displayed()

    def click500Button(self):
        self.browser.find_element(*self.BUTTON_500).click()

    def is500ButtonDisplayed(self):
        return self.browser.find_element(*self.BUTTON_500).is_displayed()

