def fractional_knapsack(value, weight, capacity):
    # Index by density
    index = list(range(len(value)))
    # Calculate the value to weight ratio and sort by this ratio
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)

    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * fractions[i]
            break

    return max_value, fractions

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, fractions = fractional_knapsack(values, weights, capacity)
print("The maximum value of items that can be carried:", max_value)
print("Fractions in which the items should be taken:", fractions)
