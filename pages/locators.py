from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK_IN_MAIN_PAGE = (By.TAG_NAME, "h1")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success .alertinner strong")
    PRISE_BOOK_IN_MAIN_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRISE_BOOK_IN_MAIN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info .alertinner strong")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
