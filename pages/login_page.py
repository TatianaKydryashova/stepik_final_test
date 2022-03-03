from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        user_login = self.browser.find_element(*BasePageLocators.USER_LOGIN)
        user_login.send_keys(email)
        user_password1 = self.browser.find_element(*BasePageLocators.USER_PASSWORD1)
        user_password1.send_keys(password)
        user_password2 = self.browser.find_element(*BasePageLocators.USER_PASSWORD2)
        user_password2.send_keys(password)
        button_registration = self.browser.find_element(*BasePageLocators.REGISTRATION_SUBMIT)
        button_registration.click()