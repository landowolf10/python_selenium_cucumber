*** Settings ***
Documentation  This test suite contains app tests for the login page

Library  ../steps/common_steps.py
Library  ../steps/login_steps.py

Suite Teardown  Close browser session

*** Variables ***
${user_name}  standard_user
${password}  secret_sauce
${browser}  Chrome

*** Test Cases ***
Scenario: Validate successful login to Sauce Lab demo app
    [Tags]  Login
    Given I navigate to SauceLab demo page  ${browser}
    When I type the credentials  ${user_name}  ${password}
    And click the login button
    Then verify that the user successfully logged in