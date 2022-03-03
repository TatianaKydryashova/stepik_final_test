from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket is not empty, but should be"

    def should_be_correct_text(self):
        url = self.browser.current_url
        basket = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
        href_url = basket.get_attribute("href")
        assert href_url in url, \
            "Message is not presented, but should be"
