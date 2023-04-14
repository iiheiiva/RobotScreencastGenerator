*** Settings ***
Documentation    Another example test suite for screencast recording.
Resource    ../Resources/screencast.resource
Library    NarrationRecorder    ${SUITE NAME}     WITH NAME    Narrator
Library  SeleniumLibrary    run_on_failure=Nothing
Library  ScreenCapLibrary
Test Teardown    Close Browser


*** Variables ***
${BROWSER}          Chrome
${CHROME_OPTIONS} =
...    add_experimental_option("excludeSwitches", ["enable-automation"]);
...    add_experimental_option("prefs", {"credentials_enable_service" : False, "password_manager_enabled" : False});
...    add_argument("--start-maximized")

*** Keywords ***

*** Test Cases ***
Bing-haun tekeminen
    Open Browser    https://www.bing.com/    ${BROWSER}    options=${CHROME_OPTIONS}
    Setup recording

    Input Text    id=sb_form_q    Hello bing!
    Add narration    Kirjoita haluamasi hakusana ja paina hakupainiketta.

    highlight element    id=search_icon    2
    Click Element    id=search_icon

    Stop recording

Google-haun tekeminen
    Open Browser    http://www.google.com    ${BROWSER}    options=${CHROME_OPTIONS}
    Setup recording     # Resource keyword

    Highlight element    id=L2AGLb
    Add narration    Klikataan ensin huomioikkuna pois.

    Click Button    id=L2AGLb
    Input Text    name=q    Hello world!
    Add narration    Kirjoita haluamasi hakusana ja paina hakupainiketta.

    Highlight element    name=btnK    2
    Click Button    name=btnK

    Stop recording     # Resource keyword


