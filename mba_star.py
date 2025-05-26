import heapq

# Define a simple Node class
class Node:
    def __init__(self, state, path, cost, heuristic):
        self.state = state
        self.path = path
        self.cost = cost
        self.heuristic = heuristic
        self.f = cost + heuristic  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.f < other.f

# Sample graph (A to G)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [],
    'F': [('G', 2)],
    'G': []
}

# Simple heuristic (estimates from each node to goal 'G')
heuristic_values = {
    'A': 7, 'B': 6, 'C': 2,
    'D': 3, 'E': 5, 'F': 1, 'G': 0
}

def memory_bounded_a_star(start, goal, memory_limit):
    frontier = []
    heapq.heappush(frontier, Node(start, [start], 0, heuristic_values[start]))

    while frontier:
        node = heapq.heappop(frontier)

        # Goal check
        if node.state == goal:
            return node.path

        # Expand successors
        for neighbor, cost in graph[node.state]:
            new_cost = node.cost + cost
            new_path = node.path + [neighbor]
            h = heuristic_values[neighbor]
            new_node = Node(neighbor, new_path, new_cost, h)
            heapq.heappush(frontier, new_node)

        # Limit memory (keep only best 'n' nodes)
        if len(frontier) > memory_limit:
            frontier = heapq.nsmallest(memory_limit, frontier)
            heapq.heapify(frontier)

    return None

# Run the algorithm
result = memory_bounded_a_star('A', 'G', memory_limit=5)
print("Path found:", result)
