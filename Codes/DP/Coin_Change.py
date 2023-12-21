def coinChange(coins, amount):
    n = len(coins)
    # A large number to represent infinity. This will be used to initialize non-feasible values.
    inf = float('inf')

    # Create a 2D DP table with (n + 1) rows and (amount + 1) columns.
    dp = [[inf for _ in range(amount + 1)] for _ in range(n + 1)]

    # Base case: 0 coins are needed to make amount 0
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            # Exclude the coin
            dp[i][j] = dp[i - 1][j]

            # Include the coin, if it doesn't exceed the current amount
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i - 1]])

    # If the amount cannot be made by any combination of the coins, return -1
    return dp[n][amount] if dp[n][amount] != inf else -1

# Example usage:
coins = [1, 2, 5]  # Denominations of the coins
amount = 11  # Target amount
print(coinChange(coins, amount))

