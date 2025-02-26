from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    CARD_NUMBER = (By.NAME, "card_nmuber")
    MONTH_DROPDOWN = (By.ID, "month")
    YEAR_DROPDOWN = (By.ID, "year")
    CVV = (By.ID, "cvv_code")
    SUBMIT_BUTTON = (By.NAME, "submit")
    PAYMENT_PROCESS = (By.XPATH,"//*[contains(text(),'Payment Process')]")