#!/usr/bin/env python3

def is_leap(year):
    leap = False

    # Write you logic here
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
            if (year % 400 == 0):
                leap = True
    return leap

def main():

    # year = int(input())
    test_cases = [1800, 1900, 2100, 2200, 2300, 2500, 2000, 2400, 1990, 160000]
    for year in test_cases:
        print(is_leap(year))


if __name__ == "__main__":
    main()
