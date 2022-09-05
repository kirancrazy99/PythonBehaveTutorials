Feature: scenario outline(tutorial04)
  Scenario Outline: use Blender
    Given I put "<thing>" in a blender
    When I switch on Blender
    Then it should turn into "<other_thing>"
    Examples:Ambhians
      | thing | other_thing |
      |Red Tree Frog|Mush    |
      |apples | apple juice  |
    Examples: Consumer Electronics
      | thing | other_thing |
      |iphone  |toxic wastage|
      |Galaxy Nexus|toxic wastage|