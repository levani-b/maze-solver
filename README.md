# Maze Solver

## Overview

This project implements a maze-solving algorithm using depth-first search. The program visualizes the solving process, showing how the algorithm explores different paths until it finds the solution or determines that no solution exists.

## Features

- Visual representation of the maze
- Animated display of the solving algorithm in action
- Depth-first search implementation for maze traversal
- Backtracking when reaching dead ends

## How It Works

The solver uses a recursive depth-first search approach:

1. Starting from the entrance (0,0)
2. Marks each visited cell
3. Explores each possible direction (up, down, left, right)
4. Backtracks when hitting dead ends
5. Continues until finding the exit or exhausting all possibilities
