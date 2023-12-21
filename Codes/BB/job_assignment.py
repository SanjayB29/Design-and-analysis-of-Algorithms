import heapq

def calculate_lower_bound(matrix, path):
    remaining_cities = [i for i in range(len(matrix)) if i not in path]
    if not remaining_cities:
        return 0  # All cities are in the path

    lower_bound = sum(min(matrix[path[i]]) for i in range(len(path) - 1))
    lower_bound += min(matrix[path[-1]][city] for city in remaining_cities)
    return lower_bound



def branch_and_bound_tsp(distance_matrix):
    # Priority queue for the nodes to explore
    queue = []
    heapq.heappush(queue, (0, [0]))  # Starting with the first city

    best_cost = float('inf')
    best_path = []

    while queue:
        cost, path = heapq.heappop(queue)

        if len(path) == len(distance_matrix) and cost < best_cost:
            best_cost = cost
            best_path = path
            continue

        for next_city in range(len(distance_matrix)):
            if next_city not in path:
                new_path = path + [next_city]
                new_cost = cost + distance_matrix[path[-1]][next_city]

                if new_cost < best_cost:
                    lower_bound = calculate_lower_bound(distance_matrix, new_path)
                    if lower_bound < best_cost:
                        heapq.heappush(queue, (new_cost, new_path))

    return best_path, best_cost

# Example usage
distance_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
path, cost = branch_and_bound_tsp(distance_matrix)
print("Path:", path)
print("Cost:", cost)
