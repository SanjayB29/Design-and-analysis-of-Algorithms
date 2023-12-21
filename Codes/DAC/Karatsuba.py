def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Determines the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the digit sequences about the middle
    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    # Three recursive steps
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    return (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0

# Example usage
num1 = 12
num2 = 6
result = karatsuba(num1, num2)
print(f"The product of {num1} and {num2} is {result}")
