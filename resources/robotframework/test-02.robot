*** Settings ***
Library   RPA.Browser.Selenium
Library    DateTime

*** Test Cases ***
Test Web Calculator
    # Open Browser 
    [Setup]    Open Browser    browser=chrome
    Go To    https://testsheepnz.github.io/BasicCalculator.html
    
    # Test Steps
    Input Text    id:number1Field    99
    Input Text    name:number2    1
    Select From List by Value    id:selectOperationDropdown    0
    Click Button    id:calculateButton
    
    # Verification
    ${result}=    Get Calculator result
    Should Be Equal    ${result}    100

    # Take screenshot
    ${timestamp}=      Get current date    result_format=%Y-%m-%d_%H-%M-%S
    Screenshot    //form[@id="calcForm"]    calculator_web_${timestamp}.jpg

    # Teardown - perform actions after the test
    [Teardown]   Close Browser

*** Keywords ***
Get Calculator result
    ${value}=   Get Value    id=numberAnswerField
    [Return]    ${value}