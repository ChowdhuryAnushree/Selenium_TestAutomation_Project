from selenium.webdriver.common.by import By


class PaymentSuccessPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'Payment successfull!')]")
    HOME_BUTTON = (By.XPATH, "//*[contains(text(), 'Home')]")
    PAYMENT_SUCCESS_LBL = (By.XPATH,"// *[contains( @class ,'table-wrapper')]")

