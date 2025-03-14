import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    _driver.quit()
