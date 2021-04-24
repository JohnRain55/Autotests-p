# Message for the reviewer
Hi, thanks for checking my project!) I wish you good and tea!
\
Due to the difference in package versions, sometimes errors like:\
from pages.product_page import ProductPage\
E ImportError: attempted relative import with no known parent package\
If so, please add dots before pages. in lines:\
from .pages.product_page import ProductPage\
from .pages.basket_page import BasketPage\
from .pages.login_page import LoginPage\
\
\
Привет, спасибо, что проверяешь мой проект!) Желаю добра и чая!
\
Из-за разницы в версиях пакетов, иногда могут падать ошибки типа:\
from pages.product_page import ProductPage\
E   ImportError: attempted relative import with no known parent package\
Если это так, пожалуйста, добавь точки  перед pages. в строках :\
from .pages.product_page import ProductPage\
from .pages.basket_page import BasketPage\
from .pages.login_page import LoginPage
