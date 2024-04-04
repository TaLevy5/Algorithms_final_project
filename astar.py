import heapq

def manhattan_distance(current_state, goal_state):
    size = int(len(current_state) ** 0.5)
    total_distance = 0
    for i in range(1, size * size):
        current_pos = current_state.index(i)
        goal_pos = goal_state.index(i)
        current_row, current_col = divmod(current_pos, size)
        goal_row, goal_col = divmod(goal_pos, size)
        total_distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return total_distance

def zero_heuristic(current_state, goal_state):
    return 0

def custom_heuristic(current_state, goal_state):
    # Implement your custom heuristic here
    # Example: Overestimate by adding a constant value to the Manhattan distance
    return manhattan_distance(current_state, goal_state) + 10

def astar(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), 0, start, [start]))  # (estimated total cost, path cost, state, path)
    visited = set()

    while open_list:
        estimated_total_cost, path_cost, current_state, path = heapq.heappop(open_list)

        if current_state in visited:
            continue

        if current_state == goal:
            return path

        visited.add(current_state)

        for next_state in graph.generate_possible_moves(current_state):
            if next_state not in visited:
                new_path_cost = path_cost + 1  # Assuming each move costs 1
                heapq.heappush(open_list, (new_path_cost + heuristic(next_state, goal), new_path_cost, next_state, path + [next_state]))

    return None
