import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    #before tests
    global driver
    # initializam un browser
    s = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    #retun driver
    yield driver
    #after test
    driver.quit()
    return driver

