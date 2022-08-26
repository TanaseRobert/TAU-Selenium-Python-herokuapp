from selenium.webdriver.common.by import By

class AddRemoveElementsPage:
    #locators
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CLASS_NAME, "added-manually")
    TITLE_PAGE = (By.CSS_SELECTOR, "h3")

    # URL
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def clickAddButton(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def clickDeleteButton(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def getNumberOfDeleteButton(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))

    def clickFirstDeleteButton(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def isAddButtonDisplayed(self):
        return self.browser.find_element(*self.ADD_ELEMENT_BUTTON).is_displayed()

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_PAGE).text

    def isTheRightLink(self):
        LINK = "https://the-internet.herokuapp.com/add_remove_elements/"
        if LINK == self.URL:
            self.browser.get(self.URL)

