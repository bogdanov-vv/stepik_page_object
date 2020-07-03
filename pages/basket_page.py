from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def tree_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_TREE)
        button.click()

    def should_not_be_basket_items_visible(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Elements in basket is presented, but should not be"

    def should_be_basket_message_clear_visible(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
        "Element BASKET_MESSAGE not visible"