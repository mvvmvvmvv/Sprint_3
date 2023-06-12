import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from faker import Faker

from locators import AuthPagesLocators
from locators import HomePageLocators
from urls import Urls
from data import Data

faker = Faker()


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(Urls.HOME_PAGE)
    yield browser
    browser.quit()


# Фикстура выполняет авторизацию С ГЛАВНОЙ СТРАНИЦЫ
@pytest.fixture
def log_in(driver):
    WebDriverWait(driver, 3)\
        .until(ec.visibility_of_element_located((By.XPATH,
                                                HomePageLocators.LOGIN_BUTTON))).click()

    driver.find_element(By.XPATH, AuthPagesLocators.INPUT_EMAIL_ON_LOGIN).send_keys(Data.TEST_EMAIL)
    driver.find_element(By.XPATH, AuthPagesLocators.INPUT_PASSWORD).send_keys(Data.TEST_PASS)
    WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                     AuthPagesLocators.LOG_IN))).click()
    return driver


# Фикстура выполняет регистрацию нового пользователя С ВАЛИДНЫМИ ДАННЫМИ
@pytest.fixture
def register(driver):
    driver.get(Urls.REGISTER_PAGE)

    driver.find_element(By.XPATH, AuthPagesLocators.INPUT_NAME).send_keys(Data.TEST_NAME)
    driver.find_element(By.XPATH, AuthPagesLocators.INPUT_EMAIL).send_keys(faker.email())
    driver.find_element(By.XPATH, AuthPagesLocators.INPUT_PASSWORD).send_keys(Data.TEST_PASS)
    driver.find_element(By.XPATH, AuthPagesLocators.REGISTER_BUTTON).click()

    return driver


