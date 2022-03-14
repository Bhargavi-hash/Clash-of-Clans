# Game specifications:
### Village :
There will be a map of n * m dimensions representing your village level. Each village must have the
following properties

* Spawning points:
  * There should be three predefined spawning points around the village.
  * Each spawning point will be controlled by a different key. 
  * Pressing the key of a certain spawning point will cause a troop to be deployed there.
* Town Hall:
  * The Town Hall is the central building of your village.
  * There is only one town hall per village.
  * Size: 4x3 tiles
* Huts:
  * There should be at least five huts in your village
  * Size of the hut can be defined by you.
* Walls:
  * There should be a sufficient number of walls in your village to protect your town hall from troops.
  * Size: 1x1 tiles
* Cannon:
  * There should be at least two cannons in your village.
  * Size can be defined by you.
  * The cannon will have a range and damage value (can be defined by you). The range (must be greater than 5 tiles) would define the area till which it can attack and the damage value should be a number telling the amount of damage it yields to a single troop in a second.
  * At a given point, the cannon can only target a single troop.
  * Each building will have a certain amount of hitpoints (basically health) and the remaining
    hitpoints of the building would be denoted by its colour.
  * The hitpoints of the building should be split into at least three ranges, each with a
    different colour.
  * For example: Green: 50% to 100% hitpoints, Yellow: 20%-50% hitpoints, Red: 0%-20% hitpoints.
  * A building with 0 hit points is considered destroyed and should not be displayed on the screen or targeted by troops.