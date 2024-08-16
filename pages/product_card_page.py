import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from pages.shop_all_plants_page import ShopAllPlantsPage
from utilities.logger import Logger


class ProductCardPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_all_plants_page = ShopAllPlantsPage(driver)

    # Locators
    card_name = "//h1[@class='product_title entry-title']"
    card_price = "//div[@class='price']"
    add_to_cart_button = "//button[@class='single_add_to_cart_button button alt']"

    # Getters
    def get_card_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.card_name)))

    def get_card_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.card_price)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    # Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click the 'Add to cart' button")

    # Methods
    def add_product_to_the_shopping_cart(self, expected_product_name, expected_product_price):
        """Checking that the name and price of the product in the product card page match the name and price of the
        same product in the Shop All Plants page. Adding a product to the shopping cart """

        with allure.step("add_product_to_the_shopping_cart"):
            Logger.add_start_step("add_product_to_the_shopping_cart")
            actual_product_name = self.product_info(self.get_card_name())
            actual_product_price = self.product_price(self.get_card_price())
            print(f"In the product card page, the product is called '{actual_product_name}' and its price is "
                  f"{actual_product_price}")
            self.compare_product_info(actual_product_name, actual_product_price, expected_product_name,
                                      expected_product_price)

            self.click_add_to_cart_button()
            Logger.add_end_step(self.driver.current_url, "add_product_to_the_shopping_cart")
