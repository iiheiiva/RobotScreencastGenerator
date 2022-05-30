*** Settings ***
Documentation    An example test suite for screencast recording.
Resource    ../Resources/screencast.resource
Library    NarrationRecorder    ${SUITE NAME}     WITH NAME    Narrator
Library  SeleniumLibrary    run_on_failure=Nothing    # Disable screenshots when failure happens
Library  ScreenCapLibrary
Library    CryptoLibrary    variable_decryption=True    key_path=\CryptoLibraryKeys
Test Teardown    Close Browser


*** Variables ***
${BROWSER}          Chrome
${encoded_pwd}    crypt:lZM8c1sm81ZWbZCo71cPAgoN1Kad493uF+XYjXg4lnEdmrd8ttPVby6c6xs2YWJgt2RFYL0SDC1K1d/ybhtGqxn1Ahc=


*** Keywords ***


*** Test Cases ***
Sovellusasetusten muuttaminen
    [Documentation]    Keywords "Setup recording", "Add narration" and "Stop recording"
    ...                are used for screencast recording.
    Open Browser    https://butane.test.roaddata.jalonne.fi/    ${BROWSER}
    Setup recording

    Add narration    Verkkosovelluksen käyttäminen vaatii kirjautumistiedot.

    Input Text    id=username   iiro.iivanainen@jalonne.fi
    Input Password    id=password    ${encoded_pwd}
    click button        id=login-button
    Wait Until Page Contains Element    id=settings-page-button     timeout= 15 seconds

    Add narration    Vasemmasta valikosta löytyy sovelluksen asetukset.

    click button    id=settings-page-button
    click button    id=app-profiles-admin-page-button
    Click Element    //ons-icon[@class="ons-icon zmdi zmdi-plus"]

    Add narration    Lisätään sovellusprofiiliin halutut tiedot.

    Input Text    //input[@name="name"]    TestProfile
    Select From List By Value    //select[@name="deviceMode"]    supervised
    Select From List By Value    //select[@name="imageSize"]    high
    Click Element    //input[@name="pictureRate"]
    Click Element    //input[@name="diskQuota"]
    Click Element    xpath=(//div[@class="center list-item__center"])[10]
    Click Element    //div[@class="switch__touch"]
    Stop recording
