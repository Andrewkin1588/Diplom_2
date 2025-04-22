from selenium.webdriver.common.by import By

ORDER_HISTORY = [By.XPATH, "//a[@href='/account/order-history']"]
LOG_OUT = [By.XPATH, "//button[@type='button']"]
ORDER_NUMBER = [By.XPATH, "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']//li[last()]//p"]
ORDER = [By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']/a"]
CROSS_MODAL = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]