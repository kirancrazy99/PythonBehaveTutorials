Feature: Fight or flight(Natuarl Language,tutorial02)
  In order to increse Ninja survival rate,
  As a Ninja commander
  I want my Ninjas to decide whether to take an opponant
  based on their skill levels

  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
    When attacked by a samurai
    Then the ninja should engage the opponent

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
    When attached by Chuck Norris
    Then the ninja should run for life