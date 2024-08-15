import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    account_button = "//a[@href='https://bloomscape.com/my-account/']"
    shop_all_plants_link = "//a[text()='Shop Plants']"

    # Getters
    def get_account_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_shop_all_plants_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.shop_all_plants_link)))

    # Actions
    def click_account_button(self):
        self.get_account_button().click()
        print("Click account button")

    def click_shop_all_plants_link(self):
        self.get_shop_all_plants_link().click()
        print("Click 'Shop All Plants' section")

    # Methods
    def choose_section_shop_all_plants(self):
        self.move_to_element(self.get_shop_all_plants_link(), self.shop_all_plants_link)
        print("Find 'Shop All Plants' section")
        self.click_shop_all_plants_link()
        self.assert_url("https://bloomscape.com/shop/shop-all-plants/")
        print("You're in the 'Shop All Plants' section")
