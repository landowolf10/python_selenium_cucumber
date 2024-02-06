import sys, os
sys.path.append(os.path.join(os.getcwd(), '..'))
from pages.login_page import LoginPage
from robot.api.deco import keyword
from utils import set_up
import assertpy

login_page = None


@keyword(name="I type the credentials")
def type_credentials(user_name, password):
    global login_page
    login_page = LoginPage(set_up.get_browser)
    login_page.write_credentials(user_name, password)

@keyword(name='click the login button')
def press_login_button():
    login_page.click_login_button()

@keyword(name='verify that the user successfully logged in')
def verify_successful_login():
    assertpy.assert_that(login_page.get_valid_login_elements()['cart_icon']).is_true()
    assertpy.assert_that(login_page.get_valid_login_elements()['drop_down']).is_true()

"""@then('verify user login was not successful')
    def invalid_login(context):
        assertpy.assert_that(self.login_page.get_invalid_login_elements()['login_button']).is_true()
        assertpy.assert_that(self.login_page.get_invalid_login_elements()['error_message']).is_true()
        assertpy.assert_that(self.login_page.get_error_message_text()).is_equal_to("Epic sadface: Username and password do not match any user in this service")"""

