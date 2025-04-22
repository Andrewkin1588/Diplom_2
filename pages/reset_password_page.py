from pages.base_page import BasePage
from locators.reset_password_page_locators import HIDE_PASSWORD, ACTIVE_PASSWORD_FIELD


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_to_hide_password_text(self):
        self.click_to_element_js(HIDE_PASSWORD)

    def get_active_field(self):
        return self.find_element(ACTIVE_PASSWORD_FIELD)