from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import AuthPagesLocators
from urls import Urls
from data import Data
from faker import Faker

faker = Faker()


class TestLoginPage:
    def test_registration_happy_path(self, register):
        driver = register

        assert WebDriverWait(driver, 5)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    AuthPagesLocators.INPUT_EMAIL_ON_LOGIN))), \
            "Страница логина не отображена (специфическое для этой страницы поле ввода имэйла отсутствует)"

    def test_registration_invalid_password_shows_warning(self, driver):
        test_pass = "123"
        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_NAME).send_keys(Data.TEST_NAME)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_EMAIL).send_keys(faker.email())
        # Вводим слишком короткий пароль
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_PASSWORD).send_keys(test_pass)
        driver.find_element(By.XPATH, AuthPagesLocators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 5)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    AuthPagesLocators.INVALID_PASSWORD_WARNING))), \
            "Предупреждение о невалидности пароля отсутствует"
