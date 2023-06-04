from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Locators import Locators


class TestMainPage:
    def test_buns_enabled_by_default_true(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Locators.HOME_PAGE)

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.BUNS_ENABLED)))

    def test_sauce_enabled_true(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Locators.HOME_PAGE)

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.SAUCE))).click()

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.SAUCE_ENABLED)))

    def test_fillings_enabled_true(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Locators.HOME_PAGE)

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                         Locators.FILLING))).click()

        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                                                Locators.FILLING_ENABLED)))
