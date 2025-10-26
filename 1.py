from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start, [start], 0))  # (f, current_node, path, g)

    visited = set()

    while not frontier.empty():
        f, current, path, g = frontier.get()

        if current == goal:
            print(f"Path found: {' -> '.join(path)} with cost: {g}")
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor not in visited:
                g_new = g + cost
                h_new = heuristic.get(neighbor, 0)
                f_new = g_new + h_new
                frontier.put((f_new, neighbor, path + [neighbor], g_new))

    print("No path found.")
    return None

# Example Graph (edges with cost)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 1},
    'E': {'D': 2, 'G': 5},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values (estimated cost to goal 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

# Run A* Search
a_star_search(graph, 'A', 'G', heuristic)
