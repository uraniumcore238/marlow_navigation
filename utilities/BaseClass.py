import inspect
import logging
import allure
import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def click(self, selector, allure_text=None):
        """Clicks on an element with the condition of its visibility
        :param selector: Selectors in the form of a tuple (By.*, "selector")
        :param allure_text: Текст для отчета
        """
        with allure.step(f"{allure_text if allure_text is not None else 'Click on element: ' + selector[1]}"):
            element = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(selector))
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.driver.find_element(*selector))
            element.click()

    def see(self, selector, allure_text=None) -> WebElement:
        """
        Waiting for element visibility
        :param selector:  Selectors in the form of a tuple (By.*, "selector")
        :param allure_text: Text for the report (The selector is displayed by default)
        :return: returns the element when it is visible
        """
        if allure_text:
            with allure.step(allure_text):
                pass
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(selector))

    @staticmethod
    def assertion(expected, factual, text_allure='Data verification'):
        """
        Data validation method, to simplify writing in code
        :param expected: Expected value
        :param factual: Actual value
        :param text_allure: Verification text for the report
        """
        with allure.step(f"{text_allure}"):
            assert expected == factual, f'\n{text_allure}\nExpected: {expected}\nActual: {factual}'
