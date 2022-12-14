from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    FAIL_TEXT = (By.CSS_SELECTOR, '[class="flash error"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class^="radius"]')

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def insert_username(self, username):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)

    def insert_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(Keys.ENTER)

    def login(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_login()

    def getFailMessage(self):
        return self.browser.find_element(*self.FAIL_TEXT).text

    def isLoginDisplayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def getButton(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).text
