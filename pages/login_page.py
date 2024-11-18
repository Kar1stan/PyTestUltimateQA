from playwright.sync_api import Page


class TestLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.locator("a[href='http://courses.ultimateqa.com/users/sign_in']")
        self.email_input = page.locator("input[name='user[email]']")
        self.password_input = page.locator("input[name='user[password]']")
        self.signin_button = page.locator("button[type='submit']")
        self.checkbox_button = page.locator("input[type='checkbox']")
        self.error_message = page.locator("li[class='form-error__list-item']")

    def click_login_button(self):
        self.login_button.click()

    def fill_email_input(self,email):
        self.email_input.fill(email)

    def fill_password_input(self, password):
        self.password_input.fill(password)

    def click_signin_button(self):
        self.signin_button.click()

    def check_checkbox_button(self):
        self.checkbox_button.check()