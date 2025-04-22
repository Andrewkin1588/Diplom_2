import time

from pages.base_page import BasePage
from locators.profile_page_locators import *
from constants import ORDER_HISTORY_URL


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_history_order(self):
        self.click_to_element_js(ORDER_HISTORY)
        time.sleep(1)

    def log_out(self):
        self.click_to_element_js(LOG_OUT)

    def get_order_number(self):
        return self.get_text_from_element(ORDER_NUMBER)

    def click_to_order(self):
        return self.click_to_element_js(ORDER)

    def click_close_modal(self):
        return self.click_to_element_js(CROSS_MODAL)
