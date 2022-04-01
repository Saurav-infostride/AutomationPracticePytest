import sys, os
import time
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.support.ui import Select

class BillingDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_enter_your_info(self):
        self.do_send_keys(Locators.FIRST_NAME, TestData.FIRST_NAME)
        self.do_send_keys(Locators.LAST_NAME, TestData.LAST_NAME)
        self.do_send_keys(Locators.COMPANY_NAME, TestData.COMPANY_NAME)
        self.do_send_keys(Locators.PHONE, TestData.PHONE)
        self.do_send_keys(Locators.ADDRESS, TestData.ADDRESS)
        time.sleep(5)
        self.do_send_keys(Locators.TOWN_CITY, TestData.TOWN_CITY)
        time.sleep(5)
        self.do_click(Locators.STATE_COUNTY)
        time.sleep(5)
        Select = Select(Locators.STATE_COUNTY)
        time.sleep(5)
        Select.select_by_visible_text('Lakshadeep')
        time.sleep(5)
        self.do_send_keys(Locators.STATE_COUNTY, TestData.STATE_COUNTY)
        time.sleep(5)
        self.do_send_keys(Locators.POSTAL_ZIP_CODE, TestData.POSTAL_ZIP_CODE)
        time.sleep(5)
        self.do_click(Locators.PAYPAL_EXPRESS_CHECKOUT)
        time.sleep(5)
        self.do_click(Locators.PLACE_ORDER_BUTTON)