import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до  элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу')
    def click_on_element_action(self, locator):
        element = self.find_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)
        element = self.find_element_to_be_clickable(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    @allure.step('Клик по элементу с доп.ожиданием')
    def click_on_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.find_element_to_be_clickable(locator)
        element.click()

    @allure.step('Поиска элемента с ожиданием.')
    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента, пока не станет кликабельным.')
    def find_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получить текст из элемента.')
    def get_text_from_element(self, locator):
        element = self.find_element_with_waiting(locator)
        return element.text

    @allure.step('Форматирование элемента.')
    def format_locator(self, locator, num):
        method, locator_final = locator
        locator_final = locator_final.format(num)
        return method, locator_final

    @allure.step('Заполнить поле текстом.')
    def insert_text_in_field(self, locator, value):
        element = self.find_element_to_be_clickable(locator)
        element.send_keys(value)

    @allure.step('Получеть значение аттрибута.')
    def get_attribute_value(self, locator, attribute):
        element = self.find_element_with_waiting(locator)
        return element.get_attribute(attribute)

    @allure.step('Перетащить элемент.')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_waiting(source_locator)
        target_element = self.find_element_with_waiting(target_locator)
        drag_and_drop(self.driver, source_element, target_element)

    @allure.step('Ожидаем  изменение текста в элементе.')
    def wait_for_element_to_change_text(self, locator, text_to_be_changed):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(
            locator, text_to_be_changed))
        return self.driver.find_element(*locator)
