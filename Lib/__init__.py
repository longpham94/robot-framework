import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
from Selenium2Library import Selenium2Library
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from robot.api.deco import keyword
from Selenium2Library import Selenium2Library
from robot.libraries.BuiltIn import BuiltIn

from keyDict import Dict

__version__ = '1.0'

ROBOT_LIBRARY_VERSION = __version__

class Lib():
    def __init__(self):
        pass
    
    def create_selector(self, driver):
        dictElement = {'name': driver.find_element_by_name, 
                       'xpath': driver.find_element_by_xpath,
                       'id': driver.find_element_by_id,
                       'css': driver.find_element_by_css_selector,
                       'tagname': driver.find_element_by_tag_name}
        return dictElement
    
    # Create Session
    def create_driver(self, url, browser='chrome'):
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser.lower() == 'ie':
            driver = webdriver.Ie() 
        driver.get(url)
        driver.maximize_window()
        self.driver = driver
        return driver

    # Click element
    def click_on_element(self, driver, keyword, name):
        dictSelector = self.create_selector(driver)
        dictSelector[keyword](name).click()
        return

    # Send keys to web element
    def send_keys(self, driver, keyword, name, key):
        dictSelector = self.create_selector(driver)    
        dictSelector[keyword](name).send_keys(key)
        return

    # Press key ("keyboard" library)
    def press_key_new(self, driver, key):
        driver.maximize_window()
        keyboard.send(key)
        return

    # Intergrate Selenium Library and User-defined library
    def get_webdriver_instance(self):
        se2lib = BuiltIn().get_library_instance('Selenium2Library')
        return se2lib._current_browser()

    # Run on a remote host
    def create_remote(self, url, host, browser='chrome'):
        if browser.lower() == 'chrome':
            driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=DesiredCapabilities.CHROME)
        elif browser.lower() == 'firefox':
            driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=DesiredCapabilities.FIREFOX)
        elif browser.lower() == 'ie':
            driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        driver.get(url)
        driver.maximize_window()
        self.driver = driver
        return driver
    
    # Tear down session
    def tearDown(self, driver):
        driver.quit()

    # Send special keys
    def send_special_key(self, driver, keyword, name, key):
        dictSelector = self.create_selector(driver)
        dictSelector[keyword](name).send_keys(Dict.dictKeyword[key])
        return driver
    
    # Screen Shot
    def screenShot(self, driver, file):
        driver.save_screenshot(file+'.png')

    # Right_Click on a element
    def right_click(self, driver, xpath):
        actionChains = ActionChains(driver)
        element=driver.find_element_by_xpath(str(xpath))
        actionChains.context_click(element).perform()