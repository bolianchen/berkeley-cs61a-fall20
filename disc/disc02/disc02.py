
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true 
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i < n:
        if cond(i):
            print(i)
        i += 1

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def matcher(cond):
        i = 1
        while i < n:
            if cond(i):
                print(i)
            i += 1
    return matcher

# 1.4 write curry2 as a lambda function
def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f

lambda_curry2 = lambda h: lambda x: lambda y: h(x,y)


def print_delayed(x):
    """Return a new function. This new function, when called, will print out
    x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f = f('hi')
    5
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

def print_n(n):
    """ take an integer n and returns a repeatable print function
    >>> f = print_n(2)
    >>> f = f('hi')
    hi
    >>> f = f('hello')
    hello
    >>> f = f('bye')
    done
    >>> g = print_n(1)
    >>> g = g('first')('second')('third')
    first
    done
    done
    """
    def inner_print(s):
        if n > 0:
            print(s)
        else:
            print('done')
        return print_n(n-1)
    return inner_print



        



