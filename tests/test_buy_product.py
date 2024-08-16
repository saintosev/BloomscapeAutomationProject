import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.shop_all_plants_page import ShopAllPlantsPage
from pages.product_card_page import ProductCardPage
from pages.your_cart import YourCart
from pages.checkout_page import CheckoutPage


@allure.description("Test buy product")
def test_buy_product(set_up, set_group):
    """A test that includes user authorization, selecting a specific set of filters, selecting an item that meets the
    filters, adding it to the cart and filling in user information."""

    print("Test #1")

    driver = set_up

    lp = LoginPage(driver)
    mp = MainPage(driver)
    sapp = ShopAllPlantsPage(driver)
    pcp = ProductCardPage(driver)
    yc = YourCart(driver)
    cp = CheckoutPage(driver)

    lp.authorization_from_main_page()
    mp.choose_section_shop_all_plants()
    sapp.select_filters_set_1()
    expected_product_name, expected_product_price = sapp.select_bromeliad_pineapple_plant()
    pcp.add_product_to_the_shopping_cart(expected_product_name, expected_product_price)
    subtotal_in_the_cart = yc.save_subtotal()
    yc.to_checkout_page(expected_product_name, expected_product_price)
    cp.checkout(subtotal_in_the_cart)
