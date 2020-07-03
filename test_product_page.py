from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_promo_url()
    product_page.should_be_add_art_bt()
    product_page.should_be_price_before_basket()
    product_page.add_article_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_name_article_in_basket()
    product_page.check_price_in_basket()

