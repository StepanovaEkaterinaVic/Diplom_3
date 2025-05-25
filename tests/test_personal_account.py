import allure
from pages.user_account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestAccountPage:

    @allure.title('Проверка перехода в персональный аккаунт по кнопке «Личный кабинет».')
    def test_account_page_jump(self, login):
        main_page = MainPage(login)
        account_page = AccountPage(login)
        main_page.go_to_personal_account()
        assert account_page.show_personal_account_window() == 'Профиль'

    @allure.title('Проверка клика и перехода на меню «История» в окне персонального аккаунта.')
    def test_account_history_visibility(self, login):
        main_page = MainPage(login)
        account_page = AccountPage(login)

        main_page.go_to_personal_account()
        assert account_page.show_personal_orders_history() == 'page'

    @allure.title('Проверка выхода из аккаунта при клике на кнопку выход «Выход» в персональном аккаунте.')
    def test_log_out_from_account(self, login):
        main_page = MainPage(login)
        account_page = AccountPage(login)
        login_page = LoginPage(login)

        main_page.go_to_personal_account()
        account_page.log_out_from_personal_account()
        assert login_page.show_authorization_form() == 'Войти'
