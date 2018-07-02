*** Keywords ***
Open Browser1   [Arguments]    ${Link}
    # ${d1} =    create_remote    ${URL}    ${remoteHost}    ${browser}.
    Open Browser    ${URL}    ${browser}
    Maximize Browser Window
    ${d1} =    Get webdriver instance
    # ${d1} =    create_driver    ${URL}    ${browser}
    Set Global Variable    ${d1}    ${d1}
    Log To Console    ${d1}

Search Browser1    [Arguments]    ${driver}    ${keyword}
    Log To Console    CHECK ${d1}
    # Input Text    name=q    Python
    send_keys    ${d1}    name    q    ${keyword}
    send_special_key    ${d1}    name    q    ENTER
    Page Should Contain Image    xpath=//*[contains(@title, 'https://www.datacamp.com/courses/intro-to-python-for-data-science')]    None    INFO
    Sleep    10s   
    tearDown    ${d1}

Open Browser2    [Arguments]    ${Link}
    # ${d2} =    create_remote    ${URL}    ${remoteHost}    ${browser}
    ${d2} =    create_driver    ${URL}    ${browser}
    Set Global Variable    ${d2}    ${d2}
    Log To Console    ${d2}

Search Browser2    [Arguments]    ${driver}    ${keyword}
    Log To Console    CHECK ${d2}
    send_keys    ${d2}    name    q    ${keyword}
    send_special_key    ${d2}    name    q    ENTER
    Sleep    10s
    tearDown    ${d2}