from selenium.webdriver.common.by import By

PASSWORD_FIELD = [By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//input[@type='password']"]
HIDE_PASSWORD = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
ACTIVE_PASSWORD_FIELD = [By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//div[contains(@class,'input_status_active')]"]