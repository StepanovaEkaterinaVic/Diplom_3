from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDERS_LIST_FORM = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    ORDER_DETAILS = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    FIRST_ORDER_IN_LIST = (By.XPATH, "/descendant::div[@class='OrderHistory_textBox__3lgbs mb-6'][position() = (1)]")
    CREATED_ORDER_FORM = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    CREATED_ORDER_FORM_CLOSE = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    CREATED_ORDER_IN_LIST = (By.XPATH, ".//p[@class = 'text text_type_digits-default' and text()='{}']")
    ALL_TIME_COUNT = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (1)]")
    TODAY_COUNT = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (2)]")
    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2' and text()='{}']")
