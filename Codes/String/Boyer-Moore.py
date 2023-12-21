def boyer_moore(text, pattern):
    # Function to create a bad character shift table
    def bad_char_table(pattern):
        badCharShift = {}
        len_pattern = len(pattern)
        for i in range(len_pattern):
            # The last occurrence of the character in pattern is stored
            badCharShift[ord(pattern[i])] = max(1, len_pattern - i - 1)
        return badCharShift

    # Create the bad character shift table
    badCharShift = bad_char_table(pattern)

    len_pattern = len(pattern)
    len_text = len(text)
    s = 0  # s is the shift of the pattern with respect to text

    while s <= len_text - len_pattern:
        j = len_pattern - 1

        # Keep reducing index j while characters of pattern and text are matching at this shift
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # If the pattern is present at the current shift, then index j will become -1
        if j < 0:
            print("Pattern occurs at shift = {}".format(s))

            # Shift the pattern so that it moves past the current match
            s += (len_pattern - badCharShift.get(ord(text[s]), len_pattern)) if s + len_pattern < len_text else 1
        else:
            # Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern.
            # The max function is used to make sure that we get a positive shift.
            # Use get method with default value equal to the length of the pattern
            s += max(1, j - badCharShift.get(ord(text[s + j]), len_pattern))

# Example usage
text = "ABAAABCD"
pattern = "BCDA"
boyer_moore(text, pattern)

