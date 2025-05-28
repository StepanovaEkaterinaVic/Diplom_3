import allure

from data import Data, Message
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import RecoveryPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль».')
    def test_recovery_page_transition(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)

        main_page.go_to_personal_account()
        assert recovery_page.go_to_recovery_window() == Message.RECOVER

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить».')
    def test_put_email_for_recovery(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_personal_account()
        recovery_page.go_to_recovery_window()
        login_page.print_user_email(Data.TEST_EMAIL)
        assert recovery_page.go_to_recovery_confirm_window() == Message.ENTER_CODE

    @allure.title("Проверка видимости пароля.")
    def test_recovery_form_field_password_active(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_personal_account()
        recovery_page.go_to_recovery_window()
        login_page.print_user_email(Data.TEST_EMAIL)
        recovery_page.go_to_recovery_confirm_window()
        login_page.print_user_password(Data.TEST_PASSWORD)
        assert recovery_page.change_password_visibility() == Message.TEXT
