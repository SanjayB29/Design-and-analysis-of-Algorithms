def StringMatch(s, p):
    m = len(s)
    n = len(p)
    d = {}

    # Populate the dictionary with the rightmost occurrence of each character in the pattern except the last one
    for i in range(n - 1):
        d[p[i]] = i

    i = n - 1  # Start comparing from the end of the pattern
    while i < m:
        j = n - 1  # Start from the end of the pattern
        while j >= 0 and s[i - (n - 1 - j)] == p[j]:
            j -= 1

        if j < 0:
            return i - n + 1  # Match found

        # Apply the bad character rule
        i += max(1, j - d.get(s[i - (n - 1 - j)], -1))

    return -1  # No match found

print(StringMatch("Sanjay", "ay"))


print(StringMatch("Sanjay","njay"))
