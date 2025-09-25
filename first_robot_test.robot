*** Settings ***
Library    Browser

*** Variables ***
${LOGIN_URL}    https://dukeport201.t2qa.com/DUKEQA1/adm/users/auth.aspx?from=https://dukeport201.t2qa.com/DUKEQA1/adm/dev/impersonateUser.aspx
${USERNAME}     Kasey1
${PASSWORD}     Parking123!!!

*** Test Cases ***
T2 Login Test Using Robot Framework
    [Documentation]    Test login functionality using Robot Framework
    ...                REQUIRES: VPN connection for site access
    New Browser    chromium    headless=False    slowMo=500ms
    New Page       ${LOGIN_URL}
    
    Fill Text      id=ctl00_T2Main_txtLogin      ${USERNAME}
    Fill Text      id=ctl00_T2Main_txtPassword   ${PASSWORD}
    Click          id=ctl00_T2Main_cmdLogin
    
    Wait For Load State    networkidle
    Get Text       body    contains    Impersonate
    
    Close Browser

*** Keywords ***
Login To T2 System
    [Arguments]    ${username}    ${password}
    Fill Text      id=ctl00_T2Main_txtLogin      ${username}
    Fill Text      id=ctl00_T2Main_txtPassword   ${password}
    Click          id=ctl00_T2Main_cmdLogin