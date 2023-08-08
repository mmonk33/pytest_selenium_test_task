from pages.portal_login_page import SBPage


class TestPortal:
    def test_button_is_disabled(self, portal_open, browser):
        portal_login_page = SBPage(browser)
        portal_login_page.check_is_button_disabled()

    def test_inputs_is_empty_after_refresh(self, portal_open, browser):
        portal_login_page = SBPage(browser)
        browser.refresh()
        portal_login_page.check_inputs_is_empty()



