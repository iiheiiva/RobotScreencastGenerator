*** Settings ***
Documentation    Beginning projcect for tutorial creation.
Library    NarrationRecorder    ${SUITE NAME}     WITH NAME    Narrator
Library  SeleniumLibrary    run_on_failure=Nothing    # Disable screenshots when failure happens
Library  ScreenCapLibrary
Library    CryptoLibrary    variable_decryption=True    key_path=\CryptoLibraryKeys
Test Teardown    Close Browser


*** Variables ***
${BROWSER}          Chrome
${encoded_pwd}    crypt:lZM8c1sm81ZWbZCo71cPAgoN1Kad493uF+XYjXg4lnEdmrd8ttPVby6c6xs2YWJgt2RFYL0SDC1K1d/ybhtGqxn1Ahc=


*** Keywords ***
Setup recording
    Set Selenium Speed    0.2 seconds
    Maximize Browser Window
    Narrator.initialize test narration    ${TEST NAME}
    Start Video Recording    alias=none    name=${SUITE NAME}_${TEST NAME}	    fps=None    size_percentage=1.0    embed=True    embed_width=100px    monitor=1
Stop recording
    Stop Video Recording    alias=None
    Narrator.append to json


*** Test Cases ***
Sovellusasetusten muuttaminen
    [Documentation]    Testidokumentointi do not delete.
    Open Browser    https://butane.test.roaddata.jalonne.fi/    ${BROWSER}
    Setup recording
    Narrator.add_narration    Verkkosovelluksen käyttäminen vaatii kirjautumistiedot.
    Input Text    id=username   iiro.iivanainen@jalonne.fi
    Input Password    id=password    ${encoded_pwd}
    click button        id=login-button
    Sleep    10
    Narrator.add narration    Vasemmasta valikosta löytyy sovelluksen asetukset.
    click button    id=settings-page-button
    click button    id=app-profiles-admin-page-button
    Sleep    3
    Click Element    //ons-icon[@class="ons-icon zmdi zmdi-plus"]
    Sleep    3
    Narrator.add narration    Lisätään sovellusprofiiliin halutut tiedot
    Input Text    //input[@name="name"]    TestProfile
    Select From List By Value    //select[@name="deviceMode"]    supervised
    Select From List By Value    //select[@name="imageSize"]    high
    Click Element    //input[@name="pictureRate"]
    Click Element    //input[@name="diskQuota"]
    Click Element    xpath=(//div[@class="center list-item__center"])[10]
    Click Element    //div[@class="switch__touch"]
    Sleep    1
    Stop recording
