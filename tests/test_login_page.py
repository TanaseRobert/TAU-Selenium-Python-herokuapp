from pages.login_page import LoginPage
from time import sleep
import pytest

from pages.secure_page import SecurePage

def test_login_check_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert "Welcome to the Secure Area. When you are done click logout below." == secure_page.getWelcomeMessage(), "Not the correct message"
    assert browser.current_url == secure_page.URL, "Wrong URL"

def test_login_fail(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tom", "SuperSecret")
    assert "Your username is invalid!" == login_page.getFailMessage(), "Not the correct failed message"
    assert browser.current_url == login_page.URL, "Wrong URL"
    assert "Login" == login_page.getButton(), "Incorrect text displayed on button"

def test_login_successfully(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert "You logged into a secure area!" == secure_page.getGoodNews(), "Not the correct message"
    assert browser.current_url == secure_page.URL, "Wrong URL"

def test_incorrect_password(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecret")
    assert "Your username is invalid!" == login_page.getFailMessage(), "Not the correct failed message"
    assert browser.current_url == login_page.URL, "Wrong URL"

def test_login_complete_process(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert "You logged into a secure area!" == secure_page.getGoodNews(), "Not the correct message"
    assert "Welcome to the Secure Area. When you are done click logout below." == secure_page.getWelcomeMessage(), "Not the correct message"
    assert browser.current_url == secure_page.URL, "Wrong URL"
    assert "Logout" == secure_page.getButton(), "Incorrect text displayed on button"
    secure_page.clickLogoutButton()
    assert browser.current_url == login_page.URL, "Wrong URL"

def test_incorrect_username(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tom", "SuperSecretPassword!")
    assert "Your username is invalid!" == login_page.getFailMessage(), "Not the correct failed message"
    assert browser.current_url == login_page.URL, "Wrong URL"





