from utils import set_up
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    chrome_driver = None
    action = None

    def __init__(self, browser):
        self.chrome_driver = set_up.get_driver(browser)
        self.action = ActionChains(self.chrome_driver)

    def get_element_by(self, element_locator):
        #self.set_up.until(EC.visibility_of_element_located(element_locator))
        return WebDriverWait(self.chrome_driver, 10).until(EC.visibility_of_element_located(element_locator))

    def get_all_elements_by(self, element_locator):
        return self.chrome_driver.find_elements(*element_locator)

    def navigate_to(self, url):
        self.chrome_driver.get(url)

    def go_to_link_text(self, link_text):
        self.chrome_driver.find_element(By.LINK_TEXT, link_text).click()

    def click_element(self, element_locator):
        self.get_element_by(element_locator).click()

    def click_element_from_list(self, element):
        element.click()

    def write_text(self, element_locator, text):
        element = self.get_element_by(element_locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, element_locator):
        return self.get_element_by(element_locator).text

    def select_from_drop_down_by_value(self, element_locator, value_to_select):
        dropdown = Select(self.get_element_by(element_locator))
        dropdown.select_by_value(value_to_select)

    def select_from_drop_down_by_index(self, element_locator, value_to_select):
        dropdown = Select(self.get_element_by(element_locator))
        dropdown.select_by_index(value_to_select)

    def select_from_drop_down_by_text(self, element_locator, value_to_select):
        dropdown = Select(self.get_element_by(element_locator))
        dropdown.select_by_visible_text(value_to_select)

    def hover_over_element(self, element_locator):
        element = self.get_element_by(element_locator)
        self.action.move_to_element(element).perform()

    def double_click(self, element_locator):
        element = self.get_element_by(element_locator)
        self.action.double_click(element).perform()

    def right_click(self, element_locator):
        element = self.get_element_by(element_locator)
        self.action.context_click(element).perform()

    def get_value_from_table(self, element_locator, row, column):
        cell = f"{element_locator}/table/tbody/tr[{row}]/td[{column}]"
        print("Cell locator: ", cell)
        return self.get_element_by((By.XPATH, cell)).text

    def set_value_on_table(self, element_locator, row, column, value):
        cell = f"{element_locator}/table/tbody/tr[{row}]/td[{column}]"
        self.get_element_by((By.XPATH, cell)).send_keys(value)

    def switch_to_iframe(self, iframe_index):
        self.chrome_driver.switch_to.frame(iframe_index)

    def switch_to_parent_frame(self):
        self.chrome_driver.switch_to.parent_frame()

    def dismiss_alert(self):
        self.chrome_driver.switch_to.alert.dismiss()

    def wait_until_element_located(self, locator_type, max_wait_sec):
        wait = WebDriverWait(self.chrome_driver, max_wait_sec)
        wait.until(EC.visibility_of_element_located(locator_type))

    def element_is_displayed(self, locator_type):
        return self.get_element_by(locator_type).is_displayed()

    def element_is_selected(self, locator_type):
        return self.get_element_by(locator_type).is_selected()

    def element_is_enabled(self, locator_type):
        return self.get_element_by(locator_type).is_enabled()