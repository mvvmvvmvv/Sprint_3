import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Locators import Locators
from faker import Faker

faker = Faker()


class TestLoginPage:
    def test_registration_happy_path(self):
        test_name = "TestName"
        test_email = faker.email()
        test_pass = "Testpass_123"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Locators.REGISTER_PAGE)

        driver.find_element(By.XPATH, Locators.INPUT_NAME).send_keys(test_name)
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL).send_keys(test_email)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(test_pass)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.INPUT_EMAIL_ON_LOGIN)))
        driver.quit()

    def test_registration_invalid_password_shows_warning(self):
        test_name = "TestName"
        test_email = faker.email()
        test_pass = "123"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Locators.REGISTER_PAGE)

        driver.find_element(By.XPATH, Locators.INPUT_NAME).send_keys(test_name)
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL).send_keys(test_email)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(test_pass)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.INVALID_PASSWORD_WARNING)))
        driver.quit()
