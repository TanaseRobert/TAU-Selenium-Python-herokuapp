from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class DisappearingElementsPage:

    TITLE_PAGE = (By.CSS_SELECTOR, "h3")
    MIDDLE_PAGE = (By.CSS_SELECTOR, 'a[target="_blank"]')
    HOME_BUTTON = (By.CSS_SELECTOR, 'a[href="/"]')
    ABOUT_BUTTON = (By.CSS_SELECTOR, 'a[href="/about/"]')
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'a[href="/contact-us/"]')
    PORTFOLIO_BUTTON = (By.CSS_SELECTOR, 'a[href="/portfolio/"]')

    URL = "https://the-internet.herokuapp.com/disappearing_elements"

    def clickHomeButton(self):
        self.browser.find_element(*self.HOME_BUTTON).click()

    def isHomeButtonDisplayed(self):
        return self.browser.find_element(*self.HOME_BUTTON).is_displayed()

    def clickAboutButton(self):
        self.browser.find_element(*self.ABOUT_BUTTON).click()

    def isAboutButtonDisplayed(self):
        return self.browser.find_element(*self.ABOUT_BUTTON).is_displayed()

    def clickContactUsButton(self):
        self.browser.find_element(*self.CONTACT_US_BUTTON).click()

    def isContactUsButtonDisplayed(self):
        return self.browser.find_element(*self.CONTACT_US_BUTTON).is_displayed()

    def clickPortfolioButton(self):
        self.browser.find_element(*self.PORTFOLIO_BUTTON).click()

    def isPortfolioButtonDisplayed(self):
        return self.browser.find_element(*self.PORTFOLIO_BUTTON).is_displayed()

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_PAGE).text

    def isElementalDisplayed(self):
        return self.browser.find_element(*self.MIDDLE_PAGE).is_displayed()

    def clickElemental(self):
        self.browser.find_element(*self.MIDDLE_PAGE).click()


