from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_be_promo_url(self):
        # реализуйте проверку на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "Don't open promo in page."

    def should_be_add_art_bt(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ART_BT), "Add art bt is not presented"


    def should_be_art_name(self):
        article = self.browser.find_element(*ProductPageLocators.TITLE_ART).text
        # print("ARTICLE:: ", article)
        return article

    def should_be_price_before_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BEFORE), "PRICE_BEFORE is not presented"
        price_b = self.browser.find_element(*ProductPageLocators.PRICE_BEFORE).text
        # print("PRICE BEFORE: ", price_b)
        return price_b

    def should_be_price_after_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_AFTER), "PRICE_AFTER is not presented"
        price_a = self.browser.find_element(*ProductPageLocators.PRICE_AFTER).text
        # print("PRICE AFTER: ", price_a)
        return price_a

    def check_price_in_basket(self):
        assert ProductPage.should_be_price_before_basket(self) == ProductPage.should_be_price_after_basket(self), "Price not correct!"

    def add_article_in_basket(self):
        add_art = self.browser.find_element(*ProductPageLocators.ADD_ART_BT)
        add_art.click()

    def should_be_alert_inner(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ALERT_INNER), "Not visible allert inner"

    def check_name_article_in_basket(self):
        alert = self.browser.find_element(*ProductPageLocators.ADD_ALERT_INNER).text
        # print("ALERT:: ", alert)
        assert ProductPage.should_be_art_name(self) == alert, "Article not in basket"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_disappered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is disappeared, but should not be"

    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"
