# Python3

```
#!/bin/python3

try:
    print(int(input()))
except ValueError:
    print("Bad String")
```

## Hacking the Error
### "Error reading result file.You should use exception handling concepts."

This error appeared when all of my test cases' output matched HackerRank's expected output.  To bypass this error, I removed the `if __name__ == "__main__"` statement and all comments.

The above code is one method to pass the test cases.

