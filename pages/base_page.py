from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url: str) -> None:
        url = f'https://{url}'
        self.driver.get(url)

    def click_to(self, locator):
        return self.find_element(locator, time=2).click()

    def wait_tab(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
