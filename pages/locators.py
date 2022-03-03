from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    USER_LOGIN = (By.NAME, "registration-email")
    USER_PASSWORD1 = (By.NAME, "registration-password1")
    USER_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class MainPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK_IN_MAIN_PAGE = (By.TAG_NAME, "h1")
    PRISE_BOOK_IN_MAIN_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info")
    PRISE_BOOK_IN_MAIN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info .alertinner strong")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success .alertinner strong")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_TEXT = (By.CSS_SELECTOR, ".content a")