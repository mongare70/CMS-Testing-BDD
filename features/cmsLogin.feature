Feature: CMS Login

  Scenario: Login to CMS with valid parameters
    Given I launch Chrome Browser
    Then I open CMS Homepage
    And Enter username "decaps" and password "123456"
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to CMS with multiple parameters
    Given I launch Chrome Browser
    Then I open CMS Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | oya      | 123456   |
      | decaps   | 123456   |
      | neymar   | 123456   |

