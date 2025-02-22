from pages.base_page import BasePage
from pages.sign_in_page_locators import SignInPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignInPage(BasePage):

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignInPageLocators.USER_NAME_TEXT_BOX).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(SignInPageLocators.PASSWORD_TEXT_BOX).send_keys(usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(SignInPageLocators.SUBMIT_BUTTON).click()