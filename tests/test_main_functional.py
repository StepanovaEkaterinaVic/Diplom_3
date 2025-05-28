import allure
import pytest
from data import Data, Message
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainPage:
    @allure.title('Проверка клика на «Конструктор».')
    def test_constructor_visibility(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_constructor_form()

    @allure.title('Проверка клика на «Лента заказов».')
    def test_orders_list_visibility(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_orders_list()
        assert order_page.show_orders_list_form()

    @pytest.mark.parametrize(
        'ingredient, detail',
        [
            (Data.TEST_BUN, Data.TEST_BUN),
            (Data.TEST_SAUCE, Data.TEST_SAUCE),
            (Data.TEST_MEAT, Data.TEST_MEAT)
        ]
    )
    @allure.title('Проверка клика на ингредиент.')
    def test_ingredients_details_visibility(self, driver, ingredient, detail):
        main_page = MainPage(driver)
        assert main_page.show_ingredients_details(ingredient, detail)

    @pytest.mark.parametrize(
        'ingredient, detail',
        [
            (Data.TEST_BUN, Data.TEST_BUN),
            (Data.TEST_SAUCE, Data.TEST_SAUCE),
            (Data.TEST_MEAT, Data.TEST_MEAT)
        ]
    )
    @allure.title('Проверка закрытия окна в деталях ингредиента.')
    def test_close_ingredients_details_window(self, driver, ingredient, detail):
        main_page = MainPage(driver)
        assert main_page.close_ingredients_details(ingredient, detail)

    @pytest.mark.parametrize(
        'ingredient, count',
        [
            (Data.TEST_BUN, '2'),
            (Data.TEST_SAUCE, '1'),
            (Data.TEST_MEAT, '1')
        ]
    )
    @allure.title('Проверка увеличения счетчика при добавлении ингредиента.')
    def test_add_ingredients_count_increase(self, driver, ingredient, count):
        main_page = MainPage(driver)
        assert main_page.count_ingredients(ingredient, count) == count

    @pytest.mark.parametrize(
        'ingredient',
        [
            Data.TEST_BUN,
            Data.TEST_SAUCE,
            Data.TEST_MEAT
        ]
    )
    @allure.title('Проверка оформления заказа.')
    def test_authorized_user_confirm_order(self, login, ingredient):
        main_page = MainPage(login)

        main_page.add_ingredients_to_burger(ingredient)
        assert main_page.confirm_order() == Message.ORDER_START_PREPARED
