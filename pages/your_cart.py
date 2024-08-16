import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from pages.shop_all_plants_page import ShopAllPlantsPage
from utilities.logger import Logger


class YourCart(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_all_plants_page = ShopAllPlantsPage(driver)

    # Locators
    your_cart_header = "//span[text()='Your Cart']"
    bromeliad_pineapple_name = "//a[@class='xoo-wsc-product__name' and contains(text(), 'Bromeliad Pineapple')]"
    bromeliad_pineapple_price = ("//a[@class='xoo-wsc-product__name' and contains(text(), 'Bromeliad "
                                 "Pineapple')]/following-sibling::span[@class='woocommerce-Price-amount amount']")
    checkout_button = "//a[@href='https://bloomscape.com/checkout/']"
    subtotal = ("//div[@class='xoo-wsc-subtotal xoo-wsc-tool']/span[@class='xoo-wsc-tools-value']/span["
                "@class='woocommerce-Price-amount amount']/bdi")

    # Getters
    def get_your_cart_header(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH,
                                                                                self.your_cart_header)))

    def get_bromeliad_pineapple_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH,
                                                                                self.bromeliad_pineapple_name)))

    def get_bromeliad_pineapple_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH,
                                                                                self.bromeliad_pineapple_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_subtotal(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.subtotal)))

    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click the 'Checkout' button")

    # Methods
    def save_subtotal(self):
        """Calculating the subtotal price"""

        with allure.step("save_subtotal"):
            subtotal_in_the_cart = self.get_subtotal().text
            return subtotal_in_the_cart

    def to_checkout_page(self, expected_product_name, expected_product_price):
        """Checking that the name and price of the product in the shopping cart match the name and price of the
        same product in the Shop All Plants page. Switching to the Checkout Page"""

        with allure.step("to_checkout_page"):
            Logger.add_start_step("to_checkout_page")
            self.assert_word(self.get_your_cart_header(), "Your Cart")
            actual_product_name = self.product_info(self.get_bromeliad_pineapple_name())
            actual_product_price = self.product_price(self.get_bromeliad_pineapple_price())
            print(f"In the shopping cart, the product is called '{actual_product_name}' and its price is "
                  f"{actual_product_price}")
            self.compare_product_info(actual_product_name, actual_product_price, expected_product_name,
                                      expected_product_price)

            time.sleep(5)
            self.click_checkout_button()
            Logger.add_end_step(self.driver.current_url, "to_checkout_page")
