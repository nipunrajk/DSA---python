"""Calculate power of number using recursion"""

def power(base, exp):
    assert 0 <= exp == int(exp), 'The exponent should be positive integer only'
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * power(base, exp - 1)


print(power(2, 3))

