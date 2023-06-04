import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Locators import Locators


@pytest.fixture
def driver():
    url = "https://stellarburgers.nomoreparties.site"
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def log_in(driver):
    test_email = "ivanmatveev2000@ya.ru"
    test_pass = "Testpass_123"

    WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                     Locators.LOGIN_BUTTON))).click()
    driver.find_element(By.XPATH, Locators.INPUT_EMAIL_ON_LOGIN).send_keys(test_email)
    driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(test_pass)
    WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                     Locators.LOG_IN))).click()
    return driver



