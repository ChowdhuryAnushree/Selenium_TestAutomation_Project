from selenium.webdriver.common.by import By


class SignInSuccessPageLocators:

    LOGIN_SUCCESS_LBL = (By.XPATH, "//*[contains(text(), ' Thank you for Loggin.')]")
    LOGOUT_URL = (By.XPATH, "//a[text()='SIGN-OFF']")

