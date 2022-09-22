from pages.about_page import AboutPage
from pages.disappearing_elements_page import DisappearingElementsPage
from pages.selenium_page import SeleniumPage
from pages.welcome_to_the_internet_page import WelcomeToTheInternetPage

import time
from selenium.webdriver.common.by import By

def test_check_site_visibility(browser):
    disappearing_elements_page = DisappearingElementsPage(browser)
    disappearing_elements_page.load_page()
    assert disappearing_elements_page.isElementalDisplayed(), "Button not displayed"

def test_check_url(browser):
    disappearing_elements_page = DisappearingElementsPage(browser)
    disappearing_elements_page.load_page()
    assert browser.current_url == disappearing_elements_page.URL, "Wrong URL"

def test_title(browser):
    disappearing_elements_page = DisappearingElementsPage(browser)
    disappearing_elements_page.load_page()
    assert "Disappearing Elements" == disappearing_elements_page.getTitlePage(), "Incorrect title page"

def test_link(browser):
    disappearing_elements_page = DisappearingElementsPage(browser)
    disappearing_elements_page.load_page()
    assert disappearing_elements_page.isElementalDisplayed(), "Powered by Elemental Selenium - not displayed"
    disappearing_elements_page.clickElemental()
    selenium_page = SeleniumPage(browser)
    assert "A free, once-weekly e-mail on how to use Selenium like a Pro" == selenium_page.getWelcomeMessage(), "Not the correct welcome message"
    assert browser.current_url == selenium_page.URL, "Wrong link"

def test_home_button(browser):
    disappearing_elements_page = DisappearingElementsPage(browser)
    disappearing_elements_page.load_page()
    assert disappearing_elements_page.isHomeButtonDisplayed(), "Home button doesn't exist"
    disappearing_elements_page.clickHomeButton()
    welcome_to_the_internet_page = WelcomeToTheInternetPage(browser)
    assert "Welcome to the-internet" == welcome_to_the_internet_page.getHeadingMessage(), "Not the correct message"
    assert browser.current_url == welcome_to_the_internet_page.URL, "Wrong link"

def test_about_button(browser):
    disappearing_elements_page = DisappearingElementsPage(browser)
    disappearing_elements_page.load_page()
    assert disappearing_elements_page.isAboutButtonDisplayed(), "Home button doesn't exist"
    disappearing_elements_page.clickAboutButton()
    about_page = AboutPage(browser)
    assert "Not Found" == about_page.getMessageDisplayed(), "Not the correct error"
    assert browser.current_url == about_page.URL, "Wrong link"

