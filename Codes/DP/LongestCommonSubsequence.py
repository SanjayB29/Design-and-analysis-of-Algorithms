def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D table to store lengths of LCS for substrings
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Building the table in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following the indices from L to find the LCS
    index = L[m][n]

    # Create a character array to store the LCS string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the bottom right corner and follow the LCS path
    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in both strings are same, then it's part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and go in the direction of the larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print("LCS is", lcs(X, Y))
