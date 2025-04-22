from selenium.webdriver.common.by import By

FEED_ORDER = [By.XPATH, "//div[@class='OrderFeed_contentBox__3-tWb']"]
ORDER_FROM_FEED_ORDER = [By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"]
MODAL_ORDER = [By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"]
CROSS_MODAL_ORDER = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
ORDERS = [By.XPATH, "//p[@class='text text_type_digits-default']"]
COUNT_ORDER_FEED_ALL_TIME = [By.XPATH, "//div[@class='undefined mb-15']//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
COUNT_ORDER_FEED_TODAY = [By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
ORDER_NUMBER_IN_WORK = [By.XPATH, "//div[@class='OrderFeed_orderStatusBox__1d4q2 mb-15']//ul[last()]/li"]