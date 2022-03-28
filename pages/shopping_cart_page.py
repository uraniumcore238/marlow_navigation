import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class ShoppingCartPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    ACTIVE_CART_MAIN_BLOCK = (By.CSS_SELECTOR, "#sc-active-cart")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, ".sc-product-price")

    def assert_main_block_in_cart(self):
        with allure.step("Check visibility of main block in cart"):
            self.see(ShoppingCartPage.ACTIVE_CART_MAIN_BLOCK)

    def get_the_product_price_in_cart(self):
        with allure.step("Get the product price in cart"):
            return self.see(ShoppingCartPage.PRODUCT_PRICE_IN_CART).text
