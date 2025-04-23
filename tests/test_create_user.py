import json

import requests
import pytest
import allure
from helpers.helpers import Helpers
from constants import BASE_URL
from faker import Faker


class TestCreateUser:

    allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        fake = Faker()
        data = {
            "email": fake.email(),
            "name": fake.name(),
            "password": fake.password()
        }
        with allure.step("Создаем пользователя"):
            response = requests.post(url=BASE_URL + 'auth/register', json=data)
        Helpers().assertion_status_code(response.status_code, 200)
        del data["password"]
        assert response.json()['user'] == data

    allure.title("создать пользователя, который уже зарегистрирован")
    def test_create_registered_users(self, create_user):
        second_user = requests.post(url=BASE_URL + 'auth/register', json=create_user[0])
        Helpers().assertion_status_code(second_user.status_code, 403)
        assert second_user.json() == {"success": False, "message": "User already exists"}


    allure.title("создать пользователя и не заполнить одно из обязательных полей.")
    def test_create_register_user_without_requierd_field(self):
        fake = Faker()
        data = {
            "email": fake.email(),
            "password": fake.password(),
        }
        with allure.step("Создаем пользователя"):
            response = requests.post(url=BASE_URL + 'auth/register', json=data)
        Helpers().assertion_status_code(response.status_code, 403)
        assert response.json() == {"success": False, "message": "Email, password and name are required fields"}

