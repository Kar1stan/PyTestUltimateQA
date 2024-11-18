from playwright.sync_api import Page


class TestPricingPage:
    def __init__(self, page: Page):
        self.page = page
        self.fake_pricing_button = page.locator("a[href='../fake-pricing-page']")
        self.free_trial_button = page.locator("(//a[text()='Purchase'])[1]")
        self.basic_button = page.locator("(//a[text()='Purchase'])[2]")
        self.enterprise_button = page.locator("(//a[text()='Purchase'])[3]")
        self.free_price_text = page.locator("//span[text()='$0']")
        self.basic_price_text = page.locator("//span[text()='$80']")
        self.enterprise_price_text = page.locator("//span[text()='$900']")


    def click_fake_pricing_button(self):
        self.fake_pricing_button.click()

    def click_free_trial_button(self):
        self.free_trial_button.click()

    def click_basic_button(self):
        self.basic_button.click()

    def click_enterprise_button(self):
        self.enterprise_button.click()
