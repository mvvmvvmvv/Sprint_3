from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Locators import Locators


class TestUserProfile:
    def test_open_user_profile_success(self, log_in):
        expected_text = "В этом разделе вы можете изменить свои персональные данные"
        driver = log_in
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.PROFILE_BUTTON))).click()

        assert WebDriverWait(driver, 3)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    Locators.PROFILE_DESCRIPTION_TEXT))).text == expected_text

    def test_open_user_profile_and_log_out_success(self, log_in):
        driver = log_in
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.PROFILE_BUTTON))).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.LOG_OUT_BUTTON))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.LOG_IN)))

    def test_open_user_profile_and_navigate_to_constructor(self, log_in):
        driver = log_in
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.PROFILE_BUTTON))).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.CONSTRUCTOR))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.CONSTRUCTOR_HEADER)))
