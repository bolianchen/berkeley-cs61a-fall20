#Q1.1
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2) 

#Q1.2
def count_k(n, k):
    """
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        count = 0
        step = k
        while step > 0:
            count += count_k(n-step, k)
            step -= 1
        return count

# Q2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [idx * s[idx] for idx in range(len(s)) if idx%2 == 0]
    

# Q2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2])
    90
    >>> max_product([5,10,5,10,5])
    125
    >>> max_product([])
    1
    """

    if len(s) == 0:
        return 1
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))
