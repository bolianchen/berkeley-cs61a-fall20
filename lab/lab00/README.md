# Lab 00

https://inst.eecs.berkeley.edu/~cs61a/fa20/lab/lab00/

## Notes

### `-i` option
Run a python script with `-i` option would opens an interactive session afterward; all defined variables, functions and classes in the script are accessible.
```shell
$ cat foo.py
boo = "Hello World"
$ python -i foo.py
>>> foo
"Hello World"
```

### **Keyboard shortcuts to exit an interactive session**
- `Ctrl-D` for Linux/Mac
- `Ctrl-Z Enter` for Windows  
&nbsp;

### **Doctests**
Doctests are defined within the docstring of functions with `>>>` followed by some Python code and the expected output.  

```python
# lab00.py has a function with doctests defined
def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return 2 * 1000 + 2 * 10
```

Run doctests in `lab00.py` with **`-m doctest`** option 
```shell
$ python3 -m doctest lab00.py
Trying:
    twenty_twenty()
Expecting:
    2020
ok
1 items had no tests:
    lab00
1 items passed all tests:
   1 tests in lab00.twenty_twenty
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```
