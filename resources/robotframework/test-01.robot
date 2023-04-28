*** Settings ***
Library    OperatingSystem
Library    RPA.Windows
Library    DateTime

*** Tasks ***
Test Windows Calculator
    # Run and set control window
    [Setup]    Windows Run   calc.exe
    Control Window    name:Calculator
    
    # Steps
    Click    type:Button and name:"Nine"
    Click    id:num9Button
    Click    type:Button and name:"Plus"
    Send Keys    keys=1
    Click    type:Button and name:"Equals"

    # Verification
    ${result}=    Get Calculator result
    Should Be Equal    "${result}"    "Display is 100"

    # Take screenshot
    ${timestamp}=      Get current date    result_format=%Y-%m-%d_%H-%M-%S
    Screenshot    type:type:WindowControl and name:"Calculator"    calculator_${timestamp}.jpg
   
    [Teardown]   Close Current Window

*** Keywords ***
Get Calculator result
    ${value}=    Get Attribute    id:CalculatorResults    Name
    [Return]    ${value}