*** Settings ***
Library    Selenium2Library
Library    Lib

Resource   resource.robot
Resource   config.txt

# *** Variables ***
# ${URL}            http://mail.google.com
# ${browser}        Chrome
# ${user}           lttp941010
# ${valid_pass}     longpham1
# ${invalid_pass}   12345678
# ${EXPECTED_URL}   https://mail.google.com/mail/u/0/#inbox
# ${EXPECTED_URL_1}  https://accounts.google.com/signin
# ${d1}

*** Test Cases ***
[TC-001]-Login Gmail with valid information
    Open Page    ${URL2}    ${browser}
    Login    ${user}    ${valid_pass}
    Check Login    ${EXPECTED_URL}
    Clean Up

[TC-002]-Login Gmail with invalid information
    Open Page    ${URL2}    ${browser}
    Login    ${user}    ${invalid_pass}
    Check Login    ${EXPECTED_URL}
    Clean Up


    
     



