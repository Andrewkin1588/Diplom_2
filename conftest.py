import pytest

from pages.base_page import WebdriverFactory


@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    driver = WebdriverFactory.get_webdriver(request.param)
    yield driver
    driver.close()