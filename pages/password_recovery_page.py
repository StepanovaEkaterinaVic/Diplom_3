import allure

from locators.password_recovery_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):

    @allure.step('Открытие окна "восстановления пароля".')
    def go_to_recovery_window(self):
        self.click_on_element(RecoveryPageLocators.PASSWORD_RECOVERY_LINK)
        return self.get_text_from_element(RecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Переход на окно с  вводом кода восстановления.')
    def go_to_recovery_confirm_window(self):
        self.click_on_element(RecoveryPageLocators.RECOVERY_BUTTON)
        return self.get_text_from_element(RecoveryPageLocators.RECOVERY_CODE_FIELD)

    @allure.step('Изменение видимости пароля')
    def change_password_visibility(self):
        self.click_on_element_action(RecoveryPageLocators.PASSWORD_VISIBILITY)
        return self.get_attribute_value(RecoveryPageLocators.RECOVERY_PASSWORD_FIELD, 'type')
