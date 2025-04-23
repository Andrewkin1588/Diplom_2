import allure
import pytest
import requests
from constants import BASE_URL
from helpers.helpers import Helpers


class TestCreateOrder:

    allure.title("с авторизацией с ингредиентами/без ингредиентов/с неверным хешем ингредиентов")
    @pytest.mark.parametrize("ingredients,status_code,body_resp", [('61c0c5a71d1f82001bdaaa6d', 200),
                                                         ('', 400, {"success": False, "message": "Ingredient ids must be provided"}),
                                                         ('1234', 500, {"message": "Internal Server Error"})])
    def test_created_orders_with_auth(self, create_user, ingredients, status_code, body_resp):
        access_token_created_user = create_user[1].json()['accessToken']
        data = {
            "ingredients": [ingredients]
        }
        headers = {"Authorization": access_token_created_user}
        response_created_order = requests.post(url=BASE_URL + 'orders', data=data, headers=headers)
        Helpers().assertion_status_code(response_created_order.status_code, status_code)

    allure.title("без авторизации с ингредиентами/без ингредиентов/с неверным хешем ингредиентов")
    @pytest.mark.parametrize("ingredients,status_code", [('61c0c5a71d1f82001bdaaa6d', 200),
                                                         ('', 400),
                                                         ('1234', 500)])
    def test_created_orders_without_auth(self, ingredients, status_code):
        data = {
            "ingredients": [ingredients]
        }
        response_created_order = requests.post(url=BASE_URL + 'orders', data=data)
        Helpers().assertion_status_code(response_created_order.status_code, status_code)

