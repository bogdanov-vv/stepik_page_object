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

class ProductPageLocators():
    TITLE_ART = (By.CSS_SELECTOR, "div[class] h1") #Name article
    ADD_ART_BT = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']") #Add article in to basket
    ADD_ALERT_INNER = (By.CSS_SELECTOR, "[class='alertinner '] strong") #Alert success add article
    PRICE_BEFORE = (By.CSS_SELECTOR, "[class='price_color']") #Price before in basket
    PRICE_AFTER = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-info  fade in'] div strong") #Price after in basket
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']") #Success message add art in basket

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_TREE = (By.CSS_SELECTOR, "[class='basket-mini pull-right hidden-xs'] [class='btn btn-default']")
    BASKET_ITEMS = (By.CSS_SELECTOR, "[class='basket-items']")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "[id='content_inner'] p")

