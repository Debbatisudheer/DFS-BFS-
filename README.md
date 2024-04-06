DFS 8-Puzzle Solver Documentation
=================================
Introduction

The 8-puzzle is a classic puzzle where you have a 3x3 grid with eight numbered tiles and one empty space. The goal is to arrange the tiles in ascending order by sliding them into the empty space. This documentation explains how to solve the 8-puzzle using a Python program.
Functions
is_goal_state(state)

    What it does: Checks if the puzzle is solved (all tiles in order).
    Inputs: The current state of the puzzle.
    Output: True if the puzzle is solved, False otherwise.

possible_moves(state)

    What it does: Finds possible moves (tiles adjacent to the empty space).
    Inputs: The current state of the puzzle.
    Output: A list of possible moves (up, down, left, right).

apply_move(state, move)

    What it does: Moves a tile into the empty space.
    Inputs: The current state of the puzzle and the move to make.
    Output: The new state of the puzzle after the move.

find_empty_space(state)

    What it does: Finds the empty space (0) in the puzzle.
    Inputs: The current state of the puzzle.
    Output: The coordinates of the empty space.

solve_8_puzzle(initial_state)

    What it does: Solves the 8-puzzle using a depth-first search.
    Inputs: The initial state of the puzzle.
    Output: The solution path, number of moves, and time taken.

print_puzzle(state)

    What it does: Prints the current state of the puzzle.
    Inputs: The current state of the puzzle.
    Output: Prints the puzzle grid.

Observations

    The solver may take a long time for complex puzzles.
    Different initial states can affect the solver's performance.

Example Usage
=============

python

import time

# Functions here...

# Define initial state
initial_state = ((1, 2, 3),
                 (4, 0, 5),
                 (6, 7, 8))

# Print initial state
print("Initial State:")
print_puzzle(initial_state)
print()

# Solve the puzzle
solution, num_moves, time_taken = solve_8_puzzle(initial_state)

if solution:
    print("\nSolution:")
    for move in solution:
        initial_state = apply_move(initial_state, move)
    print_puzzle(initial_state)
    print("\nNumber of Moves:", num_moves)
    print("Time Taken:", round(time_taken, 2), "seconds")
else:
    print("\nNo solution found.")

Output:
=======
Initial State:
1 2 3
4 0 5
6 7 8

Solution:
1 2 3
4 5 6
7 8 0

Number of Moves: 19992
Time Taken: 5.71 seconds

Conclusion
==========

This solver helps solve the 8-puzzle problem by finding the best moves to arrange the tiles in order.
