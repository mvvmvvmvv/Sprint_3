from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import HomePageLocators


class TestMainPage:
    def test_buns_enabled_by_default_true(self, driver):
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                HomePageLocators.BUNS_ENABLED))), \
            "Вкладка булочек не активна"

    def test_sauce_enabled_true(self, driver):
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HomePageLocators.SAUCE))).click(), \
            "Вкладка соусов не активна"

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                HomePageLocators.SAUCE_ENABLED)))

    def test_fillings_enabled_true(self, driver):
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HomePageLocators.FILLING))).click()

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                HomePageLocators.FILLING_ENABLED))), \
            "Вкладка начинок не активна"
