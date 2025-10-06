# logic.py
# Logic module for the 2048 game.
# To be imported in 2048.py (main game file)

import random

# --- Core Game Setup Functions ---

def start_game():
    """
    Initialize the 4x4 game board.
    Adds two initial tiles (2s or 4s) and displays commands.
    """
    mat = [[0] * 4 for _ in range(4)]

    print("Commands are as follows:")
    print("  'W' or 'w' : Move Up")
    print("  'S' or 's' : Move Down")
    print("  'A' or 'a' : Move Left")
    print("  'D' or 'd' : Move Right")
    print("-" * 25)

    # Start with two tiles, as is standard in 2048
    add_new_tile(mat)
    add_new_tile(mat)

    return mat

def add_new_tile(mat):
    """
    Add a new tile (2 or 4) to a random empty cell.
    90% chance for 2, 10% chance for 4.
    """
    empty_cells = [(r, c) for r in range(4) for c in range(4) if mat[r][c] == 0]
    if not empty_cells:
        return # Grid is full

    r, c = random.choice(empty_cells)
    
    # New tile is 4 (10% chance) or 2 (90% chance)
    mat[r][c] = 4 if random.random() < 0.1 else 2

def get_current_state(mat):
    """
    Return the current state: 'WON', 'GAME NOT OVER', or 'LOST'.
    """
    # Check for 'WON' (2048 is present)
    for i in range(4):
        if 2048 in mat[i]:
            return 'WON'

    # Check for 'GAME NOT OVER' (Empty cells or possible merges)
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
            
            # Check for horizontal merges (only need to check up to column 2)
            if j < 3 and mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
            
            # Check for vertical merges (only need to check up to row 2)
            if i < 3 and mat[i][j] == mat[i + 1][j]:
                return 'GAME NOT OVER'

    # No 2048, no empty cells, and no possible merges
    return 'LOST'

# --- Matrix Manipulation Utilities ---

def transpose(mat):
    """Transpose the matrix (convert rows to columns)."""
    # Uses list comprehension for a clean and efficient transpose
    return [list(row) for row in zip(*mat)]

def reverse(mat):
    """Reverse each row (used for 'right' move logic)."""
    return [row[::-1] for row in mat]

# --- Core Movement Functions (Left/Combine) ---

def compress(mat):
    """Slide all non-zero numbers to the left (remove gaps)."""
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True # A tile moved from its original position
                pos += 1

    return new_mat, changed

def merge(mat):
    """
    Merge identical, adjacent numbers to the left.
    Only merges the first pair in a row (e.g., [2, 2, 4, 4] -> [4, 0, 8, 0]).
    """
    changed = False
    for i in range(4):
        for j in range(3):
            # Check for non-zero equal neighbors
            if mat[i][j] != 0 and mat[i][j] == mat[i][j + 1]:
                mat[i][j] *= 2
                mat[i][j + 1] = 0 # Empty the right cell
                changed = True
    return mat, changed

def move_left(grid):
    """Execute the core left move: compress, merge, then compress again."""
    # 1. Compress (remove gaps)
    new_grid, changed1 = compress(grid)
    # 2. Merge (combine identical tiles)
    new_grid, changed2 = merge(new_grid)
    # 3. Compress again (remove gaps created by merge)
    new_grid, _ = compress(new_grid) # changed flag from this compress isn't needed

    return new_grid, changed1 or changed2

# --- Directional Move Functions ---

def move_right(grid):
    """Execute a right move using the left move logic."""
    # Right = Reverse -> Left Move -> Re-reverse
    reversed_grid = reverse(grid)
    new_grid, changed = move_left(reversed_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    """Execute an upward move using the left move logic."""
    # Up = Transpose -> Left Move -> Re-transpose
    transposed_grid = transpose(grid)
    new_grid, changed = move_left(transposed_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    """Execute a downward move using the right move logic on a transposed grid."""
    # Down = Transpose -> Right Move -> Re-transpose
    transposed_grid = transpose(grid)
    # We can reuse move_right on the transposed grid for "down" movement
    new_grid, changed = move_right(transposed_grid) 
    new_grid = transpose(new_grid)
    return new_grid, changed