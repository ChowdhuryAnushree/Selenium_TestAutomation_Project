import resources.constants
from pages.base_page import BasePage
from pages.home_page_locators import HomePageLocators
from resources.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.support.select import Select


class HomePage(BasePage):
    def select_quantity(self):
        webElementDropDown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, HomePageLocators.QUANTITY_DROPDOWN)
        dropdownSelect = Select(webElementDropDown)
        dropdownSelect.select_by_index(resources.constants.QTY_DROPDOWN_INDEX)
        selected_quantity = dropdownSelect.first_selected_option.text
        print('\n','You have selected', selected_quantity, 'number of items to checkout')

        individual_price = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, HomePageLocators.PRICE)
        individual_price = individual_price.text
        individual_price = individual_price.split("$")[1]
        total_price = int(selected_quantity) * int(individual_price)
        print('\n', 'Your total checkout amount is $' +str(total_price))

    def click_buy_now_button(self):
        self.find_element(HomePageLocators.BUY_NOW_BUTTON).click()

    def directed_to_homepage(self):
        redirected_to_homepage = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,HomePageLocators.HOME_PAGE_LABEL).text
        return redirected_to_homepage