import allure

from locators.user_account_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Проверка видимости профиля при  клике на «Личный кабинет».')
    def show_personal_account_window(self):
        return self.get_text_from_element(AccountPageLocators.ACCOUNT_PROFILE_BUTTON)

    @allure.step('Проверка видимости истории при клике на «История заказов» из личного кабинета.')
    def show_personal_orders_history(self):
        self.click_on_element(AccountPageLocators.ACCOUNT_HISTORY_BUTTON)
        return self.get_attribute_value(AccountPageLocators.ACCOUNT_HISTORY_BUTTON, 'aria-current')

    @allure.step('Проверка выхода из аккаунта.')
    def log_out_from_personal_account(self):
        self.click_on_element(AccountPageLocators.ACCOUNT_EXIT_BUTTON)
