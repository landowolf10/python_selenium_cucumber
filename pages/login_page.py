import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.base_page import BasePage
from utils.constant_data import *
from locators.login_locators import *
from locators.dashboard_locators import *

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def navigate_to_sauce_lab(self):
        self.navigate_to(URL)

    def write_credentials(self, email, password):
        self.write_text((By.XPATH, userTextbox), email)
        self.write_text((By.XPATH, passwordTextbox), password)

    def click_login_button(self):
        self.click_element((By.XPATH, loginButton))

    def get_valid_login_elements(self):
        present_elements = {}
        
        try:
            present_elements["cart_icon"] = self.element_is_displayed((By.XPATH, cartIcon))
            present_elements["drop_down"] = self.element_is_displayed((By.XPATH, sortDropDown))
        except TimeoutException as e:
            present_elements["cart_icon"] = False
            present_elements["drop_down"] = False
            print(e)

        return present_elements

    def get_invalid_login_elements(self):
        present_elements = {
            "login_button": self.element_is_displayed((By.XPATH, loginButton)),
            "error_message": self.element_is_displayed((By.XPATH, errorMessage))
        }
        return present_elements

    def get_error_message_text(self):
        return self.get_element_text((By.XPATH, errorMessage))