from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class ShopPage(Base):

    # Locators
    product_type_filter = "//div[text()='Product Type']"
    indoor_light_filter = "//div[text()='Indoor Light']"
    indoor_light_partial_bright_indirect_checkbox = "(//div[@role='checkbox' and @data-value='medium'])[1]"
    plant_size_filter = "//div[text()='Plant Size']"
    plant_size_sm_checkbox = "(//div[@role='checkbox' and @data-value='medium'])[2]"
    difficulty_filter = "//div[text()='Difficulty']"
    difficulty_no_fuss_checkbox = "//div[@role='checkbox' and @data-value='no-fuss']"
    pet_friendly_filter = "//div[text()='Pet Friendly']"
    pet_friendly_yes_checkbox = "(//div[@role='checkbox' and @data-value='yes'])[1]"
    air_cleaner_filter = "//div[text()='Air Cleaner']"
    air_cleaner_yes_checkbox = "(//div[@role='checkbox' and @data-value='yes'])[2]"
    outdoor_light_filter = "//div[text()='Outdoor Light']"
    outdoor_light_6_or_more_checkbox = "//div[@role='checkbox' and @data-value='6-or-more']"
    color_filter = "//div[text()='Color']"
    color_assorted_checkbox = "//div[@role='checkbox' and @data-value='assorted-pink-orange-yellow']"
    price_filter = "//div[text()='Price']"
    price_50_100_checkbox = "//div[@role='checkbox' and @data-value='50-99.99']"
    plants_made_simple_header = "//h1[text()='Plants Made Simple']"
    bromeliad_pineapple_header = "//div[@class='product-info']/h2[contains(text(), 'Bromeliad Pineapple')]"
    bromeliad_pineapple_price = ("//div[@class='product-info']/h2[contains(text(), 'Bromeliad "
                                 "Pineapple')]/following-sibling::div[@class='product-info__price']/span["
                                 "@class='woocommerce-Price-amount amount']/bdi[contains(text(), '79')]")

    # Getters
    def get_indoor_light_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.indoor_light_filter)))

    def get_indoor_light_partial_bright_indirect_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH,
                                                                                self.indoor_light_partial_bright_indirect_checkbox)))

    def get_plant_size_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.plant_size_filter)))

    def get_plant_size_sm_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.plant_size_sm_checkbox)))

    def get_difficulty_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.difficulty_filter)))

    def get_difficulty_no_fuss_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH,
                                                                                self.difficulty_no_fuss_checkbox)))

    def get_pet_friendly_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.pet_friendly_filter)))

    def get_pet_friendly_yes_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH,
                                                                                self.pet_friendly_yes_checkbox)))

    def get_air_cleaner_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.air_cleaner_filter)))

    def get_air_cleaner_yes_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.air_cleaner_yes_checkbox)))

    def get_outdoor_light_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.outdoor_light_filter)))

    def get_outdoor_light_6_or_more_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.outdoor_light_6_or_more_checkbox)))

    def get_color_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.color_filter)))

    def get_color_assorted_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.color_assorted_checkbox)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_price_50_100_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.price_50_100_checkbox)))

    def get_plants_made_simple_header(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.plants_made_simple_header)))

    def get_bromeliad_pineapple_header(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.bromeliad_pineapple_header)))

    def get_bromeliad_pineapple_price(self):
        return WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, self.bromeliad_pineapple_price)))

    # Actions
    def click_indoor_light_filter(self):
        self.get_indoor_light_filter().click()
        print("Expand the 'Indoor Light' filter")

    def click_indoor_light_partial_bright_indirect_checkbox(self):
        self.get_indoor_light_partial_bright_indirect_checkbox().click()
        print("Choose the 'Partial/Bright Indirect' indoor light")

    def click_plant_size_filter(self):
        self.get_plant_size_filter().click()
        print("Expand the 'Plant Size' filter")

    def click_plant_size_sm_checkbox(self):
        self.get_plant_size_sm_checkbox().click()
        print("Choose the 'MD (1-2 FT)' plant size")

    def click_difficulty_filter(self):
        self.get_difficulty_filter().click()
        print("Expand the 'Difficulty' filter")

    def click_difficulty_no_fuss_checkbox(self):
        self.get_difficulty_no_fuss_checkbox().click()
        print("Choose the 'No-Fuss' difficulty")

    def click_pet_friendly_filter(self):
        self.get_pet_friendly_filter().click()
        print("Expand the 'Pet Friendly' filter")

    def click_pet_friendly_yes_checkbox(self):
        self.get_pet_friendly_yes_checkbox().click()
        print("Choose 'Yes'")

    def click_air_cleaner_filter(self):
        self.get_air_cleaner_filter().click()
        print("Expand the 'Air Cleaner' Filter")

    def click_air_cleaner_yes_checkbox(self):
        self.get_air_cleaner_yes_checkbox().click()
        print("Choose 'Yes'")

    def click_outdoor_light_filter(self):
        self.get_outdoor_light_filter().click()
        print("Expand the 'Outdoor Light' filter")

    def click_color_filter(self):
        self.get_color_filter().click()
        print("Expand the 'Color' filter")

    def click_price_filter(self):
        self.get_price_filter().click()
        print("Expand the 'Price' filter")

    def click_price_50_100_checkbox(self):
        self.get_price_50_100_checkbox().click()
        print("Choose the '$50-$100' price range")

    def click_bromeliad_pineapple_header(self):
        self.get_bromeliad_pineapple_header().click()
        print("Click the 'Bromeliad Pineapple'")

    # Methods
    def is_checkbox_selected(self, checkbox):
        """Checking if the checkbox in the filters is selected"""

        is_checked = checkbox.get_attribute("aria-checked") == "true"
        if is_checked:
            print("Checkbox is selected")
        else:
            print("Checkbox is not selected")
