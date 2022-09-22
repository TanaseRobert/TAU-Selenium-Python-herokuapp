from selenium.webdriver.common.by import By

class AddRemoveElementsPage:

    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CLASS_NAME, "added-manually")
    TITLE_PAGE = (By.CSS_SELECTOR, "h3")
    MIDDLE_PAGE = (By.CSS_SELECTOR, 'a[target="_blank"]')

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

    def isElementalDisplayed(self):
        return self.browser.find_element(*self.MIDDLE_PAGE).is_displayed()

    def clickElemental(self):
        self.browser.find_element(*self.MIDDLE_PAGE).click()


