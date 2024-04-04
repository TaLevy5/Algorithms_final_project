import time
from puzzle import random_board, print_board
from graph import Graph
from bfs import bfs
from astar import astar, zero_heuristic, manhattan_distance

def test_algorithm(graph, start, goal, algorithm, heuristic=None):
    start_time = time.perf_counter()
    initial_node_count = len(graph.vertices)  # Record initial number of nodes

    if heuristic:
        path = algorithm(graph, start, goal, heuristic)
    else:
        path = algorithm(graph, start, goal)

    end_time = time.perf_counter()
    nodes_created = len(graph.vertices) - initial_node_count  # Calculate nodes created during this run

    return {
        'runtime': end_time - start_time,
        'path_length': len(path) if path else 0,
        'nodes_created': nodes_created
    }


def run_tests(puzzle_size, num_puzzles, num_moves):
    results = {'BFS': [], 'A* Zero': [], 'A* Manhattan': []}
    puzzle_type = 15 if puzzle_size == 4 else 24

    for _ in range(num_puzzles):
        start_list = random_board(puzzle_type, num_moves)
        start = tuple(start_list)  # Convert the board to a tuple
        goal = tuple(range(1, puzzle_size ** 2)) + (0,)
        graph = Graph()

        print("\nTesting on board:")
        print_board(start, puzzle_size)

        for name, algorithm, heuristic in [
            ('BFS', bfs, None),
            ('A* Zero', astar, zero_heuristic),
            ('A* Manhattan', astar, manhattan_distance)
        ]:
            graph.vertices = {}  # Reset the graph for each algorithm
            result = test_algorithm(graph, start, goal, algorithm, heuristic)
            results[name].append(result)
            print(f"{name} - Time: {result['runtime']:.4f} seconds, Path Length: {result['path_length']}, Nodes Created: {result['nodes_created']}")

    return results



def analyze_results(results):
    print("\nAverage Results:")
    for algo, data in results.items():
        avg_runtime = sum(d['runtime'] for d in data) / len(data)
        avg_path_length = sum(d['path_length'] for d in data) / len(data)
        avg_nodes_created = sum(d['nodes_created'] for d in data) / len(data)
        print(f"{algo} - Average Time: {avg_runtime:.4f} seconds, Average Path Length: {avg_path_length}, Average Nodes Created: {avg_nodes_created}")

def main():
    num_tests = 5
    num_moves = 10
    print("Testing Puzzle 15")
    puzzle_15_results = run_tests(4, num_tests, num_moves)
    analyze_results(puzzle_15_results)

    print("\nTesting Puzzle 24")
    puzzle_24_results = run_tests(5, num_tests, num_moves)
    analyze_results(puzzle_24_results)

    # Further testing with 50 random boards for each puzzle
    # Uncomment the below lines to run the extensive tests
    # print("\nExtensive Testing Puzzle 15")
    # extensive_15_results = run_tests(4, 50, num_moves)
    # analyze_results(extensive_15_results)

    # print("\nExtensive Testing Puzzle 24")
    # extensive_24_results = run_tests(5, 50, num_moves)
    # analyze_results(extensive_24_results)

if __name__ == "__main__":
    main()
