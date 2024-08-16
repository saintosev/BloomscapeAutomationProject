import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from pages.shop_page import ShopPage
from utilities.logger import Logger


class ShopAllPlantsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_page = ShopPage(driver)

    # Locators
    shop_all_plants_header = "//header[@class='shop__header']/h2[contains(text(), 'Shop All Plants')]"

    # Getters
    def get_shop_all_plants_header(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.shop_all_plants_header)))

    # Actions

    # Methods
    def select_filters_set_1(self):
        """Selecting a specific set of filters, which includes checking whether the desired checkbox is selected"""

        with allure.step("select_filters_set_1"):
            Logger.add_start_step("select_filters_set_1")
            self.shop_page.click_indoor_light_filter()
            self.shop_page.click_indoor_light_partial_bright_indirect_checkbox()
            time.sleep(10)
            self.shop_page.is_checkbox_selected(self.shop_page.get_indoor_light_partial_bright_indirect_checkbox())
            self.shop_page.click_plant_size_filter()
            self.shop_page.click_plant_size_sm_checkbox()
            time.sleep(5)
            self.shop_page.is_checkbox_selected(self.shop_page.get_plant_size_sm_checkbox())
            self.shop_page.click_difficulty_filter()
            self.shop_page.click_difficulty_no_fuss_checkbox()
            time.sleep(5)
            self.shop_page.is_checkbox_selected(self.shop_page.get_difficulty_no_fuss_checkbox())
            self.shop_page.click_pet_friendly_filter()
            self.shop_page.click_pet_friendly_yes_checkbox()
            time.sleep(5)
            self.shop_page.is_checkbox_selected(self.shop_page.get_pet_friendly_yes_checkbox())
            time.sleep(2)
            self.move_to_element(self.shop_page.get_plants_made_simple_header())
            time.sleep(2)
            self.shop_page.click_air_cleaner_filter()
            self.shop_page.click_air_cleaner_yes_checkbox()
            time.sleep(5)
            self.shop_page.is_checkbox_selected(self.shop_page.get_air_cleaner_yes_checkbox())
            self.shop_page.click_outdoor_light_filter()
            time.sleep(2)
            self.shop_page.is_checkbox_selected(self.shop_page.get_outdoor_light_6_or_more_checkbox())
            self.shop_page.click_color_filter()
            self.shop_page.is_checkbox_selected(self.shop_page.get_color_assorted_checkbox())
            time.sleep(2)
            self.shop_page.click_price_filter()
            self.shop_page.click_price_50_100_checkbox()
            time.sleep(5)
            self.shop_page.is_checkbox_selected(self.shop_page.get_price_50_100_checkbox())
            self.move_to_element(self.get_shop_all_plants_header())
            Logger.add_end_step(self.driver.current_url, "select_filters_set_1")

    def select_bromeliad_pineapple_plant(self):
        """Selecting a specific item"""

        with allure.step("select_bromeliad_pineapple_plant"):
            Logger.add_start_step("select_bromeliad_pineapple_plant")
            product_name = self.product_info(self.shop_page.get_bromeliad_pineapple_header())
            product_price = self.product_price(self.shop_page.get_bromeliad_pineapple_price())
            print(f"Find '{product_name}'")
            print(f"On the 'Shop All plants' page, the product is called '{product_name}' and its price is "
                  f"{product_price}")

            self.shop_page.click_bromeliad_pineapple_header()
            Logger.add_end_step(self.driver.current_url, "select_bromeliad_pineapple_plant")
            return product_name, product_price
