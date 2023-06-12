from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import HeaderLocators
from locators import AuthPagesLocators
from locators import HomePageLocators
from locators import ProfileLocators

from data import Data


class TestUserProfile:
    def test_open_user_profile_success(self, log_in):
        expected_text = Data.PROFILE_INFO_TEXT
        driver = log_in
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HeaderLocators.PROFILE_BUTTON))).click()

        assert WebDriverWait(driver, 3)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    ProfileLocators.PROFILE_DESCRIPTION_TEXT))).text == expected_text, \
            "Страница профиля не открыта (отсутствует пояснительный текст)"

    def test_open_user_profile_and_log_out_success(self, log_in):
        driver = log_in
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HeaderLocators.PROFILE_BUTTON))).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         ProfileLocators.LOG_OUT_BUTTON))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, AuthPagesLocators.LOG_IN))), \
            "Страница логина не открыта"

    def test_open_user_profile_and_navigate_to_constructor(self, log_in):
        driver = log_in
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HeaderLocators.PROFILE_BUTTON))).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HeaderLocators.CONSTRUCTOR))).click()

        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                                HomePageLocators.CONSTRUCTOR_HEADER))), \
            "Страница конструктора не открыта (отсутствует элемент хэдера таблицы)"
