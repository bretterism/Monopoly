# Monopoly
Python implementation of the board game Monopoly

## Purpose
This is an implementation where the computer plays against itself. Each player has a number of play styles that are either conservative in gameplay or aggressive. The idea is to have the computer play many different games of Monopoly and record the results of each game. From there, we should be able to determine what the best style of gameplay is in any situation.

## Current Status
This is a major work-in-progress. Most of the core rules of Monopoly have been implemented. As far as the players go, there are no play styles developed yet. Each player plays at 100% aggression and will buy up any property they land on.

Currently, the players don't know how to trade with each other, so when the game is run, almost nobody can buy all the properties of the same color and place houses or hotels on their property. Each player end up getting more money from passing GO than from the other players, and the game runs forever.

## How to run
It's simple! Just run main.py. When the player settings have been built out, there will be some arguments added to the command-line.
