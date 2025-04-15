import requests
from helpers.helpers import Helpers
from constants import BASE_URL


class TestUpdateUser:

    def test_update_user_with_auth(self, create_user):
        access_token_created_user = create_user[1].json()['accessToken']
        headers = {"Authorization": access_token_created_user}
        response = requests.patch(url=BASE_URL + 'auth/user', data=create_user[0], headers=headers)
        Helpers().assertion_status_code(response.status_code, 200)

    def test_update_user_without_auth(self, create_user):
        response = requests.patch(url=BASE_URL + 'auth/user', data=create_user[0], headers='')
        Helpers().assertion_status_code(response.status_code, 401)
