# Python3

```
class Calculator():
  def power(self, n, p):
    if  (n < 0) or (p < 0):
    raise Exception('n and p should be non-negative')
  return n**p
```

## Explanation

You can use the `raise` statement to *raise* an exception explicitly.  Meaning,
we can define an exception object rather than using Python's built-in
definitions.  The `raise` is a simple statement with the following syntax:
`raise <varName>('<stdout>')`.

When a raise exception is caught, the exception propagation mechanism begins
calling back upon itself in the stack.  This allows us to define the declared
exception object in the stub lock code within our class.

The exception works by taking our `<stdout>` back through the stack's
function->class->try calls with `try` being the top of the stack.  Now, since
the `try` failed, the `except` clause will be invoked with our defined
`raise` statement's `<stdout>`.  Hence, we're able to print out '`n and p
should be non-negative`'.

Lastly, if our power method's condition is never met, then it'll just return
the operation.

