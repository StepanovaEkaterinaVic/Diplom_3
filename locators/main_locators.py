from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.CLASS_NAME, "App_App__aOmNj")
    MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGO_BUTTON = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
    PERSONAL_ACCOUNT_LINK = By.XPATH, ".//p[text()='Личный Кабинет']"
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    CONSTRUCTOR_FORM = (By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']")
    ORDERS_LIST_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    INGREDIENT_BUTTON = (By.XPATH, ".//p[@class = 'BurgerIngredient_ingredient__text__yp3dH' and text()='{}']")
    INGREDIENT_DETAILS_FORM = (By.XPATH, ".//p[@class = 'text text_type_main-medium mb-8' and text()='{}']")
    INGREDIENT_DETAILS_CLOSE = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    INGREDIENT_COUNT = (By.XPATH, ".//p[@class = 'counter_counter__num__3nue1' and text()='{}']")
    INGREDIENTS_IN_BURGER_LIST = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    CONFIRM_ORDER_FORM = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")
