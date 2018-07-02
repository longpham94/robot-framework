from selenium import webdriver
import logging
import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
from Selenium2Library import Selenium2Library
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.webdriver.support.ui as ui
from robot.api.deco import keyword
from Selenium2Library import Selenium2Library
from keyDict import Dict

class Locator:
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    # special keys codes
    # dictKeyword = {'ENTER': u'\ue007', 'CONTROL': u'\ue009'}

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


    # def create_driver_session(self, session_id, executor_url):
    #     # Save the original function, so we can revert our patch
    #     org_command_execute = RemoteWebDriver.execute
    #     def new_command_execute(self, command, params=None):
    #         if command == "newSession":
    #             # Mock the response
    #             return {'success': 0, 'value': None, 'sessionId': session_id}
    #         else:
    #             return org_command_execute(self, command, params)

    #     # Patch the function before creating the driver object
    #     RemoteWebDriver.execute = new_command_execute

    #     new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    #     new_driver.session_id = session_id

    #     # Replace the patched function with original function
    #     RemoteWebDriver.execute = org_command_execute
    #     return new_driver

    # Click element
    def click_element(self, driver, keyword, name):
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
    
    def right_click(self, driver, xpath):
        actionChains = ActionChains(driver)
        element=driver.find_element_by_xpath(str(xpath))
        actionChains.context_click(element).perform()

# class ExtendedSeleniumLibrary(Selenium2Library):
#     @keyword("Right Click Element")
#     def right_click(self, xpath):
#         driver = self._current_browser()
#         actionChains = ActionChains(driver)
#         element=driver.find_element_by_xpath(str(xpath))
#         actionChains.context_click(element).perform()
