from collections import deque
from graph import Graph  # Import the Graph class to use its methods

def bfs(graph, start, goal):
    queue = deque([(start, [])])  # Initialize the queue with the start state and an empty path
    visited = {start}  # Set of visited states to avoid cycles
    nodes_created = 1

    while queue:
        current_state, path = queue.popleft()  # Get the next state and path from the queue

        if current_state == goal:  # Check if the goal state is reached
            return path + [current_state], nodes_created  # Return the path including the current state

        for next_state in graph.generate_possible_moves(current_state):
            if next_state not in visited:  # Only consider unvisited states
                visited.add(next_state)  # Mark the new state as visited
                queue.append((next_state, path + [current_state]))  # Add the new state and path to the queue
                nodes_created += 1
    return None, nodes_created  # Return None if no solution is found
