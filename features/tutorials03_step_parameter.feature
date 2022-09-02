Feature: Step Parameters
  Scenario: Blenders
    Given I put "Apples" in a blender
    When I switch on blender
    Then it should turn into "Apple juice"