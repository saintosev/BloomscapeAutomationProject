import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from pages.main_page import MainPage
from utilities.logger import Logger


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.main_page = MainPage(driver)

    # Locators
    log_in_header = "//h2[text()='Log In']"
    email_address = "//input[@name='username']"
    password = "//input[@name='password']"
    log_in_button = "//button[@name='login']"
    hello_paragraph = "//div[@class='woocommerce-MyAccount-content']//p[contains(text(), 'Hello')]"

    # Getters
    def get_log_in_header(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.log_in_header)))

    def get_email_address(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.email_address)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.password)))

    def get_log_in_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.log_in_button)))

    def get_hello_paragraph(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.hello_paragraph)))

    # Actions
    def input_email_address(self, email_address):
        self.get_email_address().send_keys(email_address)
        print("Enter the email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Enter the password")

    def click_log_in_button(self):
        self.get_log_in_button().click()
        print("Click the 'Log in' button")

    # Methods
    def authorization_from_main_page(self):
        """Authorization, which includes switching from the main page of the store to the login page, filling in the
        mail and password, performing several checks, and returning to the main page."""

        with allure.step("authorization_from_main_page"):
            Logger.add_start_step("authorization_from_main_page")

            mail_used = "helagof163@biowey.com"
            password_used = "dih-4UL-par-Apf"

            print("You're on the Main page")
            self.main_page.click_account_button()
            self.assert_word(self.get_log_in_header(), "Log In")
            print("You're on the Login page")
            self.input_email_address(mail_used)
            self.input_password(password_used)
            self.click_log_in_button()
            self.assert_word(self.get_hello_paragraph(), f"Hello {mail_used} (not {mail_used}? Log out)")
            print("Authorization was successful")
            self.main_page.returning_to_main_page()
            Logger.add_end_step(self.driver.current_url, "authorization_from_main_page")
