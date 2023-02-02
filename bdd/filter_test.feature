# Created by krzys at 23.01.2023
Feature: Filters test
  # Enter feature description here

  Scenario: Category
    When Select category and subcategory
    Then Products appear

  Scenario: Brands
    When Select brand
    Then Products appear