import time

from pages.base_page import BasePage
from locators.main_page_locators import *
from constants import BASE_URL


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_to_main_page(self):
        return self.driver.get(BASE_URL)

    def click_to_personal_account_link(self):
        self.click_to_element_js(PERSONAL_ACCOUNT_LINK)
        time.sleep(1)

    def click_to_feed_order(self):
        return self.click_to_element_js(FEED_ORDER)

    def click_to_constructor(self):
        return self.click_to_element_js(CONSTRUCTOR)

    def click_to_ingredient(self):
        return self.click_to_element_js(INGREDIENT)

    def click_to_cross_modal(self):
        return self.click_to_element_js(MODAL_CROSS)

    def assertion_modal(self):
        assert self.find_element(INFO_INGREDIENT)

    def added_ingredient(self):
        self.drag_drop(INGREDIENT, CONSTRUCTOR_TOP)
        time.sleep(1)

    def assertion_counter(self):
        assert int(self.get_text_from_element(COUNTER)) == 2

    def click_to_create_order(self):
        return self.click_to_element_js(CREATE_ORDER)

    def get_order_number(self):
        return self.get_text_from_element(ORDER_NUMBER)


