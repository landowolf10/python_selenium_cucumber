import sys, os
sys.path.append(os.path.join(os.getcwd(), '..'))

from pages.login_page import LoginPage
from utils import set_up
from robot.api.deco import keyword

login_page = None

@keyword(name="I navigate to SauceLab demo page")
def navigate(browser):
    login_page = LoginPage(browser)
    login_page.navigate_to_sauce_lab()

@keyword(name="Close browser session")
def closeBrowserSession():
    set_up.quit_driver()

"""@after_step
def screenshot(context, step):
    take_screen_shot(context.scenario)"""