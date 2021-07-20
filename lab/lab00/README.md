# Notes from Lab 0

## Appendix: Useful Python command line options

The **-i** option runs your Python script, then opens an interactive session. To exit, type exit() into the interpreter prompt or use the keyboard shortcut Ctrl-D on Linux/Mac machines or Ctrl-Z Enter on Windows.

If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.
```shell
$ python -i lab00.py
>>> twenty_twenty()
2020
```

The **-m doctest** option runs doctests in a particular file. Doctests are defined in the docstring of functions. Each test in the file consists of >>> followed by some Python code and the expected output.

```shell
def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return 2 * 1000 + 2 * 10
```

Run its doctest
```shell
$ python3 -m doctest -v lab00.py
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

Revise the function return to be inconsistent with its doctest
```shell
def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return 2 * 1000 + 2 * 10 + 2
```

Run the doctest and the reuslts failed
```shell
$ python3 -m doctest -v lab00.py
Trying:
    twenty_twenty()
Expecting:
    2020
**********************************************************************
File "/Users/bolianchen/Projects/My-CS61A-FALL20/lab/lab00/lab00.py", line 5, in lab00.twenty_twenty
Failed example:
    twenty_twenty()
Expected:
    2020
Got:
    2022
1 items had no tests:
    lab00
**********************************************************************
1 items had failures:
   1 of   1 in lab00.twenty_twenty
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
```
