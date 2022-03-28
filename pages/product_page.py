import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class ProductPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    MAIN_IMAGE = (By.CSS_SELECTOR, "#main-image-container")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")
    CONFIRMATION_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#sw-atc-confirmation")
    PRODUCT_PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "#corePrice_feature_div span[aria-hidden='true']")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "#sw-gtc a")

    def assert_main_image(self):
        with allure.step("Check visibility of main image on product page"):
            self.see(ProductPage.MAIN_IMAGE)

    def add_product_to_cart(self):
        with allure.step("Click on add to cart button"):
            self.click(ProductPage.ADD_TO_CART_BUTTON)
            self.see(ProductPage.CONFIRMATION_PRODUCT_ADDED_TO_CART)

    def push_button_go_to_cart(self):
        with allure.step("Click on go to cart button"):
            self.click(ProductPage.GO_TO_CART_BUTTON)

    def get_product_price_in_product_page(self):
        with allure.step("Get product price on product page"):
            return self.see(ProductPage.PRODUCT_PRICE_ON_PRODUCT_PAGE).text
