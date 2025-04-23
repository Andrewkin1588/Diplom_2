import requests
import pytest
import allure
from helpers.helpers import Helpers
from constants import BASE_URL
from faker import Faker

class TestLogInUser:

    allure.title("логин под существующим пользователем")
    def test_log_in_user(self, create_user):
        with allure.step("Авторизуемся"):
            data_for_log_in = {
                "email": create_user[0].get('email'),
                "password": create_user[0].get('password')
            }
            auth = requests.post(url=BASE_URL + 'auth/login', json=data_for_log_in)
        Helpers().assertion_status_code(auth.status_code, 200)
        del create_user[0]['password']
        assert auth.json()['user'] == create_user[0]

    allure.title("логин с неверным логином и паролем")
    def test_log_in_incorrect_data(self):
        fake = Faker()
        data = {
            "email": fake.email(),
            "password": fake.password()
        }
        with allure.step("Авторизуемся"):
            auth = requests.post(url=BASE_URL + 'auth/login', json=data)
        Helpers().assertion_status_code(auth.status_code, 401)
        assert auth.json() == {"success": False, "message": "email or password are incorrect"}