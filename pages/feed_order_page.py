from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from locators.feed_order_locators import *

class FeedOrderPage(BasePage):

    def click_to_order_from_feed_order(self):
        self.click_to_element_js(ORDER_FROM_FEED_ORDER)

    def find_order_number(self, order):
        assert order in self.get_text_from_elements(ORDERS)

    def get_all_time_order(self):
        return self.get_text_from_element(COUNT_ORDER_FEED_ALL_TIME)

    def get_today_order(self):
        return self.get_text_from_element(COUNT_ORDER_FEED_TODAY)

    def get_order_in_work(self):
        return self.get_text_from_element(ORDER_NUMBER_IN_WORK)
