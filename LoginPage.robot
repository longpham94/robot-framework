*** Keywords ***
Login    ${user}    ${pass}
    Input Text    xpath=//*[@type='email']    ${user}
    Press Key    xpath=//*[@type='email']    \\13
    Wait Until Element Is Visible    xpath=//*[@type='password']    20 Seconds
    Input Text    xpath=//*[@type='password']    ${pass}
    send_special_key    ${d1}    xpath    //*[@type='password']    ENTER

# Login With Invalid Information
#     Input Text    xpath=//*[@type='email']    ${invalid_user}
#     Press Key    xpath=//*[@type='email']    \\13
#     Wait Until Element Is Visible    xpath=//*[@type='password']    20 Seconds
#     Input Text    xpath=//*[@type='password']    ${in/lvalid_pass}
#     send_special_key    ${d1}    xpath    //*[@type='password']    ENTER