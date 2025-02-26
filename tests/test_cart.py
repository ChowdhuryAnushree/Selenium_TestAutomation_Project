from pages.home_page import HomePage
from pages.payment_success_page import PaymentSuccessPage
from resources.constants import TEST_SITE_URL
from pages.checkout_page import CheckoutPage



class TestCart:
    def test_selected_quantity(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to(TEST_SITE_URL)
        home_page.select_quantity()
        home_page.click_buy_now_button()

    def test_payment(self,driver):
        checkout_page = CheckoutPage(driver)
        payments_page_entered_lbl = checkout_page.verify_page_label()
        assert payments_page_entered_lbl.__contains__('Payment Process'), "Error!Still in homepage"
        checkout_page.enter_card_number()
        checkout_page.select_card_expiry_month()
        checkout_page.select_card_expiry_year()
        checkout_page.enter_card_cvv()
        checkout_page.click_pay_button()

    def test_return_to_homepage(self,driver):
        payment_success_page = PaymentSuccessPage(driver)
        payments_success_lbl = payment_success_page.payment_success_label()
        assert payments_success_lbl.__contains__('Order ID'), "Order not processed"
        payment_success_page.click_home_button()
        home_page = HomePage(driver)
        redirected_to_homepage = home_page.directed_to_homepage()
        assert redirected_to_homepage.__contains__('Mother Elephant With Babies Soft Toy'), "Not re-directed to Homepage"