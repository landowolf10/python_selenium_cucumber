from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from utils.constant_data import *
import os

driver = None
wait = None
driver_instance_exists = False
driver_instance = None
browser = ""
service = None

def get_driver(browser_name):
    global driver
    wait = None
    #browser = None
    global driver_instance_exists
    global driver_instance
    global browser
    global service


    if driver_instance_exists:
        driver = driver_instance
    else:
        driver = create_driver(browser_name)

    driver_instance_exists = True
    driver_instance = driver
    browser = browser_name

    print("Browser: ", browser)
    return driver

def create_driver(browser_name):
    os_name = os.name
    chrome_driver_path = ""
    print("OS: ", os_name)

    if browser_name.lower() == "chrome":
        if "Windows" in os_name:
            chrome_driver_path = chromeDriverPathWindows
        elif "Linux" in os_name:
            chrome_driver_path = chromeDriverPathLinux

        service = chrome_driver_path

        chrome_options = ChromeOptions()
        #chrome_options.add_argument("--remote-allow-origins=*")
        driver = webdriver.Chrome(service=service)
    elif browser_name.lower() == "firefox":
        firefox_driver_path = ""

        if "Windows" in os_name:
            firefox_driver_path = geckoDriverPathWindows
        elif "Linux" in os_name:
            firefox_driver_path = geckoDriverPathLinux

        #firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(firefox_driver_path)

    #chrome_options = ChromeOptions()
    #chrome_options.add_argument("--remote-allow-origins=*")

    

    #driver = webdriver.Chrome()

    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    return driver

def get_browser():
    return browser

def quit_driver():
    global driver_instance_exists, driver_instance

    if driver_instance_exists:
        current_driver = driver_instance
        current_driver.quit()

    driver_instance_exists = False
    driver_instance = None