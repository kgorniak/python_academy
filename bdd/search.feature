# Created by krzys at 23.01.2023
Feature: Search
  # Enter feature description here

  Scenario: Check price
    Given I'm logged in
      |name   |password |
      |krzys  |secret   |
    When I add product to cart
    Then I see price 123