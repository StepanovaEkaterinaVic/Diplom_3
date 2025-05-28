import allure
from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Проверяем отображение окна авторизации.')
    def show_authorization_form(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ввод пароля пользователя.')
    def print_user_password(self, password):
        self.insert_text_in_field(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Ввод почты пользователя.')
    def print_user_email(self, email):
        self.insert_text_in_field(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
