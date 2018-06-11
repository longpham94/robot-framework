* Settings *
Library    Selenium2Library


* Variables *
${URL}            https://www.google.com
${browser}        Chrome
${keyword}        Python

* Test Cases *
[TC-001]-Launch the browser and search for keyword 'Python' and click on the first result
    Launch Browser
    Search Keyword
    Click First Result
    Clean Up

* Keywords *
Launch Browser
    Open Browser    ${URL}  ${browser}
    Maximize Browser Window

Search Keyword
    Input Text    name=q    ${keyword}
    Press Key     name=q    \\13

Click First Result
    Wait Until Element Is Visible    //*[@id="resultStats"]/following::h3[1]/a    10 Seconds
    Click Element    xpath=//*[@id="resultStats"]/following::h3[1]/a
    Sleep    10 Seconds

Clean Up
   Close Browser