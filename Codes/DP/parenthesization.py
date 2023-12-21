def matrix_chain_order(p):
    """
    p: list of dimensions of matrices such that the ith matrix has dimensions p[i-1] x p[i]
    """
    n = len(p) - 1  # Number of matrices
    m = [[0 for _ in range(n)] for _ in range(n)]  # Initializing the DP table with zeros
    s = [[0 for _ in range(n)] for _ in range(n)]  # To store the split positions

    # L is the chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i - 1][j - 1] = float('inf')  # Set to infinity initially
            for k in range(i, j):
                # Cost = cost/scalar multiplications
                cost = m[i - 1][k - 1] + m[k][j - 1] + p[i - 1] * p[k] * p[j]
                if cost < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = cost
                    s[i - 1][j - 1] = k  # Store the split position

    return m, s

def print_optimal_parens(s, i, j):
    """
    Utility function to print the optimal parenthesization
    s: DP table containing split positions
    i, j: matrix indices
    """
    if i == j:
        print(f'A{i}', end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i - 1][j - 1])
        print_optimal_parens(s, s[i - 1][j - 1] + 1, j)
        print(')', end='')

# Example usage
p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(p)
print("Minimum number of multiplications is:", m[0][len(p)-2])
print("Optimal Parenthesization is: ", end='')
print_optimal_parens(s, 1, len(p) - 1)
