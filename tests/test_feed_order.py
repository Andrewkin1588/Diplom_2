import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.feed_order_page import FeedOrderPage


class TestFeedOrder:

    allure.title("Лента заказов")
    def test_feed_order(self, browser):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        profile_page = ProfilePage(browser)
        feed_order = FeedOrderPage(browser)

        with allure.step("Логинимся"):
            login_page.log_in()
        main_page.click_to_feed_order()
        feed_order.click_to_order_from_feed_order()
        with allure.step("Проверяем открытие информации по заказу"):
            main_page.assertion_modal()
        main_page.click_to_cross_modal()
        with allure.step("Запоминаем значения каунтеров"):
            all_time_order = feed_order.get_all_time_order()
            today_order = feed_order.get_today_order()
        main_page.click_to_constructor()
        with allure.step("Добавляем заказ"):
            main_page.added_ingredient()
        with allure.step("Сохздаем заказ"):
            main_page.click_to_create_order()
            main_page.click_to_cross_modal()
        with allure.step("Переходим на страницу юзера"):
            main_page.click_to_personal_account_link()
        with allure.step("Выбираем историю заказов"):
            profile_page.click_history_order()
        with allure.step("Запоминаем номер заказа"):
            order_number = profile_page.get_order_number()
        main_page.click_to_feed_order()
        with allure.step("Проверяем заказ в ленте заказов"):
            feed_order.find_order_number(order_number)
        with allure.step("Проверяем увеличения каунтеров"):
            assert int(all_time_order) + 1 == int(feed_order.get_all_time_order())
            assert int(today_order) + 1 == int(feed_order.get_today_order())





