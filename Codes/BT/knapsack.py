def knapsack(capacity, weights, values, n):
    # Initialize variables to store the maximum value and the best combination
    max_value = 0
    best_combination = []

    def backtrack(i, current_weight, current_value, current_combination):
        nonlocal max_value, best_combination

        # Check if the current index is beyond the last item
        if i == n:
            if current_value > max_value:
                max_value = current_value
                best_combination = current_combination.copy()
            return

        # Include the current item, if it doesn't exceed the capacity
        if current_weight + weights[i] <= capacity:
            current_combination.append(i)
            backtrack(i + 1, current_weight + weights[i], current_value + values[i], current_combination)
            current_combination.pop()

        # Exclude the current item
        backtrack(i + 1, current_weight, current_value, current_combination)

    # Start the backtracking process from the first item
    backtrack(0, 0, 0, [])
    return max_value, best_combination

# Example usage
weights = [1, 2, 4, 2, 5]
values = [5, 3, 5, 3, 2]
capacity = 10
n = len(values)

max_val, items_selected = knapsack(capacity, weights, values, n)
print("Maximum Value: ", max_val)
print("Items Selected (0-indexed): ", items_selected)
