def KMP_search(text, pattern):
    # Preprocess the pattern to get the longest prefix suffix array
    def compute_lps_array(pattern):
        length = 0  # length of the previous longest prefix suffix
        lps = [0] * len(pattern)
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps_array(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print("Pattern found at index " + str(i - j))
            j = lps[j - 1]

        # Mismatch after j matches
        elif i < len(text) and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMP_search(text, pattern)
