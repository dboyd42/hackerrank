#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    # Unpack and concatenate a list through the reverse class
    print(*reversed(arr))

