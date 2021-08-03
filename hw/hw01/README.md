# Homework 1: Variables & Functions, Control

https://inst.eecs.berkeley.edu/~cs61a/fa20/hw/hw01/

## Notes

### Q5: If Function vs Statement
This question was mind-boggling for me, so I think it may be worthwile to understand it clearly.  
`if_function` is a function shown below to emulate an `if` statement. It seems to work fine for the examples in its doctest when the arguments are simple expressions. 
```python
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
```

For a while, I was thinking that `with_if_statement` and `with_if_function` just do the same thing and I might not be able to solve it until I gradually noticed several facts:
* Both of them return None. It means true_func() or false_func() should return None.
* The 3 functions you need to write, cond(), true_func() and false_func(), should print the specifed number(s).
* `with_if_function` returns a call to `if_function` with functions as arguments. Those functions must be evaluated before `if_function` can be evaluated.

```python
def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"

def true_func():
    "*** YOUR CODE HERE ***"

def false_func():
    "*** YOUR CODE HERE ***"
```



