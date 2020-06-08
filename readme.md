# Gess

###Motivation

My final project for CS162 was an implementation of the board game [Gess](https://www.chessvariants.com/crossover.dir/gess.html) in Python, playable from the command line. After completion, I decided to make the game playable via a GUI interface which I've implemented using [PyGame](https://www.pygame.org/).

###What You'll Need

* Full GUI version: 
The game requires Python3.6+ and PyGame to run the GUI version. 

* Command line version:
Without PyGame, the game can still be played from the command line with any version of Python3.

**To install PyGame:**

```
python3 -m pip install pygame
```

If you don't have admin rights, or would like to only install PyGame for your current user profile, try adding the *user* flag, like so:

```
python3 -m pip install pygame --user
```

If you are still having trouble installing PyGame, please visit the PyGame Wiki's [Getting Started](https://www.pygame.org/wiki/GettingStarted) page.

###In Action

![Image of game being played](images/in_action_sm.png)

###How To Play

The game rules are available [here](https://www.chessvariants.com/crossover.dir/gess.html#:~:text=There%20are%20two%20players%2C%20black,belonging%20to%20the%20opposing%20player.).

###Work Left To Do

This game is a work in progress. Features I intend to add in the future include, by estimated time commitment:

**Short**

- [X] Add an underlay showing which tile was chosen
- [ ] Add an underlay outlining the "piece" that was chosen
- [ ] Allow the player to forfeit via the GUI (currently only possible from the command line)
- [X] A "Game Over" screen announcing the winner
- [ ] A "Play Again" option after a game has been won
- [ ] The option to change the board background image

**Medium**
- [ ] Add an options drop-down / tooltip
- [ ] The option to change the teams' colors and piece outline, choosing from either a list of preset colors, but also allowing for the choice of any RGB color
- [ ] Allow the game to be downloaded as an executable instead of requiring the download of PyGame
- [ ] Add audio

**Long**
- [ ] Add a title / menu / options screen
- [ ] Add an overlay showing all legal moves from the starting position chosen (this one may require me to rewrite much of the game)
- [ ] Add a tutorial

**Very Long**
- [ ] Rewrite game. The game as it exists