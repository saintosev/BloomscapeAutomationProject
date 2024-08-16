# Automation Testing Project (Python + Selenium)
The site used is [Bloomscape](http://bloomscape.com/) — an online store that sells and delivers plants and related products.

The project is based on the principles of Object Oriented Programming and the Page Object Model.
The Pytest framework is used. 
## Project Structure

1. Base 
    This Python Package includes the base_method.py module, which contains a class with base methods. These are universal methods that are used repeatedly later. The module contains the following methods: get page url, check current page url against expected url, check received value against expected value, scroll to the desired element, get product information, generate data, get screenshot.
2. Pages
    This package stores modules of all pages that participate in the tests. At the moment they are:
    - the authorization page; 
    - the main page of the site;
    - two pages of the catalog;
    - a product card page;
    - the shopping cart (not exactly a page, but it is placed in a separate .py file for convenience);
    - the checkout page.

    Each of these pages stores element locators, methods to work with them, and methods that include the steps that are performed on that page. 

3. Tests
This package stores tests that include methods from the Pages package. There is currently one smoke test stored here. 
4. Utilities
    This package contains modules for project logging and a driver for the Chrome browser. 
5. Logs, Screen, Test_results
    The 'Logs', 'Screen', and 'Test_results' folders store logs, screenshots, and Allure report results saved after each test run.

## Test description
Right now, the project includes one smoke test that covers the E2E user path: authorization, selecting a product category, setting filters, selecting an item and adding it to the cart, filling out additional information for payment and shipping. The test is accompanied by checks for correct url, product name, product price on different pages of the site, and verifies the success of user actions.

## Prerequisites
- Python 3.x
- Pytest
- Selenium
- ChromeDriver
- Allure

## Installation and Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/saintosev/BloomscapeAutomationProject.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Running Tests
1. Run the tests with the following command:
    ```
    python -m pytest --alluredir=test_results/ tests/test_buy_product.py
    ```
2. View the test results using Allure:
    ```
    allure serve test_results/ 
    ```

## License

MIT
