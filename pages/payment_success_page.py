from pages.base_page import BasePage
from pages.payment_success_page_locators import PaymentSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class PaymentSuccessPage(BasePage):
    def verify_success_message(self):
        return self.find_element(PaymentSuccessPageLocators.SUCCESS_MESSAGE).text == "Payment successfull!"

    def click_home_button(self):
        self.find_element(PaymentSuccessPageLocators.HOME_BUTTON).click()

    def payment_success_label(self):
        payment_success = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,PaymentSuccessPageLocators.PAYMENT_SUCCESS_LBL).text
        return payment_success

