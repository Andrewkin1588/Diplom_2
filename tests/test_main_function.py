import time

import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from constants import BASE_URL, ORDER_FEED


class TestMainFunc:

    def test_main_func(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        with allure.step('Переходим на страницу авторизации'):
            login_page.get_to_login_page()
        login_page.log_in()
        with allure.step("Нажимаем на Историю заказов"):
            main_page.click_to_feed_order()
        assert browser.current_url == ORDER_FEED
        with allure.step("Нажимаем на конструктор"):
            main_page.click_to_constructor()
        assert browser.current_url == BASE_URL
        with allure.step("Нажимаем на ингредиент"):
            main_page.click_to_ingredient()
        main_page.assertion_modal()
        with allure.step("Нажимаем на крестик в модальном окне"):
            main_page.click_to_cross_modal()
        with allure.step("Переносим ингредиент в корзину"):
            main_page.added_ingredient()
        main_page.assertion_counter()
