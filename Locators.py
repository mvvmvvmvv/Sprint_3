class Locators:
    # URL's
    HOME_PAGE = "https://stellarburgers.nomoreparties.site/"
    LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"
    REGISTER_PAGE = "https://stellarburgers.nomoreparties.site/register"
    RESTORE_PASSWORD_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"

    # XPATHs
    # Home Page
    CONSTRUCTOR_HEADER = ".//section/h1[text()='Соберите бургер']"
    LOGIN_BUTTON = ".//button[text()='Войти в аккаунт']"
    BUNS = ".//span[text()='Булки']"
    BUNS_ENABLED = \
        ".//main/section[1]/div[1]/div[1][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    SAUCE = ".//span[text()='Соусы']"
    SAUCE_ENABLED =\
        ".//main/section[1]/div[1]/div[2][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    FILLING = ".//span[text()='Начинки']"
    FILLING_ENABLED = \
        ".//main/section[1]/div[1]/div[3][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    MAKE_ORDER_BUTTON = ".//button[text()='Оформить заказ']"

    # Header
    PROFILE_BUTTON = ".//p[text()='Личный Кабинет']"
    LOGO_LINK = ".//div[@class='AppHeader_header__logo__2D0X2']"
    CONSTRUCTOR = ".//p[text()='Конструктор']"

    # Login, register, restore password
    ENTER_HEADER = ".//div/h2[text()='Вход']"
    INPUT_NAME = ".//input[@name='name']"
    INPUT_EMAIL = ".//fieldset[2]/div/div/input"
    INPUT_EMAIL_ON_LOGIN = ".//input[@name='name']"
    INPUT_PASSWORD = ".//input[@name='Пароль']"
    LOG_IN = ".//button[text()='Войти']"
    REGISTER_LINK = ".//a[text()='Зарегистрироваться']"
    RESTORE_PASSWORD_LINK = ".//a[text()='Восстановить пароль']"
    REGISTER_BUTTON = ".//button[text()='Зарегистрироваться']"
    INVALID_PASSWORD_WARNING = ".//p[text()='Некорректный пароль']"
    LOGIN_PAGE_LINK = ".//a[text()='Войти']"

    # User profile
    PROFILE_DESCRIPTION_TEXT = ".//p[@class='Account_text__fZAIn text text_type_main-default']"
    LOG_OUT_BUTTON = ".//button[text()='Выход']"




