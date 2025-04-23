import allure
import requests
from helpers.helpers import Helpers
from constants import BASE_URL


class TestUpdateUser:

    allure.title("с авторизацией")
    def test_update_user_with_auth(self, create_user):
        access_token_created_user = create_user[1].json()['accessToken']
        headers = {"Authorization": access_token_created_user}
        response = requests.patch(url=BASE_URL + 'auth/user', data=create_user[0], headers=headers)
        Helpers().assertion_status_code(response.status_code, 200)
        assert response.json() == {"success": True, "user": {"email": f"{create_user[0].get('email')}", "name": f"{create_user[0].get('name')}"}}


    allure.title("без авторизации")
    def test_update_user_without_auth(self, create_user):
        response = requests.patch(url=BASE_URL + 'auth/user', data=create_user[0], headers='')
        Helpers().assertion_status_code(response.status_code, 401)
        assert response.json() == {"success": False, "message": "You should be authorised"}

