from pages.base_page import BasePage
from locators.forgot_page_locators import EMAIL_FIELD, FORGOT_BUTTON

class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def send_email(self):
        self.send_keys_to_field(EMAIL_FIELD, 'test@mail.ru')

    def click_to_forgot_button(self):
        self.click_to_element_js(FORGOT_BUTTON)