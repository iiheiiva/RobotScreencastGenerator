*** Settings ***
Documentation    Another example test suite for screencast recording.
Resource    ../Resources/screencast.resource
Library    NarrationRecorder    ${SUITE NAME}     WITH NAME    Narrator
Library  SeleniumLibrary    run_on_failure=Nothing    # Disable screenshots when failure happens
Library  ScreenCapLibrary
Test Teardown    Close Browser


*** Variables ***
${BROWSER}          Chrome

*** Keywords ***


*** Test Cases ***
Google-haun tekeminen ${BROWSER}-selaimella
    Open Browser    http://www.google.com    ${BROWSER}
    Setup recording     # Resource keyword

    Highlight element    id=L2AGLb
    Add narration    Klikataan ensin huomioikkuna pois.

    Click Button    id=L2AGLb
    Add narration    Kirjoita haluamasi hakusana ja paina "enter".
    Input Text    name=q    Hello world!
    Stop recording     # Resource keyword

Bing-haun tekeminen
    Open Browser    https://www.bing.com/    ${BROWSER}
    Setup recording

    highlight element    id=sb_form

    Add narration    Kirjoita haluamasi hakusana ja paina "enter".
    Input Text    id=sb_form_q    Hello bing!
    Stop recording
