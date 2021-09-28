# Python3

```
return 1 if (n <= 1) else (n * factorial(n-1))
```

## Explanation

This code uses a ternary statement.  A ternary statement is shorthand for a quick and easy `if` `else` statement.  Be careful if your statement is too long or nested as these can easily become difficult to read, aka, *clever code*.

#### Long version of the ternary statement:

```
>>> if (n <= 1):
>>> 	return 1
>>> else:
>>> 	return (n * factorial(n-1))
```
## Recursion Explained

You can think of recursion as a `while True` infinite loop.  In fact, all recursive functions are replaceable through the use of loops.  And as with infinite loops, you'll need a **base case** that prevents it from being infinite.  The second requirement is the **recursive case** which breaks down our problem into smaller, more manageable steps.


