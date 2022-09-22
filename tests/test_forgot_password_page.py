import time
from selenium.webdriver.common.by import By

from pages.forgot_password_page import ForgotPasswordPage
from pages.internal_server_error_page import InternalServerErrorPage

def test_check_site_utility(browser):
    forgot_password_page = ForgotPasswordPage(browser)
    forgot_password_page.load_page()
    assert forgot_password_page.isRetrieveButtonDisplayed(), "Retrieve button not displayed"

def test_check_url(browser):
    forgot_password_page = ForgotPasswordPage(browser)
    forgot_password_page.load_page()
    assert browser.current_url == forgot_password_page.URL, "Wrong URL"

def test_title(browser):
    forgot_password_page = ForgotPasswordPage(browser)
    forgot_password_page.load_page()
    assert "Forgot Password" == forgot_password_page.getTitlePage(), "Incorrect title page"

def test_email_write(browser):
    forgot_password_page = ForgotPasswordPage(browser)
    forgot_password_page.load_page()
    assert forgot_password_page.isEmailInputDisplayed(), "Can't write your email"

def test_link(browser):
    forgot_password_page = ForgotPasswordPage(browser)
    forgot_password_page.load_page()
    forgot_password_page.insert_email('apov@yahoo.com')
    assert forgot_password_page.isRetrieveButtonDisplayed(), "Retrieve password - not displayed"
    forgot_password_page.clickRetrieveButton()
    internal_server_error_page = InternalServerErrorPage(browser)
    assert "Internal Server Error" == internal_server_error_page.getNews(), "Not the correct message"
    assert browser.current_url == internal_server_error_page.URL, "Wrong link"