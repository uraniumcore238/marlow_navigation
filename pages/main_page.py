import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class MainPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    MAIN_PAGE_BANNER = (By.CSS_SELECTOR, "#desktop-banner")
    LEFT_NAVIGATION_BUTTON = (By.CSS_SELECTOR, "#nav-main .nav-left")
    LEFT_MENU = (By.CSS_SELECTOR, "#hmenu-container")

    def assert_the_banner(self):
        with allure.step("Check visibility of main banner on the main page"):
            self.see(MainPage.MAIN_PAGE_BANNER)

    def go_to_main_menu(self):
        self.click(MainPage.LEFT_NAVIGATION_BUTTON, 'Click on left burger button')
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(MainPage.LEFT_MENU))
