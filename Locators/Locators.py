
from selenium.webdriver.common.by import By

class Locators:
    
    EMAIL = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    ERROR_MESSAGE = (By.XPATH, "//li[text()=': The password you entered for the username ']")
    SHOP_TAB = (By.XPATH, "//a[text()='Shop']")

    '''homepage'''
    CART_ICON = (By.XPATH, "//a[@title='View your shopping cart']")
    NO_OF_ITEMS_IN_CART_DISPLAYED = (By.XPATH, "//span[text()='2']")
    HEADER = (By.XPATH, "(//h4[@class='widgettitle'])[1]")
    ANDROID_QUICK_START_GUIDE = (By.XPATH, "//a[@href='/shop/?add-to-cart=169']")
    HTML5_FORMS = (By.XPATH, "//a[@href='/shop/?add-to-cart=181']")
    MY_ACCOUNT_TAB = (By.XPATH, "//a[text()='My Account']")
    # BURGER_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    '''cart page'''
    CART_PAGE_TITLE = (By.XPATH, "//th[text()='Product']")
    QTY = (By.XPATH, "(//input[@title='Qty'])[1]")
    ITEM_1 = (By.XPATH, "//a[text()='Android Quick Start Guide']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[@class='checkout-button button alt wc-forward']")

    '''CHECKOUT: YOUR INFORMATION'''
    CHECKOUT_YOUR_INFO = (By.XPATH, "//span[text()='Checkout: Your Information']")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    COMPANY_NAME = (By.ID, "postal-code")
    PLACE_ORDER_BUTTON = (By.ID, "continue")

    '''Checkout overview page'''
    CHECOUT_OVERVIEW_TITLE = (By.XPATH, "Checkout: Overview")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")

    '''checkout complete page'''
    CHECKOUT_COMPLETE_PAGE = (By.XPATH, "//*[text()='Checkout: Complete!']")
    THANK_YOU_FOR_ORDER = (By.XPATH, "//*[text()='THANK YOU FOR YOUR ORDER']")
    BACK_TO_HOME_PAGE = (By.XPATH, "//button[text()='Back Home']")
