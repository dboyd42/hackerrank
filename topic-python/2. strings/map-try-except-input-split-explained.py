#!/usr/bin/env python3

def main():

    while True:
        try:
            n, m = map(int, input().split())
            break
        except ValueError:
            print("Invalid input. Please enter in two " +
                  "space-separated integers")
    print(n, m)


if __name__ == "__main__":
    main()
