import allure

from locators.main_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открытие личного кабинета.')
    def go_to_personal_account(self):
        self.click_on_element_action(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Переход в окно авторизации')
    def click_main_button(self):
        self.click(MainPageLocators.MAIN_PAGE_BUTTON)

    @allure.step('Открытие ленты заказов.')
    def go_to_orders_list(self):
        self.click_on_element_action(MainPageLocators.ORDERS_LIST_BUTTON)

    @allure.step('Ожидание загрузки главной страницы.')
    def wait_for_main_page(self):
        self.find_element_with_waiting(MainPageLocators.MAIN_PAGE)

    @allure.step('Возврат на главную страницу по кнопке с логотипом.')
    def go_to_main_page(self):
        self.click_on_element_action(MainPageLocators.LOGO_BUTTON)

    @allure.step('Отображение формы с конструктором.')
    def show_constructor_form(self):
        self.click_on_element_action(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        self.click_on_element_action(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.find_element_with_waiting(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Отображение деталей по ингредиентам.')
    def show_ingredients_details(self, ingredient, detail):
        self.click_on_element_action(MainPageLocators.CONSTRUCTOR_BUTTON)
        ingredient_formatted = self.format_locator(MainPageLocators.INGREDIENT_BUTTON, ingredient)
        detail_formatted = self.format_locator(MainPageLocators.INGREDIENT_DETAILS_FORM, detail)
        self.scroll_to_element(ingredient_formatted)
        self.click_on_element_action(ingredient_formatted)
        return self.find_element_with_waiting(detail_formatted)

    @allure.step('Закрытие деталей по ингредиентам.')
    def close_ingredients_details(self, ingredient, detail):
        self.show_ingredients_details(ingredient, detail)
        self.click_on_element_action(MainPageLocators.INGREDIENT_DETAILS_CLOSE)
        return self.find_element_with_waiting(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Перетаскиваем ингредиенты в бургер.')
    def add_ingredients_to_burger(self, ingredient):
        ingredient_formatted = self.format_locator(MainPageLocators.INGREDIENT_BUTTON, ingredient)
        self.scroll_to_element(ingredient_formatted)
        self.drag_and_drop_element(ingredient_formatted, MainPageLocators.INGREDIENTS_IN_BURGER_LIST)

    @allure.step('Просмотр счетчика ингредиентов.')
    def count_ingredients(self, ingredient, count):
        self.add_ingredients_to_burger(ingredient)
        count_formatted = self.format_locator(MainPageLocators.INGREDIENT_COUNT, count)
        return self.get_text_from_element(count_formatted)

    @allure.step('Создание заказа.')
    def confirm_order(self):
        self.click_on_element_action(MainPageLocators.CONFIRM_ORDER_BUTTON)
        return self.get_text_from_element(MainPageLocators.CONFIRM_ORDER_FORM)
