import time
from selenium.webdriver.common.by import By

from pages.new_window_page import NewWindowPage
from pages.opening_a_new_window_page import OpeningWindowPage
from pages.selenium_page import SeleniumPage


def test_check_site_utility(browser):
    opening_a_new_windows_page = OpeningWindowPage(browser)
    opening_a_new_windows_page.load_page()
    assert opening_a_new_windows_page.isClickButtonDisplayed(), "Click button not displayed"

def test_check_url(browser):
    opening_a_new_windows_page = OpeningWindowPage(browser)
    opening_a_new_windows_page.load_page()
    assert browser.current_url == opening_a_new_windows_page.URL, "Wrong URL"

def test_title(browser):
    opening_a_new_windows_page = OpeningWindowPage(browser)
    opening_a_new_windows_page.load_page()
    assert "Opening a new window" == opening_a_new_windows_page.getTitlePage(), "Incorrect title page"

def test_link(browser):
    opening_a_new_windows_page = OpeningWindowPage(browser)
    opening_a_new_windows_page.load_page()
    opening_a_new_windows_page.clickButton()
    new_window_page = NewWindowPage(browser)
    assert "New Window" == new_window_page.getHeading(), "Not the correct message"
    assert browser.current_url == new_window_page.URL, "Wrong link"

def test_site_visibility(browser):
    opening_a_new_windows_page = OpeningWindowPage(browser)
    opening_a_new_windows_page.load_page()
    assert opening_a_new_windows_page.isElementalDisplayed(), "Powered by Elemental Selenium - not displayed"
    opening_a_new_windows_page.clickElemental()
    selenium_page = SeleniumPage(browser)
    assert "A free, once-weekly e-mail on how to use Selenium like a Pro" == selenium_page.getWelcomeMessage(), "Wrong welcome message"
    assert browser.current_url == selenium_page.URL, "Wrong URL"
