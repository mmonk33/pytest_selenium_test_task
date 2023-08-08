import pytest

from pages.result_page import Results
from pages.search_page import SearchPage
from pages.portal_login_page import SBPage, SBLocators


@pytest.fixture(scope="class")
def portal_open(browser, data_file):
    search_page = SearchPage(browser)
    search_page.go_to_site(data_file[1])
    search_page.enter_word("портал совкомбанк")
    search_page.press_enter()
    results = Results(browser)
    results.print_result_count()
    results.go_to_first_element()
    results.wait_tab()
    sb_page = SBPage(browser)
    sb_page.find_element(SBLocators.LOGIN_FORM).send_keys("login")
    sb_page.find_element(SBLocators.PASS_FORM).send_keys("pass")
    sb_page.click_to(SBLocators.AUTH_BUTTON)
    sb_page.print_feedback_message()
    return browser
