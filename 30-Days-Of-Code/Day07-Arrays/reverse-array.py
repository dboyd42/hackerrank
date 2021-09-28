#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    # Use the reversed class and loop through array
    for i in reversed(arr):
        print(i, end=' ')

