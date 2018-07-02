*** Settings ***
Library    Selenium2Library
Library    Lib

Resource   ../resource.robot
Resource   ../config.txt


*** Test Cases ***
[TC-001]-Login Gmail with valid information
    Open Page    ${URL}    ${browser}
    Login    ${user}    ${valid_pass}
#    Check Login    ${EXPECTED_URL}
    Clean Up

[TC-002]-Login Gmail with invalid information
    Open Page    ${URL}    ${browser}
    Login    ${user}    ${invalid_pass}
#    Check Login    ${EXPECTED_URL_1}
    Clean Up


    
     



