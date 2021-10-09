# Question1.1
def multiply(m, n):
    """Return the product of m and n without using * or mul
    >>> multiply(5, 3)
    15
    >>> multiply(3, 5)
    15
    """
    if m == 1:
        return n
    else:
        return n + multiply(m-1, n)


# Question1.2
def rec(x, y):
    """Return pow(x, y) for ys in int"""
    if y > 0:
        return x * rec(x, y-1)
    return 1

# Question1.3
def hailstone(n):
    """
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n + 1)

# Question1.4
def merge(n1, n2):
    """
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """

    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1%10 <= n2%10:
        return n1%10 + 10 * merge(n1//10, n2)
    else:
        return n2%10 + 10 * merge(n1, n2//10)

# Question1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    >>> mul_2 = make_func_repeater(lambda x: x * 2, 1)
    >>> mul_2(2)
    4
    >>> mul_2(5)
    32
    """

    def repeat(n):
        assert n > 0 and isinstance(n, int)
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))

    return repeat

# Question1.6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n == 1:
        return False
    else:
        return prime_helper(n, 2)

def prime_helper(n, k):
    if n%k == 0:
        return False
    else:
        if k+1 == n:
            return True
        return prime_helper(n, k+1)
