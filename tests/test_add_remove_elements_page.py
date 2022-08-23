import time
from selenium.webdriver.common.by import By

from pages.add_remove_elements_page import AddRemoveElementsPage


def test_check_add_element_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    #deschidem o pagina
    add_remove_page.load_page()
    add_remove_page.clickAddButton()
    assert add_remove_page.isAddButtonDisplayed(), "Button not displayed"

def test_check_url(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # deschidem o pagina
    add_remove_page.load_page()

def test_title(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # deschidem o pagina
    add_remove_page.load_page()
    assert add_remove_page.isTitleCorrect(), "Incorrect title"

def test_link(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # deschidem o pagina
    add_remove_page.load_page()
    add_remove_page.TheRightLink()

def test_add_and_delete_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # deschidem o pagina
    add_remove_page.load_page()
    add_remove_page.clickAddButton()
    for i in range(10):
        add_remove_page.clickAddButton()
    add_remove_page.clickDeleteButton()
    assert add_remove_page.getNumberOfDeleteButton(), "Not all delete button is displayed "
    for i in range(10):
        add_remove_page.clickFirstDeleteButton()
        delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")
        assert len(delete_button_list) == 10 - i - 1, "Not all delete button are removed"
