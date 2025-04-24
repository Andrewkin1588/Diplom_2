import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:

    allure.title("Тестирование восстановления пароля")
    def test_reset_password(self, browser):
        log_in_page = LoginPage(browser)
        forgot_password = ForgotPasswordPage(browser)
        reset_password = ResetPasswordPage(browser)

        log_in_page.get_to_login_page()
        with allure.step("Нажимаем на ссылку 'Восстановить пароль'"):
            log_in_page.click_to_reset_password_link()
        with allure.step("Заполняем поле Email и нажимаем на кнопку Восстановить"):
            forgot_password.send_email()
            forgot_password.click_to_forgot_button()
        with allure.step("Нажимаем на кнопку Показать/Скрыть"):
            reset_password.click_to_hide_password_text()
        assert reset_password.get_active_field()
