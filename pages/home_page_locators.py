from selenium.webdriver.common.by import By


class HomePageLocators:
    QUANTITY_DROPDOWN = (By.NAME, "quantity")
    BUY_NOW_BUTTON = (By.XPATH, "//*[@value='Buy Now']")
    PRICE = (By.XPATH, "//*[contains(text(), 'Price:')]")
    HOME_PAGE_LABEL = (By.XPATH,"//section[contains(@class,'wrapper')]")