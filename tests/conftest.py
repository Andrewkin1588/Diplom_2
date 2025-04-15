import pytest
import requests
from helpers.helpers import Helpers
from constants import BASE_URL
from faker import Faker


@pytest.fixture(scope="function")
def create_user():
    fake = Faker()
    data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
    response = requests.post(url=BASE_URL + 'auth/register', json=data)
    Helpers().assertion_status_code(response.status_code, 200)
    yield data, response
    Helpers().clear_data(response.json()['user'])
