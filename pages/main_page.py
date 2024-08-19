import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    # Locators
    account_button = "//a[@href='https://bloomscape.com/my-account/']"
    cart_menu_button = ("//li[@id='mega-menu-item-308525']//button[@type='button' and @class='cart-toggle menu__cart' "
                        "and @aria-label='View cart']")
    shop_all_plants_link = "//a[text()='Shop Plants']"
    return_to_main_page = "(//a[@class='mega-menu-link'])[1]"

    # Getters
    def get_account_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_cart_menu_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.cart_menu_button)))

    def get_shop_all_plants_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.shop_all_plants_link)))

    def get_return_to_main_page(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.return_to_main_page)))

    # Actions
    def click_account_button(self):
        self.get_account_button().click()
        print("Click the 'Account' button")

    def click_cart_menu_button(self):
        self.get_cart_menu_button().click()
        print("Click the 'Cart' button")

    def click_shop_all_plants_link(self):
        self.get_shop_all_plants_link().click()
        print("Click the 'Shop All Plants' category")

    def click_return_to_main_page(self):
        self.get_return_to_main_page().click()
        print("Click the 'Return to Main page' button")

    # Methods
    def returning_to_main_page(self):
        """Returning to the main page from any other"""

        Logger.add_start_step("returning_to_main_page")
        self.click_return_to_main_page()
        self.assert_url("https://bloomscape.com/")
        print("You're back on the Main page")
        Logger.add_end_step(self.driver.current_url, "returning_to_main_page")

    def choose_section_shop_all_plants(self):
        """Switching to the 'Shop All Plants' category from the main page."""

        with allure.step("choose_section_shop_all_plants"):
            Logger.add_start_step("choose_section_shop_all_plants")
            self.move_to_element(self.get_shop_all_plants_link())
            print("Find the 'Shop All Plants' category")
            self.click_shop_all_plants_link()
            self.assert_url("https://bloomscape.com/shop/shop-all-plants/")
            print("You're in the 'Shop All Plants' category")
            Logger.add_end_step(self.driver.current_url, "choose_section_shop_all_plants")
