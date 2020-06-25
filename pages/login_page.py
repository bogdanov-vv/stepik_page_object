from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Don't open login page."
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.IN_MAIL), "In Mail is not presented"
        assert self.is_element_present(*LoginPageLocators.IN_PW), "In password is not presented"
        assert self.is_element_present(*LoginPageLocators.IN_BT), "In button is not presented"
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_MAIL), "Reg Mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PW), "Reg password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PW_AGAIN), "Reg password2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BT), "Reg button is not presented"
        # assert True