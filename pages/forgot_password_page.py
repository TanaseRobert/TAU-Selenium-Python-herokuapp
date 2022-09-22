from selenium.webdriver.common.by import By

class ForgotPasswordPage:

    TITLE_PAGE = (By.CSS_SELECTOR, 'h2')
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    RETRIEVE_BUTTON = (By.CSS_SELECTOR, 'button')


    URL = "https://the-internet.herokuapp.com/forgot_password"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def isRetrieveButtonDisplayed(self):
        return self.browser.find_element(*self.RETRIEVE_BUTTON).is_displayed()

    def clickRetrieveButton(self):
        self.browser.find_element(*self.RETRIEVE_BUTTON).click()

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_PAGE).text

    def insert_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def isEmailInputDisplayed(self):
        return self.browser.find_element(*self.EMAIL_INPUT).is_displayed()