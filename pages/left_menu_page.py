import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class LeftMenuPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    DESKTOP_CONTENT = (By.CSS_SELECTOR, ".s-desktop-content")
    LEFT_MENU_TITLE = (By.CSS_SELECTOR, "#hmenu-content .hmenu-visible .hmenu-title")

    def click_on_menu_element(self, menu_name):
        with allure.step(f"Click on {menu_name} menu element first step"):
            self.driver.find_element(By.XPATH, f"//div[@id='hmenu-content']//div[text()='{menu_name}']").click()
            WebDriverWait(self.driver, 20).until(
                expected_conditions.text_to_be_present_in_element(LeftMenuPage.LEFT_MENU_TITLE, menu_name))

    def click_on_menu_element_second_step(self, menu_name):
        with allure.step("Click on certain menu element second step"):
            self.driver.find_element(By.XPATH, f"//div[@id='hmenu-content']//a[text()='{menu_name}']").click()
            self.see(LeftMenuPage.DESKTOP_CONTENT)
