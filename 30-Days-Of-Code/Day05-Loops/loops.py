#!/bin/python3

def loop_me(n):
    for i in range(10):
        print(n, "x", i+1, "=", (i+1)*n )

if __name__ == '__main__':
    n = int(input().strip())
    loop_me(n)

