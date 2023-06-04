from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Locators import Locators


class TestLoginPage:
    def test_login_from_main_page_successful(self, log_in):
        driver = log_in
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.MAKE_ORDER_BUTTON)))

    def test_login_from_register_page_success(self):
        test_email = "ivanmatveev2000@ya.ru"
        test_pass = "Testpass_123"

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(Locators.REGISTER_PAGE)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.LOGIN_PAGE_LINK))).click()

        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_ON_LOGIN).send_keys(test_email)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(test_pass)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.LOG_IN))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.MAKE_ORDER_BUTTON)))

    def test_login_from_reset_password_page_success(self):
        test_email = "ivanmatveev2000@ya.ru"
        test_pass = "Testpass_123"

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(Locators.RESTORE_PASSWORD_PAGE)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.LOGIN_PAGE_LINK))).click()

        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_ON_LOGIN).send_keys(test_email)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(test_pass)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.LOG_IN))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.MAKE_ORDER_BUTTON)))

    def test_login_from_account_button_success(self):
        test_email = "ivanmatveev2000@ya.ru"
        test_pass = "Testpass_123"

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(Locators.HOME_PAGE)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.PROFILE_BUTTON))).click()

        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_ON_LOGIN).send_keys(test_email)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(test_pass)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.LOG_IN))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.MAKE_ORDER_BUTTON)))





