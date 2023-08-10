#!/usr/bin/env python3

def main():

    test_cases = [4, 17, 4, 6, 9]
    for n in test_cases:
        for a in range(1, n+1):
            print(a, sep='', end='')
        print()

    return None


if __name__ == "__main__":
    main()
