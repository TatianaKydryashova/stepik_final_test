from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_correct_add_name_book(self):
        name_book_in_main = self.browser.find_element(*MainPageLocators.NAME_BOOK_IN_MAIN_PAGE)
        name_book_text = name_book_in_main.text
        name_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET)
        name_book_text_basket = name_book_in_basket.text
        assert name_book_text == name_book_text_basket, "Error in book title"

    def should_be_correct_price_book(self):
        price_book_in_main = self.browser.find_element(*MainPageLocators.PRISE_BOOK_IN_MAIN_PAGE)
        price_book_text = price_book_in_main.text
        price_book_in_basket = self.browser.find_element(*ProductPageLocators.PRISE_BOOK_IN_MAIN_BASKET)
        price_book_text_basket = price_book_in_basket.text
        assert price_book_text == price_book_text_basket, "Error in price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"




