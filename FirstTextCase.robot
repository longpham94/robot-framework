*** Settings ***
Library    Selenium2Library

*** Variables ***
${APP}            selenium
${URL}            https://www.google.com
${BROWSER}        CHROME
${EXPECTED_URL}   https://www.seleniumhq.org/

*** Test Cases ***
[TC-001]-Launching the browser and search and launch the 'selenium' Application on Google.com
    Launch Browser
    Search Application On Google
    Launch Application
    Verify URL
    Clean Up

*** Keywords ***
Launch Browser
    Open Browser            ${URL}   ${BROWSER}   None  http://192.168.35.49:4444/wd/hub
Search Application On Google
    Input Text    id=lst-ib    ${APP}
    Press Key     name=q       \\13
Launch Application
    Wait Until Element Is Visible    link=Selenium - Web Browser Automation      20 Seconds
    Click Element     link=Selenium - Web Browser Automation
Verify URL
    Location Should Be    ${EXPECTED_URL}
Clean Up
    Close Browser