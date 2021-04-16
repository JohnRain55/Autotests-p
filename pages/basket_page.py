from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "'login' not in current url"

    def should_be_basket_name(self):
        assert self.is_element_present(*BasketPageLocators.PAGE_HEADER),  "Basket name is not presented"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "'Basket empty' message is not presented"

    def should_not_be_basket_formset(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Basket formset is presented, but should not be"
