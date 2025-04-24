from pages.base_page import BasePage
from constants import LOGIN_PAGE
from locators.login_page_locators import FORGOT_PASSWORD_LINK, EMAIL_FILED, PASSWORD_FIELD, LOGIN_BUTTON
from test_data import *

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_to_login_page(self):
        self.get_to_url(LOGIN_PAGE)

    def click_to_reset_password_link(self):
        self.click_to_element_js(FORGOT_PASSWORD_LINK)

    def log_in(self):
        self.get_to_login_page()
        self.send_keys_to_field(EMAIL_FILED, EMAIL)
        self.send_keys_to_field(PASSWORD_FIELD, PASSWORD)
        self.click_to_element_js(LOGIN_BUTTON)
        self.wait_change_url(LOGIN_PAGE)