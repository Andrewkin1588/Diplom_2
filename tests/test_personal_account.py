import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from constants import ORDER_HISTORY_URL, PROFILE_PAGE, LOGIN_PAGE


class TestPersonalAccount:


    allure.title("Тестирование личного кабинета")
    def test_personal_account(self, browser):
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        main_page = MainPage(browser)

        login_page.get_to_login_page()
        with allure.step("Авторизуемся"):
            login_page.log_in()
        with allure.step("Нажимаем на Личный кабинет"):
            main_page.click_to_personal_account_link()
        assert main_page.get_current_url() == PROFILE_PAGE
        with allure.step("Нажимаем на Историю заказов"):
            profile_page.click_history_order()
        assert main_page.get_current_url() == ORDER_HISTORY_URL
        profile_page.log_out()
        assert main_page.get_current_url() == LOGIN_PAGE