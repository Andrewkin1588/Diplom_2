import allure
from constants import BASE_URL
import requests

class Helpers:
    @staticmethod
    def assertion_status_code(actual, expected):
        with allure.step("Проверяем статус код"):
            assert actual == expected, f'Статус код не соответствует ожидаемому. ФР: {actual}, ОР: {expected}'

    @staticmethod
    def clear_data(user):
        with allure.step(f"Удаляем созданного пользователя {user}"):
            requests.delete(url=BASE_URL + 'auth/user', json=user)