# Lab - Rock Paper Scissors

## Task

You are going to create a small app where given the option of two hand gestures from a list of 3, one is chosen over the other.  The 3 options are:

- Rock
- Paper
- Scissors

The way in which one task is preferred over another is:

- Rock wins against scissors.
- Scissors win against paper.
- Paper wins against rock.

You should write tasks for all classes and functions you create. Make sure that you create a separate file for each class and a separate test file for each class/module.


### MVP


Create a file `Game`. `Game`s has a function that takes in a `player_1` and a `player_2` objects and returns the preferred task based on the `gesture` of the `Player`:

Create a class `Player`. `Player` has a `name`, and a `gesture`.

Use TDD, creating as many tests as you think you will need.

### Extension

Let's bring in another two gestures, "Lizard" and "Spock", so we are now dealing with five different gestures. You will still be choosing between two gestures so in addition to what has been done already:

- Scissors cut Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitate Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

There are fifteen possible pairings of the five gestures. Each gesture beats two of the other gestures and is beaten by the remaining two. In a tie, the process is repeated until a winner is found. The original rules (rock beats scissors, scissors beats paper, paper beats rock) remain the same in the extended version of the game.

https://www.youtube.com/watch?v=x5Q6-wMx-K8 


### Files and Directories

  - In your working directory, create two directories, one for your classes and one for your tests
  - Remember to create an empty `__init__.py` file in the directories created above
  - create a `run_tests.py` file in your working directory. Use this file to run your tests.


**REMEMBER** to commit to git regularly
