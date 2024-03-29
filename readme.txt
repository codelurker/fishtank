Contents
~~~~~~~~~
	1. Introduction
	2. License
	3. Dependencies
	4. Controls
	5. Fish Emotions
	6. Known Bugs


1. Introduction
~~~~~~~~~~~~~~~~
fishtank - simulation of a fish tank

The fishtank is a home to two kinds of fishes. The smaller ones are just fooling
around and trying to find something to eat. When they eat some food a new fish
is born. Since they are so small and weak they tend to gather in a fish school.
The bigger ones are predators and therefore are trying to hunt down the smaller
ones. 
You can add food to the tank or even new fishes - so try to create
a balanced ecosystem.

2. License
~~~~~~~~~~~
fishtank is released under the MIT license, see license.txt

3. Dependencies
~~~~~~~~~~~~~~~~
Python 2.6 (or later)

4. Controls
~~~~~~~~~~~~
q - quit
c - add a cyan fish
f - add some food for the fish
p - add a predator fish

5. Fish Emotions
~~~~~~~~~~~~~~~~~
Small fish:
    0< - the fish feels good and is fooling around
    X< - the fish just ate something good
    &< - the fish is scared to death while running away from a predator

Predator:
    0=< - the predator is looking for something tasty
    $=< - the predator is in a hunting rush
    X=< - the predator just devoured some poor little fish
    ^=< - the predator is going to sleep as there is nothing to eat

6. Known Bugs
~~~~~~~~~~~~~~
  - Shrinking the terminal while fishtank is running will crash the application

