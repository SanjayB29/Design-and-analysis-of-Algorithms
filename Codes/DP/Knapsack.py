def knapsack(weights, values, W):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.

    :param weights: List of weights of the items.
    :param values: List of values of the items.
    :param W: Maximum weight capacity of the knapsack.
    :return: Maximum value that can be put in the knapsack.
    """
    n = len(values)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table dp[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],  dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
W = 50

print("Maximum value in knapsack =", knapsack(weights, values, W))
