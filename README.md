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



8-Puzzle Solver Documentation (BFS Approach)
============================================
Introduction

The 8-puzzle solver using the Breadth-First Search (BFS) algorithm finds the solution for the 8-puzzle problem. In this problem, a 3x3 grid contains eight numbered tiles and one empty space. The objective is to arrange the tiles in numerical order by sliding them into the empty space.
Functions
is_goal_state(state)

    Purpose: Checks if the given state represents the goal state where all tiles are in numerical order.
    Input: The current state of the puzzle.
    Output: Returns True if the state is the goal state; otherwise, returns False.

possible_moves(state)

    Purpose: Determines possible moves (tiles adjacent to the empty space) for the given state.
    Input: The current state of the puzzle.
    Output: Returns a list of possible moves represented as offsets (row_offset, col_offset).

apply_move(state, move)

    Purpose: Applies the given move to the state and returns the new state.
    Inputs: The current state of the puzzle and the move to make.
    Output: Returns the new state of the puzzle after applying the move.

find_empty_space(state)

    Purpose: Finds the coordinates of the empty space (0) in the given state.
    Input: The current state of the puzzle.
    Output: Returns the coordinates of the empty space as (row, col).

solve_8_puzzle_bfs(initial_state)

    Purpose: Solves the 8-puzzle problem using the Breadth-First Search (BFS) algorithm.
    Input: The initial state of the puzzle.
    Output: Returns the solution path, the number of moves taken, and the time taken to solve the puzzle.

print_puzzle(state)

    Purpose: Prints the current state of the puzzle.
    Input: The current state of the puzzle.
    Output: Prints the puzzle grid.

Example
=========

python

import time

# Function implementations here...

# Define initial state
initial_state = ((1, 2, 3),
                 (4, 0, 5),
                 (6, 7, 8))

# Print initial state
print("Initial State (Example):")
print_puzzle(initial_state)
print()

# Solve the puzzle using BFS
bfs_solution, bfs_num_moves, bfs_time_taken = solve_8_puzzle_bfs(initial_state)

if bfs_solution:
    print("\nBFS Solution:")
    for move in bfs_solution:
        initial_state = apply_move(initial_state, move)
    print_puzzle(initial_state)
    print("\nBFS Number of Moves:", bfs_num_moves)
    print("BFS Time Taken:", round(bfs_time_taken, 2), "seconds")
else:
    print("\nBFS could not find a solution.")

Output:
=======

yaml

Initial State (Example):
1 2 3
4 0 5
6 7 8

BFS Solution:
1 2 3
4 5 6
7 8 0

BFS Number of Moves: 14
BFS Time Taken: 0.06 seconds

Conclusion
===========

The BFS-based solver efficiently solves the 8-puzzle problem by exploring all possible moves level by level until finding the solution.






8-Puzzle Solver Documentation
=============================
Introduction

The 8-puzzle solver is a program designed to find the solution to the classic 8-puzzle problem. In this problem, there is a 3x3 grid with eight numbered tiles and one empty space. The objective is to rearrange the tiles into numerical order by sliding them into the empty space.
Main Points
Depth-First Search (DFS)
========================

    Approach: DFS explores as far as possible along each branch before backtracking.
    Pros:
        Memory-efficient as it doesn't store all explored nodes.
        Can find a solution with fewer moves in certain cases.
    Cons:
        May take longer to find a solution for complex puzzles.
        Not guaranteed to find the shortest solution path.

Breadth-First Search (BFS)
============================

    Approach: BFS explores all neighbor nodes at the present depth before moving on to the nodes at the next depth level.
    Pros:
        Guarantees to find the shortest solution path.
        Ideal for finding the optimal solution.
    Cons:
        Requires more memory to store all explored nodes.
        Can be slower than DFS for puzzles with deep solution paths.

Functions
is_goal_state(state)

    Description: Checks if the given state is the goal state where all tiles are in numerical order.
    Input: The current state of the puzzle.
    Output: Returns True if the state is the goal state; otherwise, returns False.

possible_moves(state)

    Description: Determines possible moves (tiles adjacent to the empty space) for the given state.
    Input: The current state of the puzzle.
    Output: Returns a list of possible moves represented as offsets (row_offset, col_offset).

apply_move(state, move)

    Description: Applies the given move to the state and returns the new state.
    Inputs: The current state of the puzzle and the move to make.
    Output: Returns the new state of the puzzle after applying the move.

find_empty_space(state)

    Description: Finds the coordinates of the empty space (0) in the given state.
    Input: The current state of the puzzle.
    Output: Returns the coordinates of the empty space as (row, col).

solve_8_puzzle_dfs(initial_state)

    Description: Solves the 8-puzzle problem using the Depth-First Search (DFS) algorithm.
    Input: The initial state of the puzzle.
    Output: Returns the solution path, the number of moves taken, and the time taken to solve the puzzle.

solve_8_puzzle_bfs(initial_state)

    Description: Solves the 8-puzzle problem using the Breadth-First Search (BFS) algorithm.
    Input: The initial state of the puzzle.
    Output: Returns the solution path, the number of moves taken, and the time taken to solve the puzzle.

print_puzzle(state)

    Description: Prints the current state of the puzzle.
    Input: The current state of the puzzle.
    Output: Prints the puzzle grid.

Example Usage

python

import time

# Function implementations here...

# Define initial state
initial_state = ((1, 2, 3),
                 (4, 0, 5),
                 (6, 7, 8))

# Print initial state
print("Initial State (Example):")
print_puzzle(initial_state)
print()

# Solve the puzzle using DFS
dfs_solution, dfs_num_moves, dfs_time_taken = solve_8_puzzle_dfs(initial_state)

if dfs_solution:
    print("\nDFS Solution:")
    for move in dfs_solution:
        initial_state = apply_move(initial_state, move)
    print_puzzle(initial_state)
    print("\nDFS Number of Moves:", dfs_num_moves)
    print("DFS Time Taken:", round(dfs_time_taken, 2), "seconds")
else:
    print("\nDFS could not find a solution.")

# Solve the puzzle using BFS
bfs_solution, bfs_num_moves, bfs_time_taken = solve_8_puzzle_bfs(initial_state)

if bfs_solution:
    print("\nBFS Solution:")
    for move in bfs_solution:
        initial_state = apply_move(initial_state, move)
    print_puzzle(initial_state)
    print("\nBFS Number of Moves:", bfs_num_moves)
    print("BFS Time Taken:", round(bfs_time_taken, 2), "seconds")
else:
    print("\nBFS could not find a solution.")

Output:

Initial State (Example):
1 2 3
4 0 5
6 7 8

DFS Solution:
1 2 3
4 5 6
7 8 0

DFS Number of Moves: 19992
DFS Time Taken: 5.71 seconds

BFS Solution:
1 2 3
4 5 6
7 8 0

BFS Number of Moves: 14
BFS Time Taken: 0.06 seconds

Conclusion

The 8-puzzle solver provides efficient solutions using both DFS and BFS approaches. DFS may find solutions with fewer moves, while BFS guarantees to find the shortest solution path.
