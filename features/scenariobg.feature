Feature: CMS Login
  Background: Common Steps
    Given I launch browser
    When I open application
    And Enter username "decaps" and password "123456"
    And Click on Login

  Scenario: Login to CMS Application
    Then User must login to the Dashboard page

  Scenario: Open Profile Page
    When Navigate to "decaps" Profile Page
    Then Profile Page should display

  Scenario: Log Out
    When Click on Log Out
    Then Login Page should display
