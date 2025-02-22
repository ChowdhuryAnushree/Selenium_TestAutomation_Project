from pages.base_page import BasePage
from pages.sign_in_success_page_locators import SignInSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignInSuccessPage(BasePage):

    def get_register_success_label(self):
        lbl_login_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, SignInSuccessPageLocators.LOGIN_SUCCESS_LBL).text
        return lbl_login_success_txt

    def click_logout_url(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,SignInSuccessPageLocators.LOGOUT_URL).click()
