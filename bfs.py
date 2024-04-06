import time
from collections import deque

def is_goal_state(state):
    # Check if the state is the goal state (all tiles in numerical order)
    return state == ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def possible_moves(state):
    # Find possible moves (tiles adjacent to the empty space)
    moves = []
    empty_row, empty_col = find_empty_space(state)

    # Check upward move
    if empty_row > 0:
        moves.append((-1, 0))  # Move empty space up

    # Check downward move
    if empty_row < 2:
        moves.append((1, 0))  # Move empty space down

    # Check left move
    if empty_col > 0:
        moves.append((0, -1))  # Move empty space left

    # Check right move
    if empty_col < 2:
        moves.append((0, 1))  # Move empty space right

    return moves

def apply_move(state, move):
    # Apply the move to the state and return the new state
    empty_row, empty_col = find_empty_space(state)
    row_offset, col_offset = move
    state_list = list(state)
    new_state = [list(row) for row in state_list]  # Make a copy of the state

    # Swap the empty space with the adjacent tile
    new_state[empty_row][empty_col] = new_state[empty_row + row_offset][empty_col + col_offset]
    new_state[empty_row + row_offset][empty_col + col_offset] = 0  # Empty space

    return tuple(tuple(row) for row in new_state)

def find_empty_space(state):
    # Find the coordinates of the empty space (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def solve_8_puzzle_bfs(initial_state):
    start_time = time.time()  # Record start time
    if is_goal_state(initial_state):
        return [], 0, 0  # Already in the goal state

    visited = set()
    queue = deque([(initial_state, [])])  # (state, path)

    while queue:
        state, path = queue.popleft()
        visited.add(state)

        if is_goal_state(state):
            end_time = time.time()  # Record end time
            elapsed_time = end_time - start_time
            return path, len(path), elapsed_time  # Return the sequence of moves, the number of moves taken, and time elapsed

        for move in possible_moves(state):
            new_state = apply_move(state, move)
            if new_state not in visited:
                queue.append((new_state, path + [move]))

    return None, None, None  # No solution found

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))

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