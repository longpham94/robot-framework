*** Settings ***

Library    Selenium2Library
Library    libEdit.Locator

Resource    config.txt
Resource    resource_1.robot

*** Test Case ***
[TC-001] - Multiple Browsers
    Open Browser1     Google
    # Open Browser2     Google
    Search Browser1    driver1    Python
    # Search Browser2    driver2    Java
