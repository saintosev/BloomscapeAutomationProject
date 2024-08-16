from datetime import datetime
from selenium.webdriver import ActionChains
from faker import Faker


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method get current url"""

        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    def assert_word(self, word, result):
        """Method assert word"""

        value_word = word.text
        assert value_word == result, f"Expected '{result}', but got '{value_word}'"
        print(f"Value word '{value_word}' is OK")

    def assert_url(self, result):
        """Method assert url"""

        get_url = self.driver.current_url
        assert get_url == result, f"Expected URL '{result}', but got '{get_url}'"
        print("URL is correct")

    def assert_price(self, actual_price, expected_price):
        """Method assert price"""

        assert actual_price == expected_price, f"Expected price is {expected_price}, but got {actual_price} instead"
        print(f"Price {actual_price} is correct")

    def move_to_element(self, element):
        """Method move to element"""

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def product_info(self, get_product):
        """Method get product info"""

        product = get_product
        value_product = product.text
        return value_product

    def product_price(self, get_product_price):
        """Method get product price"""

        product_price = get_product_price
        value_product_price = product_price.text
        return value_product_price

    def compare_product_info(self, actual_name, actual_price, expected_name, expected_price):
        """Method compare product info"""

        assert actual_name == expected_name, (f"Product name mismatch: actual name is '{actual_name}' but "
                                              f"expected name is '{expected_name}'")
        assert actual_price == expected_price, (f"Product price mismatch: actual price is {actual_price} but "
                                                f"expected price is {expected_price}")
        print(f"Product name and price match: '{actual_name}' and {actual_price}")

    def faker(self):
        """Method generate random data"""

        faker = Faker("en_US")
        fake_first_name = faker.first_name()
        fake_last_name = faker.last_name()
        fake_address = faker.street_address()
        fake_city = faker.city()
        fake_zip = faker.zipcode()
        fake_phone = faker.basic_phone_number()
        return fake_first_name, fake_last_name, fake_address, fake_city, fake_zip, fake_phone

    def get_screenshot(self):
        """Method screenshot"""

        now_date = datetime.now().strftime("%d-%m-%Y_%H-%M")
        name_screenshot = f"screenshot {now_date}.png"
        self.driver.save_screenshot("C:\\Users\\saintosev\\PycharmProjects\\BloomscapeAutomationProject\\screen\\" +
                                    name_screenshot)
        print("A screenshot was taken.")
