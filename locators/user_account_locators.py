from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_PROFILE_BUTTON = By.LINK_TEXT, 'Профиль'
    ACCOUNT_HISTORY_BUTTON = By.XPATH, '//*[@href="/account/order-history"]'
    ACCOUNT_EXIT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'
