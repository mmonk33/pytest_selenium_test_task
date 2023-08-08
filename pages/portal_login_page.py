from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SBLocators:
    SEARCH_FIELD = (By.XPATH, "//textarea[@type='search']")
    LOGIN_FORM = (By.XPATH, "//input[@id='auth-form-email']")
    PASS_FORM = (By.XPATH, "//input[@id ='auth-form-password']")
    FEEDBACK_MESSAGE = (By.XPATH, "//span[@class='kc-feedback-text']")
    AUTH_BUTTON = (By.XPATH, "//button[@class='auth__btn']")


class SBPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_is_button_disabled(self):
        _button = self.find_element(SBLocators.AUTH_BUTTON)
        assert _button.get_attribute("disabled"), "Assertion error, button is not disabled"

    def check_inputs_is_empty(self):
        login = self.find_element(SBLocators.LOGIN_FORM).get_attribute("value")
        passw = self.find_element(SBLocators.PASS_FORM).get_attribute("value")
        assert login == passw == '', "Assertion error, fields is not empty"

    def print_feedback_message(self):
        print(self.find_element(SBLocators.FEEDBACK_MESSAGE))
