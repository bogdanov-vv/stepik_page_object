from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    IN_MAIL = (By.CSS_SELECTOR, "#id_login-username")
    IN_PW = (By.CSS_SELECTOR, "#id_login-password")
    IN_RESET_LINK = (By.CSS_SELECTOR, "")
    IN_BT = (By.CSS_SELECTOR, "button[name='login_submit']")
    REG_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PW = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PW_AGAIN = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BT = (By.CSS_SELECTOR, "button[name='registration_submit']")