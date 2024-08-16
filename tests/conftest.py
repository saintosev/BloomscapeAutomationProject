import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    print("Start a new test suite")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('log-level=INT')
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    url = "https://bloomscape.com/"
    driver.get(url)
    driver.maximize_window()

    yield driver

    print("\nFinish test")
    time.sleep(30)
    driver.quit()


@pytest.fixture(scope="module")
def set_group():
    print("\nEnter system")
    yield
    print("Exit system")
