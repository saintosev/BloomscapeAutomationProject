import allure
import time
import re
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from selenium.webdriver.support.ui import Select

from utilities.logger import Logger


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    error_message = "//div[@class='styles__content___f7Rp4']"

    subtotal = ("//section[@class='styles__totals___YbWNp']/div[@class='styles__row___RHhaV'][1]/span["
                "@class='styles__value___e5HRC']/bdi")
    shipping = ("//div[@class='styles__row___RHhaV'][span[@class='styles__label___OqcIG' and contains(text(), "
                "'Shipping')]]/span[@class='styles__value___e5HRC']")
    state_sales_tax = ("//div[@class='styles__row___RHhaV'][span[@class='styles__label___OqcIG' and contains(text(), "
                       "'State Sales Tax')]]/span[@class='styles__value___e5HRC']/bdi")
    total = ("//div[@class='styles__row___RHhaV'][span[@class='styles__big-label___GSAfI' and contains(text(), "
             "'Total')]]/span[@class='styles__big-value___JBAmg']/bdi")

    continue_button_1 = "//button[@class='styles__root___EeWwL styles__button___G1Zqf' and text()='Continue']"
    continue_button_2 = "//button[@class='styles__root___EeWwL styles__button___npKeS' and text()='Continue']"
    continue_button_3 = "//button[@class='styles__root___EeWwL styles__button___qbaol' and text()='Continue']"
    first_name_field = "//input[@name='shippingInfo.firstName']"
    last_name_field = "//input[@name='shippingInfo.lastName']"
    street_address_field = "//input[@name='shippingInfo.streetAddress1']"
    city_field = "//input[@name='shippingInfo.city']"
    state_field = "//select[@name='shippingInfo.state']"
    zip_field = "//input[@name='shippingInfo.zip']"
    phone_field = "//input[@name='shippingInfo.phone']"
    express_shipping_option = "//label[section[contains(text(),'Express Shipping')]]//input[@type='radio']"
    continue_shopping_button = "//a[@href='/shop' and text()='Continue Shopping']"

    # Getters
    def get_error_message(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.error_message)))

    def get_subtotal(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.subtotal)))

    def get_shipping(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.shipping)))

    def get_state_sales_tax(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.state_sales_tax)))

    def get_total(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.total)))

    def get_continue_button_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.continue_button_1)))

    def get_continue_button_2(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.continue_button_2)))

    def get_continue_button_3(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.continue_button_3)))

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_street_address_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.street_address_field)))

    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.city_field)))

    def get_state_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.state_field)))

    def get_zip_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.zip_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_express_shipping_option(self):
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH,
                                                                                    self.express_shipping_option)))

    # Actions
    def click_continue_button_1(self):
        self.get_continue_button_1().click()
        print("Click the 'Continue' button")

    def click_continue_button_2(self):
        self.get_continue_button_2().click()
        print("Click the 'Continue' button")

    def click_continue_button_3(self):
        self.get_continue_button_3().click()
        print("Click the 'Continue' button")

    def fill_in_first_name_field(self, first_name):
        self.get_first_name_field().send_keys(first_name)
        print("Fill in the first name field")

    def fill_in_last_name_field(self, last_name):
        self.get_last_name_field().send_keys(last_name)
        print("Fill in the last name field")

    def fill_in_street_address_field(self, street_address):
        self.get_street_address_field().send_keys(street_address)
        print("Fill in the street address field")

    def fill_in_city_field(self, city_name):
        self.get_city_field().send_keys(city_name)
        print("Fill in the city field")

    def select_state(self, state_name):
        state_dropdown = self.get_state_field()
        state_dropdown.click()
        select = Select(state_dropdown)
        select.select_by_value(state_name)
        print("Select the state")

    def fill_in_zip_field(self, zip):
        self.get_zip_field().send_keys(zip)
        print("Fill in the zip-code field")

    def fill_in_phone_field(self, phone_number):
        self.get_phone_field().send_keys(phone_number)
        print("Fill in the phone number field")

    def select_express_shipping_option(self):
        self.get_express_shipping_option().click()
        print("Select the 'Express Shipping' option")

    # Methods
    def checkout(self, subtotal_in_the_cart):
        """Making an order, which includes checking for an expired session error, entering user fake data before
        filling out billing information."""

        with allure.step("checkout"):
            Logger.add_start_step("checkout")
            self.assert_url("https://bloomscape.com/checkout/")

            try:
                self.get_error_message()
                print("Try to use the VPN connected to the US servers. Otherwise it will be impossible to work with "
                      "the Checkout page.")
                print("You'll be redirected to the 'Shop All' page")
                self.get_screenshot()
                Logger.add_end_step(self.driver.current_url, "checkout")

            except TimeoutException:

                subtotal_in_the_checkout = self.get_subtotal().text
                self.assert_price(subtotal_in_the_checkout, subtotal_in_the_cart)
                fake_first_name, fake_last_name, fake_address, fake_city, fake_zip, fake_phone = self.faker()
                self.click_continue_button_1()
                self.fill_in_first_name_field(fake_first_name)
                self.fill_in_last_name_field(fake_last_name)
                self.fill_in_street_address_field(fake_address)
                self.fill_in_city_field(fake_city)
                self.select_state("NY")
                self.fill_in_zip_field(fake_zip)
                self.fill_in_phone_field(fake_phone)
                self.click_continue_button_2()
                self.select_express_shipping_option()
                time.sleep(5)
                self.click_continue_button_3()

                shipping_in_the_checkout = self.get_shipping().text
                state_sales_tax_in_the_checkout = self.get_state_sales_tax().text
                total_in_the_checkout = self.get_total().text
                subtotal_in_the_checkout_num = float(subtotal_in_the_checkout.replace('$', "").replace(',', ""))
                match = re.search(r'\$([\d.]+)', shipping_in_the_checkout)
                if match:
                    shipping_in_the_checkout_num = float(match.group(1))
                else:
                    shipping_in_the_checkout_num = 0.0
                state_sales_tax_in_the_checkout_num = float(state_sales_tax_in_the_checkout.replace("$", "").replace(',', ""))
                total_in_the_checkout_num = float(total_in_the_checkout.replace("$", "").replace(',', ""))

                actual_total = (subtotal_in_the_checkout_num + shipping_in_the_checkout_num +
                                state_sales_tax_in_the_checkout_num)
                self.assert_price(actual_total, total_in_the_checkout_num)

                print("Please review the Billing Information")
                self.get_screenshot()
                Logger.add_end_step(self.driver.current_url, "checkout")
