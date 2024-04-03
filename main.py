from graph import Graph
from puzzle import manual_input, print_board, random_board
from bfs import bfs 

def main():
    graph = Graph()  # Create a graph instance
    start_state = None
    puzzle_size = None

    while True:
        try:
            choice = input("Choose the method to create the initial board state:\n1. Manual Input\n2. Random Generation\nEnter 1 or 2: ")
            
            if choice == '1':
                puzzle_size = int(input("Enter the puzzle size (4 for 15-puzzle, 5 for 24-puzzle): "))
                if puzzle_size not in [4, 5]:
                    raise ValueError("Invalid puzzle size. Only 4 (for 15-puzzle) or 5 (for 24-puzzle) are allowed.")
                start_state = tuple(manual_input(puzzle_size))
                print("The board state you entered is:")
            elif choice == '2':
                puzzle_type = int(input("Enter the puzzle type (15 for 15-puzzle, 24 for 24-puzzle): "))
                num_moves = int(input("Enter the number of moves to shuffle the board: "))
                start_state = tuple(random_board(puzzle_type, num_moves))
                puzzle_size = 4 if puzzle_type == 15 else 5
                print("The randomly generated board state is:")
            else:
                print("Invalid choice")
                continue

            print_board(start_state, puzzle_size)

            # Define the goal state based on puzzle size
            goal_state = tuple(range(1, puzzle_size**2)) + (0,)
            print("Solving...")

            # Use BFS to solve the puzzle
            path = bfs(graph, start_state, goal_state)
            if path:
                print(f"Solution found in {len(path)} steps:")
                for step, state in enumerate(path, start=1):
                    print(f"Step number {step}:")
                    print_board(state, puzzle_size)
                    print()  # Add an empty line for visual separation between steps
            else:
                print("No solution found.")
            
            break  # Exit the loop after a successful operation

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
