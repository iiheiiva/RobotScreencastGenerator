*** Settings ***
Documentation    Contains keywords for screencast recording and logging narration.
Library    NarrationRecorder    ${SUITE NAME}     WITH NAME    Narrator
Library  SeleniumLibrary    run_on_failure=Nothing    # Disable screenshots when failure happens
Library  ScreenCapLibrary


*** Keywords ***
Setup recording
    [Documentation]    Sets a proper pace for selenium, prepares the browser and begins recording narrations.
    ...                Also has a sleep time so it doesn't need to be included in post production.
    [Arguments]    ${speed}=0.2 seconds     ${pause}=3
    Set Selenium Speed    ${speed}
    Maximize Browser Window
    Start Video Recording    alias=none    name=${SUITE NAME}_${TEST NAME}	    fps=None    size_percentage=1.0    embed=True    embed_width=100px    monitor=1
    Narrator.initialize test narration    ${TEST NAME}
    Sleep    ${pause}
Stop recording
    [Documentation]    Stops recording and adds the narrations to `.json` file
    ...                Also has a sleep time so it doesn't need to be included in post production.
    [Arguments]    ${pause}=4
    Sleep   ${pause}
    Narrator.append to json
    Stop Video Recording    alias=None
Add narration
    [Documentation]     Logs the narration message and also waits for an appropriate time.
    [Arguments]    ${message}
    narrator.add narration    ${message}
    Sleep    3

