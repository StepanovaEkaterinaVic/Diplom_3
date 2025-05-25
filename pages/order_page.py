import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Проверка отображения формы ленты заказов.')
    def show_orders_list_form(self):
        return self.find_element_with_waiting(OrderPageLocators.ORDERS_LIST_FORM)

    @allure.step('Отображение формы с деталями заказа.')
    def show_order_details_form(self):
        self.click_on_element_action(OrderPageLocators.FIRST_ORDER_IN_LIST)
        return self.get_text_from_element(OrderPageLocators.ORDER_DETAILS)

    @allure.step('Получение номера нового заказа.')
    def get_number_of_created_order(self):
        self.wait_for_element_to_change_text(OrderPageLocators.CREATED_ORDER_FORM, '9999')
        order_number = self.get_text_from_element(OrderPageLocators.CREATED_ORDER_FORM)
        self.click_on_element_action(OrderPageLocators.CREATED_ORDER_FORM_CLOSE)
        return order_number

    @allure.step('Поиск заказа по номеру из раздела «История заказов».')
    def show_user_order(self, order_number):
        order_in_list_formatted = self.format_locator(OrderPageLocators.CREATED_ORDER_IN_LIST, order_number)
        return self.get_text_from_element(order_in_list_formatted)

    @allure.step('Проверка счётчика «Выполнено за всё время».')
    def show_all_time_done_orders(self):
        all_time_count = self.get_text_from_element(OrderPageLocators.ALL_TIME_COUNT)
        return all_time_count

    @allure.step('Проверка счётчика «Выполнено за сегодня».')
    def show_today_done_orders(self):
        today_count = self.get_text_from_element(OrderPageLocators.TODAY_COUNT)
        return today_count

    @allure.step('Проверка заказа в блоке «В работе».')
    def show_created_order_in_work(self, order_count):
        order_number_in_work_formatted = self.format_locator(OrderPageLocators.ORDER_NUMBER_IN_WORK, order_count)
        return self.get_text_from_element(order_number_in_work_formatted)
