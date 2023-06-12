from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import AuthPagesLocators
from locators import HomePageLocators
from  locators import HeaderLocators
from urls import Urls
from data import Data


class TestLoginPage:
    def test_login_from_main_page_successful(self, log_in):
        driver = log_in
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                                HomePageLocators.MAKE_ORDER_BUTTON))), \
            "Авторизация не выполнена (кнопка заказа не отображена)"

    def test_login_from_register_page_success(self, driver):
        # Открываем страницу регистрации (БЕЗ АВТОРИЗАЦИИ :))
        driver.get(Urls.REGISTER_PAGE)
        # Нажимаем ссылку на страницу авторизации
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         AuthPagesLocators.LOGIN_PAGE_LINK))).click()

        # Прим.: поскольку здесь мы авторизируемся не с главной страницы, а проверяем специфический сценарий,
        # то оптимизировать код целесообразно не запуском фикстуры с авторизацией по-умолчанию (зачем?),
        # а в рамках POM в классе страницы LoginPage (в данном случае). Но мы это пока "не проходили"  :)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_EMAIL_ON_LOGIN).send_keys(Data.TEST_EMAIL)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_PASSWORD).send_keys(Data.TEST_PASS)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         AuthPagesLocators.LOG_IN))).click()

        assert WebDriverWait(driver, 3)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    HomePageLocators.MAKE_ORDER_BUTTON))), \
            "Авторизация не выполнена (кнопка заказа не отображена)"

    def test_login_from_reset_password_page_success(self, driver):
        # Открываем страницу восстановления пароля
        driver.get(Urls.RESTORE_PASSWORD_PAGE)
        # Нажимаем ссылку на страницу авторизации
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         AuthPagesLocators.LOGIN_PAGE_LINK))).click()

        # Прим.: поскольку здесь мы авторизируемся не с главной страницы, а проверяем специфический сценарий,
        # то оптимизировать код целесообразно не запуском фикстуры с авторизацией по-умолчанию (зачем?),
        # а в рамках POM в классе страницы LoginPage (в данном случае). Но мы это пока "не проходили"  :)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_EMAIL_ON_LOGIN).send_keys(Data.TEST_EMAIL)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_PASSWORD).send_keys(Data.TEST_PASS)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         AuthPagesLocators.LOG_IN))).click()

        assert WebDriverWait(driver, 3)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    HomePageLocators.MAKE_ORDER_BUTTON))), \
            "Авторизация не выполнена (кнопка заказа не отображена)"

    def test_login_from_account_button_success(self, driver):
        # Пытаемся открыть личный кабинет из хэдера БЕЗ АВТОРИЗАЦИИ
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         HeaderLocators.PROFILE_BUTTON))).click()

        # Прим.: поскольку здесь мы авторизируемся не с главной страницы, а проверяем специфический сценарий,
        # то оптимизировать код целесообразно не запуском фикстуры с авторизацией по-умолчанию (зачем?),
        # а в рамках POM в классе страницы LoginPage (в данном случае). Но мы это пока "не проходили"  :)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_EMAIL_ON_LOGIN).send_keys(Data.TEST_EMAIL)
        driver.find_element(By.XPATH, AuthPagesLocators.INPUT_PASSWORD).send_keys(Data.TEST_PASS)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH,
                                                                         AuthPagesLocators.LOG_IN))).click()

        assert WebDriverWait(driver, 3)\
            .until(ec.visibility_of_element_located((By.XPATH,
                                                    HomePageLocators.MAKE_ORDER_BUTTON))), \
            "Авторизация не выполнена (кнопка заказа не отображена)"





