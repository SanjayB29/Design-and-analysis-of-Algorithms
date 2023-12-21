def subset_sum(nums, target):
    """
    Determine if there's a subset of `nums` that sums to `target`.

    Args:
    nums (List[int]): A list of integers.
    target (int): The target sum.

    Returns:
    bool: True if there's a subset that sums to `target`, False otherwise.
    """
    n = len(nums)

    # Create a 2D array `dp` with dimensions (n+1) x (target+1)
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # Initialize the first column as True, as the sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Populate the dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                # Include the current element or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                # Exclude the current element
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


# Example usage
nums = [3, 34, 4, 12, 5, 2]
target = 9
result = subset_sum(nums, target)
print(f"Is there a subset with sum {target}? {'Yes' if result else 'No'}")
