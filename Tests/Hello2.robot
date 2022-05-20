*** Settings ***
Documentation    Beginning projcect for tutorial creation.
Library    NarrationRecorder    ${SUITE NAME}     WITH NAME    Narrator
Library  SeleniumLibrary    run_on_failure=Nothing    # Disable screenshots when failure happens
Library  ScreenCapLibrary
Test Teardown    Close Browser


*** Variables ***
${BROWSER}          Chrome

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
Google-haun tekeminen ${BROWSER}-selaimella
    Open Browser    http://www.google.com    ${BROWSER}
    Setup recording
    Narrator.add narration    Klikataan ensin huomio ikkuna pois.
    Click Button    id=L2AGLb
    Sleep    1s
    Narrator.add narration    Kirjoita haluamasi hakusana ja paina "enter".
    Input Text    name=q    Toinen kerta toden sanoo
    Sleep    1s
    Stop recording

Bing-haun tekeminen
    Open Browser    https://www.bing.com/    ${BROWSER}
    Setup recording
    Sleep    1s
    Narrator.add narration    Kirjoita haluamasi hakusana ja paina "enter".
    Input Text    id=sb_form_q    Bingiä voi käyttää vaikka säälistä
    Sleep    1s
    Stop recording


