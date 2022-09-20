import time
from selenium.webdriver.common.by import By

from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.selenium_page import SeleniumPage


def test_check_add_element_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.clickAddButton()
    assert add_remove_page.isAddButtonDisplayed(), "Button not displayed"

def test_check_url(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    assert browser.current_url == add_remove_page.URL, "Wrong URL"

def test_title(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    assert "Add/Remove Elements" == add_remove_page.getTitlePage(), "Incorrect title page"

def test_link(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.clickElemental()
    assert add_remove_page.isElementalDisplayed(), "Powered by Elemental Selenium - not displayed"
    selenium_page = SeleniumPage(browser)
    assert "A free, once-weekly e-mail on how to use Selenium like a Pro" == selenium_page.getWelcomeMessage(), "Not the correct message"
    assert browser.current_url == selenium_page.URL, "Wrong link"


def test_add_and_delete_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.clickAddButton()
    for i in range(10):
        add_remove_page.clickAddButton()
    add_remove_page.clickDeleteButton()
    assert add_remove_page.getNumberOfDeleteButton(), "Not all delete button is displayed"
    for i in range(10):
        add_remove_page.clickFirstDeleteButton()
        delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")
        assert len(delete_button_list) == 10 - i - 1, "Not all delete button are removed"
