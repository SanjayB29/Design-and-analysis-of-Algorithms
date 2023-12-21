def rodCutting(prices, n):
    # Create a 2D array to store the solutions of subproblems
    # dp[i][j] will store the maximum revenue for a rod of length j using prices[1...i]
    dp = [[0 for _ in range(n+1)] for _ in range(len(prices)+1)]

    # Build the table dp[][] in bottom-up manner
    for i in range(1, len(prices)+1):
        for j in range(1, n+1):
            # If the length of the rod is less than the current piece length, don't cut
            if i > j:
                dp[i][j] = dp[i-1][j]
            else:
                # Maximum of not cutting at this length or cutting and considering previous solutions
                dp[i][j] = max(dp[i-1][j], prices[i-1] + dp[i][j-i])

    # The maximum revenue is stored in dp[len(prices)][n]
    return dp[len(prices)][n]

# Example usage
length_of_rod = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]  # Prices for lengths 1, 2, ..., n
max_revenue = rodCutting(prices, length_of_rod)
print("Maximum Revenue: ", max_revenue)
