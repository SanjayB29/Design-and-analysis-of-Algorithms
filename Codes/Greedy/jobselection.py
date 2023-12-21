def find_platform(arr, dep, n):
    # Sort arrival and departure arrays
    arr.sort()
    dep.sort()

    # platforms_needed indicates number of platforms needed at a time
    platforms_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in merge sort
    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            platforms_needed += 1
            i += 1

            # Update result if needed 
            if (platforms_needed > result):  
                result = platforms_needed
        else:
            platforms_needed -= 1
            j += 1

    return result

# Example:
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ", find_platform(arr, dep, n))
