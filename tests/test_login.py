import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import TestLoginPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestUltimateAutomationLogin:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.login = TestLoginPage(self.page)

    def test_login(self, test_before_each, page):
        """Should test log in on login page"""
        expect(self.page).to_have_url('https://ultimateqa.com/automation/')
        self.login.click_login_button()
        self.login.fill_email_input(Data.login_email)
        self.login.fill_password_input(Data.login_password)
        self.login.check_checkbox_button()
        self.login.click_signin_button()
        expect(self.page).to_have_url(re.compile("/users/sign_in"))
        expect(self.login.error_message).to_be_visible()
        take_screenshot(self.page, "test2: test login page")