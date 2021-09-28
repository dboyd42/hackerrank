# Python3

```
# Declare two instance variables
def __init__(self):
  self.stack = []
  self.queue = []

# Adds an item to the end of the list
def pushCharacter(self, item):
  self.stack.append(item)

# Removes an item from the end of the list
def popCharacter(self):
  return self.stack.pop()

# Adds an item to the end of the list
def enqueueCharacter(self, item):
  self.queue.append(item)

# Removes an item from the front of the list
def dequeueCharacter(self):
  return self.queue.pop(0)
```

## Explanation

There are multiple ways to implement a palindrome, but the problem asks us to use the **stack** and **queue** data structures.

A **stack** is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.  Some real world examples include the order of operations, undo (`^+z` or `⌘+z`), and your browser's back button.

A **queue** is similar to a stack, but calls for the removal of items at the opposing end.  Some real word examples include standing in line at a cafeteria, a printer's print queue, and in a call center where you're put on hold until it's your turn to speak.

The problem doesn't ask for a full implementation of these two data structures, but instead only calls for the adding and removal of characters; predefined in the locked stub code as: `pushCharacter`, `popCharacter`, `queueCharacter`, `dequeueCharacter`.

In the code above, I used the `list.append` method to add an item, and `list.pop` to remove an item.  The `popChracter` method returns the popped item from the *end of the list*.  `pop` doesn't require any arguements as it defaults to the end of a list "`[-1]`".  The `dequeueChracter` method returns the popped item from the *beginning of the list*.   To access the beginning of the list, we pass the first index "`0`" in  `pop`'s first parameter.

Another way to implement the queue data structure, is by using `list.insert(0, item)` in the `queueCharacter` method, and then popping in the `dequeueCharacter` method without passing any arguments in its `pop`.

There's also a `pythonds.basic` module that holds all these data structures as classes, relieving us from defining these methods.  However, HackerRank refused to import this module.

