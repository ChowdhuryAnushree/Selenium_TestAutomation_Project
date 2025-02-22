import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "ac1"
    password = "ac123"
    return [user_name, password]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()