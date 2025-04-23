from selenium import webdriver


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == 'chrome':
            return webdriver.Chrome()
        elif browser_name == 'firefox':
            return webdriver.Firefox()