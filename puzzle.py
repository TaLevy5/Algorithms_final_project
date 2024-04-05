def manual_input(puzzle_size):
    if puzzle_size not in [4,5]:
        raise ValueError("Invalid puzzle size. Only 4 (for 15-puzzle) or 5 (for 24-puzzle) are allowed.")
    
    num_tiles = puzzle_size * puzzle_size
    print(f"Enter the numbers for the {puzzle_size}x{puzzle_size} puzzle, from 0 to {num_tiles - 1}, row by row:")

    board = []
    while len(board) < num_tiles:
        try:
            row = input(f"Enter row {len(board)//puzzle_size + 1} of {puzzle_size}: ").split()
            if len(row) != puzzle_size:
                raise ValueError("Incorrect number of elements in the row")
            
            row_numbers = [int(num) for num in row]
            if any(num < 0 or num >= num_tiles for num in row_numbers):
                raise ValueError("Numbers must be within the puzzle range")
            
            board.extend(row_numbers)

            if len(set(board)) != len(board):
                raise ValueError("Duplicate numbers are not allowed")

        except ValueError as e:
            print(f"Error: {e}")
            # If there's an error, reset the board to start over
            board = []

    return board

import random

def random_board(puzzle_type, num_moves):
    if puzzle_type == 15:
        size = 4
    elif puzzle_type == 24:
        size = 5
    else:
        raise ValueError("Invalid puzzle type")

    # Start with a solved board with '0' at the end
    board = list(range(1, size * size)) + [0]
    
    # Shuffle the board by making 'num_moves' random moves
    for _ in range(num_moves):
        empty_index = board.index(0)
        neighbors = []
        if empty_index % size > 0:  # Can move the empty space to the right
            neighbors.append(empty_index - 1)
        if empty_index % size < size - 1:  # Can move the empty space to the left
            neighbors.append(empty_index + 1)
        if empty_index // size > 0:  # Can move the empty space down
            neighbors.append(empty_index - size)
        if empty_index // size < size - 1:  # Can move the empty space up
            neighbors.append(empty_index + size)
        
        # Choose a random neighbor and swap
        to_swap = random.choice(neighbors)
        board[empty_index], board[to_swap] = board[to_swap], board[empty_index]

    return board

def print_board(board, size):
    for i in range(size):
        row = board[i*size:(i+1)*size]
        print(' '.join(map(str, row)))
