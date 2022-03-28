import allure
from selenium.webdriver.common.by import By


class ProductResultPage:
    def __init__(self, driver):
        self.driver = driver

    ALL_PRODUCT_CARDS = (By.CSS_SELECTOR, ".s-result-item")

    def click_on_the_product(self, index_of_the_product):
        with allure.step(f"Go to the {index_of_the_product}-th product page"):
            self.driver.find_element(By.XPATH, f"//div[@data-component-type='s-search-result']"
                                               f"[{index_of_the_product}]").click()
