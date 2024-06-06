
# Puzzle Solver Project

## Overview
This project aims to solve the 15-puzzle and 24-puzzle games using different search algorithms. The algorithms implemented are:
- Breadth-First Search (BFS)
- A* Search with various heuristics:
  - Zero Heuristic
  - Manhattan Distance
  - Custom Heuristic

## Project Structure
The project is organized into the following files:
- `main.py`: The main entry point of the application. It handles user input for creating the initial board state, selecting the solving algorithm, and displaying the solution.
- `graph.py`: Contains the implementation of the Graph class, which is used to represent the puzzle states and transitions.
- `puzzle.py`: Provides functions for manual input and random generation of puzzle board states, as well as a function to print the board.
- `bfs.py`: Implements the Breadth-First Search algorithm.
- `astar.py`: Implements the A* Search algorithm with different heuristics.

## Requirements
- Python 3.x
- No external libraries are required.

## How to Use
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/puzzle-solver.git
    cd puzzle-solver
    ```

2. Run the main program:
    ```sh
    python main.py
    ```

3. Follow the on-screen prompts to:
   - Choose the method to create the initial board state (manual input or random generation).
   - Select the solving algorithm (BFS, A* with Zero Heuristic, A* with Manhattan Distance, A* with Custom Heuristic).

## Example
```sh
Choose the method to create the initial board state:
1. Manual Input
2. Random Generation
Enter 1 or 2: 1
Enter the puzzle size (4 for 15-puzzle, 5 for 24-puzzle): 4
Enter the numbers for the board row by row, separated by spaces (use 0 for the blank tile):
1 2 3 4
5 6 7 8
9 10 11 12
13 14 0 15

The board state you generated is:
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 0 15 

Choose the algorithm:
1. BFS
2. A* with Zero Heuristic
3. A* with Manhattan Distance
4. A* with Custom Heuristic
Enter 1, 2, 3, or 4: 3
Solving...

Start Board:
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 0 15 

Solution found in X steps:

Step number 1:
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 0 14 15 

Step number 2:
1 2 3 4 
5 6 7 8 
9 10 11 12 
0 13 14 15 

...
```

## Algorithms
### BFS (Breadth-First Search)
BFS explores all the neighboring nodes at the present depth level before moving on to nodes at the next depth level.

### A* Search
A* Search uses heuristics to guide its search. The project includes three heuristics:
- **Zero Heuristic**: A trivial heuristic that always returns zero, effectively making A* equivalent to Dijkstra's algorithm.
- **Manhattan Distance**: A common heuristic for grid-based puzzles, calculating the sum of the distances of the tiles from their goal positions.
- **Custom Heuristic**: A user-defined heuristic that can be tailored to specific characteristics of the puzzle.

## Conclusion
This project demonstrates the implementation of various search algorithms to solve sliding puzzle games, showcasing their differences in performance and efficiency.

## Author
- Tal Levy
