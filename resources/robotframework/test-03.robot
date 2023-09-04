*** Settings ***
Library    OperatingSystem
Library    FlaUILibrary
Library    DateTime

*** Tasks ***
Test Windows Calculator
    # Setup - perform actions before the test
    [Setup]       Launch Application    calc.exe
    ${app}=    Attach Application By Name    calc.exe
    
    # Test steps
    Click    //Group[@AutomationId="NumberPad"]//Button[@Name="Nine"]
    Click    //Group[@AutomationId="NumberPad"]//Button[@Name="Nine"]
    Click    //Button[@AutomationId="plusButton"]
    Click    //Button[@AutomationId="num1Button"]
    Click    //Button[@AutomationId="equalButton"]

    # Verification
    ${result}=    Get Calculator result
    Log    "${result}"
    Should Be Equal    "${result}"    "Display is 100"

    # Take screenshot
    Take Screenshot
   
    # Teardown - perform actions after the test
    [Teardown]   Close Application    ${app}

*** Keywords ***
Get Calculator result
    ${value}=    Get Name From Element    //Text[@AutomationId="CalculatorResults"]
    [Return]    ${value}