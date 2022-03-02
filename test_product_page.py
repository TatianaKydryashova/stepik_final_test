import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link, 10)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_add_name_book()
    page.should_be_correct_price_book()
    #time.sleep(200)
