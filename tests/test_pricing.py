import pytest
import re
from playwright.sync_api import Page, expect
from pages.pricing_page import TestPricingPage
from utils.tools import take_screenshot


class TestUltimateAutomationPricing:

    @pytest.fixture
    def test_before_each(self, new_page):
        self.page = new_page
        self.pricing = TestPricingPage(self.page)

    def test_pricing(self, test_before_each, page):
        """Should verify business plans on pricing page"""
        expect(self.page).to_have_url('https://ultimateqa.com/automation/')
        self.pricing.click_fake_pricing_button()
        self.pricing.click_free_trial_button()
        self.pricing.click_basic_button()
        self.pricing.click_enterprise_button()
        expect(self.pricing.free_price_text).to_contain_text("$0")
        expect(self.pricing.basic_price_text).to_contain_text("$80")
        expect(self.pricing.enterprise_price_text).to_contain_text("$900")
        expect(self.page).to_have_url(re.compile("/automation/fake-pricing-page/"))
        take_screenshot(self.page, "test1: verify fake pricing page")
