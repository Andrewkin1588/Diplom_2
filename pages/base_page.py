import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_to_url(self, url):
        with allure.step(f"Переходим на страницу: {url}"):
            self.driver.get(url)

    def click_to_element_xpath(self, locator):
        element = self.find_element(locator)
        return element.click()

    def click_to_element_js(self, locator):
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].click();", element)

    def send_keys_to_field(self, locator, text):
        element = self.find_element(locator)
        with allure.step(f"Вводим текст: {text}"):
            element.send_keys(text)

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element

    def get_text_from_elements(self, locator):
        text = []
        element = self.driver.find_elements(*locator)
        for i in element:
            text.append(i.text)
        return text

    def wait_change_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(expected_url))

    def drag_drop(self, source_elem, target_elem):
        action = ActionChains(self.driver)
        from_element = self.find_element(source_elem)
        to_element = self.find_element(target_elem)
        action.drag_and_drop(from_element, to_element).perform()

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_current_url(self):
        return self.driver.current_url
