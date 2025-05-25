from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    RECOVERY_CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    RECOVERY_PASSWORD_FIELD = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @name = 'Введите новый пароль']")
    PASSWORD_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']")
