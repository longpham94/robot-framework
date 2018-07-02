*** Keywords ***
Login    ${user}    ${pass}
    Input Text    xpath=//*[@type='email']    ${user}
    Press Key    xpath=//*[@type='email']    \\13
    Wait Until Element Is Visible    xpath=//*[@type='password']    20 Seconds
    Right Click    ${d1}    xpath    //*[@type='password']    xpath        
    Input Text    xpath=//*[@type='password']    ${pass}
    send_special_key    ${d1}    xpath    //*[@type='password']    ENTER