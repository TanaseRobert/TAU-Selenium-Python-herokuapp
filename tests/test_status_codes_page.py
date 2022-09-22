from pages.selenium_page import SeleniumPage
from pages.status_codes_page import StatusCodesPage
from pages.status_codes_200_page import StatusCodes200Page
from pages.status_codes_301_page import StatusCodes301Page
from pages.status_codes_404_page import StatusCodes404Page
from pages.status_codes_500_page import StatusCodes500Page

def test_check_add_element_functionality(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert status_code_page.isElementalDisplayed, "Button not displayed"

def test_check_url(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert browser.current_url == status_code_page.URL, "Wrong URL"

def test_title(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert "Status Codes" == status_code_page.getTitlePage(), "Incorrect title page"

def test_link(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert status_code_page.isElementalDisplayed(), "Powered by Elemental Selenium - not displayed"
    status_code_page.clickElemental()
    selenium_page = SeleniumPage(browser)
    assert "A free, once-weekly e-mail on how to use Selenium like a Pro" == selenium_page.getWelcomeMessage(), "Not the correct message"
    assert browser.current_url == selenium_page.URL, "Wrong link"

def test_button_200_utility(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert status_code_page.is200ButtonDisplayed(), "Button 200 not displayed"
    status_code_page.click200Button()
    status_code_200_page = StatusCodes200Page(browser)
    assert "This page returned a 200 status code." == status_code_200_page.getMessageDisplayed(), "Incorrect message displayed"
    assert browser.current_url == status_code_200_page.URL, "Wrong Link"

def test_button_301_utility(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert status_code_page.is301ButtonDisplayed(), "Button 301 not displayed"
    status_code_page.click301Button()
    status_code_301_page = StatusCodes301Page(browser)
    assert "This page returned a 301 status code." == status_code_301_page.getMessageDisplayed(), "Incorrect message displayed"
    assert browser.current_url == status_code_301_page.URL, "Wrong Link"

def test_button_404_utility(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert status_code_page.is404ButtonDisplayed(), "Button 404 not displayed"
    status_code_page.click404Button()
    status_code_404_page = StatusCodes404Page(browser)
    assert "This page returned a 404 status code." == status_code_404_page.getMessageDisplayed(), "Incorrect message displayed"
    assert browser.current_url == status_code_404_page.URL, "Wrong Link"

def test_button_500_utility(browser):
    status_code_page = StatusCodesPage(browser)
    status_code_page.load_page()
    assert status_code_page.is500ButtonDisplayed(), "Button 500 not displayed"
    status_code_page.click500Button()
    status_code_500_page = StatusCodes500Page(browser)
    assert "This page returned a 500 status code." == status_code_500_page.getMessageDisplayed(), "Incorrect message displayed"
    assert browser.current_url == status_code_500_page.URL, "Wrong Link"





