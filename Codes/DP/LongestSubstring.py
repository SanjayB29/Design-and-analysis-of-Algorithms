def longest_common_substring(str1, str2):
    # Lengths of the input strings
    m = len(str1)
    n = len(str2)

    # Creating a 2D array for tabulation
    # Initialize all values to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # To store the length of the longest common substring
    length_of_lcs = 0

    # To store the ending index of the longest common substring in str1
    end_index = 0

    # Building the dp table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length_of_lcs:
                    length_of_lcs = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    # Extracting the longest common substring
    lcs = str1[end_index - length_of_lcs : end_index]

    return lcs, length_of_lcs

# Example usage
str1 = "OldSite:GeeksforGeeks.org"
str2 = "NewSite:GeeksQuiz.com"
lcs, length = longest_common_substring(str1, str2)
print(f"Longest Common Substring: {lcs}")
print(f"Length of Longest Common Substring: {length}")
