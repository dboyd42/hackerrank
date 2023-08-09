#!/usr/bin/env python3

def main():

    a = int(input())
    b = int(input())

    floater = b and a/b or 0
    inter = int(floater)

    print(floater, inter, sep='\n')
    return


if __name__ == "__main__":
    main()
