Feature: Search a product

  Scenario: Search a winter coat
    Given I am on the shopping website
    When I search for "Winter coat"
    Then I should get the search results for winter coat