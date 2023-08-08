import traceback
from datetime import datetime

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.__driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.__driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.__driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url: str) -> None:
        url = f'https://{url}'
        self.__driver.get(url)

    def click_to(self, locator):
        return self.find_element(locator, time=2).click()

    def wait_tab(self):
        WebDriverWait(self.__driver, 10).until(EC.number_of_windows_to_be(2))
        self.__driver.close()
        self.__driver.switch_to.window(self.__driver.window_handles[-1])

    def screenshot(self):
        stack = traceback.extract_stack()
        self.__driver.save_screenshot(f'./screenshots/{stack[-2][2]}{datetime.now()}.png')

    def refresh(self):
        self.__driver.refresh()

    def open_link_in_new_tab(self, element):
        action_chains = ActionChains(self.__driver)
        return action_chains.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
