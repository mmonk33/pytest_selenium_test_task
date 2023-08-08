from selenium.webdriver import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.XPATH, "//textarea[@type='search']")


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_word(self, word: str) -> None:
        search = self.find_element(SearchLocators.SEARCH_FIELD)
        search.click()
        search.send_keys(word)

    def press_enter(self) -> None:
        self.find_element(SearchLocators.SEARCH_FIELD, time=2).send_keys(Keys.ENTER)
