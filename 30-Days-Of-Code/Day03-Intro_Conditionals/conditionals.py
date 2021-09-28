#!/bin/python3

def weird(n):
    # Weird # odd # 1,3,5 # 6-20
    if (n % 2 == 1) or (( n >= 6 ) and ( n <= 20)):
        print("Weird")
    #Not Weird # even # 2,4 # >20
    else:
        print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    weird(N)

