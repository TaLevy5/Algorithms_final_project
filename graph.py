class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, board_state):
        # board_state is a tuple representing the puzzle state.
        if board_state not in self.vertices:
            self.vertices[board_state] = []

    def add_edge(self, from_state, to_state):
        if from_state in self.vertices and to_state in self.vertices:
            self.vertices[from_state].append(to_state)
            self.vertices[to_state].append(from_state)

    def get_neighbors(self, board_state):
        # Returns the neighbors of a given board state.
        # This represents all possible moves from the given state.
        return self.vertices.get(board_state, [])

    def generate_possible_moves(self, board_state):
        # Generate all possible moves from the given board state
        neighbors = []
        size = int(len(board_state) ** 0.5)  # Calculate the size of the board (4 for 15-puzzle)
        empty_pos = board_state.index(0)  # Find the position of the empty space
        row, col = divmod(empty_pos, size) # find the col and row of the empty space

        # Possible directions where the empty tile can move
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < size and 0 <= new_col < size:
                new_pos = new_row * size + new_col
                new_state = list(board_state)
                new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]  # Swap the empty space with the adjacent tile
                neighbors.append(tuple(new_state))

        return neighbors

    def build_graph(self, initial_state):
        if initial_state not in self.vertices:
                self.add_vertex(initial_state)

        for neighbor in self.generate_possible_moves(initial_state):
                if neighbor not in self.vertices:
                    self.add_vertex(neighbor)
                self.add_edge(initial_state, neighbor)

        # Recursion can be controlled to avoid exploring too deep if necessary
        # For testing, you might want to limit the depth or avoid recursion altogether

    def display_graph(self):
        # This is a helper method to display the graph's vertices and their neighbors
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")
