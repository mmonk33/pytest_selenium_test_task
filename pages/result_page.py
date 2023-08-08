from selenium.webdriver import Keys, ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultLocators:
    FIRST_ITEM = (By.XPATH, "//cite[contains(text(), 'portal.sovcombank.ru')]")
    RESULTS_COUNT = (By.XPATH, "//div[@id='result-stats']")


class Results(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_first_element(self):
        element = self.find_element(SearchResultLocators.FIRST_ITEM, time=2)
        return self.open_link_in_new_tab(element)

    def print_result_count(self):
        print(self.find_element(SearchResultLocators.RESULTS_COUNT).text)
