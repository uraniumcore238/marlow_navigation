import allure
from pages.left_menu_page import LeftMenuPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.products_result_page import ProductResultPage
from pages.shopping_cart_page import ShoppingCartPage
from utilities.BaseClass import BaseClass


class TestVerifyPriceInCart(BaseClass):

    @allure.feature('Allure example feature')
    @allure.story('Allure example story')
    @allure.severity('critical')
    def test_verify_price(self):

        with allure.step("Test check product's price in cart"):

            main_page = MainPage(self.driver)
            left_menu_page = LeftMenuPage(self.driver)
            product_result_page = ProductResultPage(self.driver)
            product_page = ProductPage(self.driver)
            shopping_cart_page = ShoppingCartPage(self.driver)

            electronics_menu_element: str = "Electronics"
            computers_and_accessories_menu_element: str = "Computers & Accessories"
            number_of_product: str = "4"

            with allure.step("Open main menu"):
                main_page.assert_the_banner()
                main_page.go_to_main_menu()
            with allure.step(f"Click on '{electronics_menu_element}' menu element"):
                left_menu_page.click_on_menu_element(electronics_menu_element)
            with allure.step(f"Click on '{computers_and_accessories_menu_element}' menu element"):
                left_menu_page.click_on_menu_element_second_step(computers_and_accessories_menu_element)
            with allure.step(f"Go to the {number_of_product}-th product's page"):
                product_result_page.click_on_the_product(number_of_product)
            with allure.step("Add product to cart on product's page"):
                product_page.assert_main_image()
            with allure.step(f"Get price of the {number_of_product}-th on product page"):
                product_price = product_page.get_product_price_in_product_page()
            with allure.step("Add product to cart"):
                product_page.add_product_to_cart()
            with allure.step("Go to cart"):
                product_page.push_button_go_to_cart()
            with allure.step("Get product's price in cart"):
                shopping_cart_page.assert_main_block_in_cart()
                price_in_cart = shopping_cart_page.get_the_product_price_in_cart()
            with allure.step(f"Check if price in cart is equals to {product_price}-price in product page"):
                self.assertion(product_price, price_in_cart)
