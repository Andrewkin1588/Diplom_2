import pytest

from webdriver_factory import WebdriverFactory


@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    driver = WebdriverFactory.get_webdriver(request.param)
    yield driver
    driver.close()