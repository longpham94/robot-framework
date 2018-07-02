*** Keywords ***
Open Page    [Arguments]    ${URL}    ${browser}
    Open Browser    ${URL}    ${browser}
    ${d1} =    get_webdriver_instance
    Set Global Variable    ${d1}    ${d1}
    Log To Console    ${d1}

Login    [Arguments]    ${user}    ${pass}
    Input Text    xpath=//*[@type='email']    ${user}
    Press Key    xpath=//*[@type='email']    \\13
    Wait Until Element Is Visible    xpath=//*[@type='password']    20 Seconds
    Input Text    xpath=//*[@type='password']    ${pass}
    send_special_key    ${d1}    xpath    //*[@type='password']    ENTER

#Check Login    [Arguments]    ${URL}
#    Sleep    10 Seconds
#    ${current_URL} =    Get Location     
#    Run Keyword If  '${current_URL}'== '${URL}'  Log To Console  "Log in Success"    ELSE    Log To Console  "Log In Failed" 

Clean Up
    Close Browser
