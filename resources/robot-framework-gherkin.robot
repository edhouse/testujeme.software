*** Settings ***
Documentation  Feature: Website Search Functionality
...  * As a website visitor
...  * I want to use the search function
...  * So that I can find content related to the searched text

Library  SeleniumLibrary
Suite Teardown  Close All Browsers

*** Test Cases ***
Scenario: Search for Robot Framework content
  Given I opened the edhouse.cz homepage in "Firefox"
  When I click on the search icon
  And I enter "Robot Framework" in the search field
  And I click the search icon again
  Then the search results should contain "Robot Framework"

*** Keywords ***
I opened the edhouse.cz homepage in "${browser}"
  Open Browser  https://www.edhouse.cz/  ${browser}
  Wait Until Page Contains Element  ${accept_cookies}
  Click Element  ${accept_cookies}
  Wait Until Page Does Not Contain Element  locator=${accept_cookies}

I click on the search icon
  Click Element  ${search_icon}

I enter "${search_string}" in the search field
  Input Text  ${search_input}  ${search_string}

I click the search icon again
  Click Element  ${search_button}

the search results should contain "${search_string}"
  Wait Until Page Contains   počet nalezených záznamů
  Page Should Contain  ${search_string}

***Variables***
${search_icon}  //*[@class='icon icon--search']
${search_input}  //*[@id="search"]
${search_button}  //*[@class="search__submit"]//*[@class='icon icon--search']
${accept_cookies}  //*[@id="cookie-policy"]//*[text()='Přijmout']