from pages.base_page import BasePage
from pages.checkout_page_locators import CheckoutPageLocators
from resources import constants
from resources.constants import MAX_WAIT_INTERVAL, MONTH_DROPDOWN_INDEX, YEAR_DROPDOWN_INDEX
from selenium.webdriver.support.select import Select

class CheckoutPage(BasePage):

    def enter_card_number(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckoutPageLocators.CARD_NUMBER).send_keys(constants.CARD_NUMBER)

    def select_card_expiry_month(self):
        webElementDropDown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckoutPageLocators.MONTH_DROPDOWN)
        dropdownSelect = Select(webElementDropDown)
        dropdownSelect.select_by_index(MONTH_DROPDOWN_INDEX)

    def select_card_expiry_year(self):
        webElementDropDown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckoutPageLocators.YEAR_DROPDOWN)
        dropdownSelect = Select(webElementDropDown)
        dropdownSelect.select_by_index(YEAR_DROPDOWN_INDEX)

    def enter_card_cvv(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckoutPageLocators.CVV).send_keys(constants.CVV)

    def click_pay_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckoutPageLocators.SUBMIT_BUTTON).click()

    def verify_page_label(self):
        payments_page_entered = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckoutPageLocators.PAYMENT_PROCESS).text
        return payments_page_entered