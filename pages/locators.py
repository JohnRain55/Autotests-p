from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[value=\"Add to basket\"]")
    BOOK_NAME = (By.CSS_SELECTOR, ".breadcrumb > li[class=active]")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    COST_OF_THE_BOOK = (By.CSS_SELECTOR, "#content_inner .price_color")
    COST_OF_THE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
