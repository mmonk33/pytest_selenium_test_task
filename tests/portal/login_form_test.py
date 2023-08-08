from pages.portal_login_page import SBPage


class TestPortalLoginFields:
    def test_button_is_disabled(self, portal_open):
        portal_login_page = SBPage(portal_open)
        portal_login_page.check_is_button_disabled()

    def test_inputs_is_empty_after_refresh(self, portal_open):
        portal_login_page = SBPage(portal_open)
        portal_login_page.refresh()
        portal_login_page.check_inputs_is_empty()
        portal_login_page.screenshot()
