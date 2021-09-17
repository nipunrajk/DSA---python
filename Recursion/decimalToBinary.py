"""Convert a number from decimal to binary using recursion"""

def decimalTOBinary(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return 0
    return n % 2 + 10 * decimalTOBinary(int(n / 2))


print(decimalTOBinary(4))

