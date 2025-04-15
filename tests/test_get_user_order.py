import requests
from constants import BASE_URL
from helpers.helpers import Helpers


class TestGetUserOrder:

    def test_get_user_order(self, create_user):
        headers = {'Authorization': create_user[1].json()['accessToken']}
        response = requests.get(url=BASE_URL + 'orders', headers=headers)
        Helpers().assertion_status_code(response.status_code, 200)

    def test_get_user_order_without_auth(self):
        response = requests.get(url=BASE_URL + 'orders')
        Helpers().assertion_status_code(response.status_code, 401)
