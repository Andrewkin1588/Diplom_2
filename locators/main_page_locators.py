from selenium.webdriver.common.by import By

PERSONAL_ACCOUNT_LINK = [By.XPATH, "//a[@href='/account']/p"]
FEED_ORDER = [By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[contains(text(),'Лента Заказов')]"]
CONSTRUCTOR = [By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[contains(text(),'Конструктор')]"]
INGREDIENT = [By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"]
INFO_INGREDIENT = [By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']"]
MODAL_CROSS = [By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
COUNTER = [By.XPATH, "//p[@class='counter_counter__num__3nue1']"]
CONSTRUCTOR_TOP = [By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']"]
CREATE_ORDER = [By.XPATH, "//button[contains(text(),'Оформить заказ')]"]
