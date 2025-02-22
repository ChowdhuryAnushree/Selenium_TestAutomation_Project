from selenium.webdriver.common.by import By


class SignInPageLocators:

    USER_NAME_TEXT_BOX = (By.XPATH, "//input[@name='userName']")
    PASSWORD_TEXT_BOX = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@name='submit']")
