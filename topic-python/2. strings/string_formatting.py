#!/usr/bin/env python3

def print_formatted(number):

    # number = 17
    max_width = len(bin(number)[2:])

    for i in range(1, number+1):
        print(str(i).rjust(max_width),
              oct(i)[2:].rjust(max_width),
              hex(i)[2:].upper().rjust(max_width),
              bin(i)[2:].rjust(max_width))


def main():
    while True:
        n = int(input('Input an integer: '))
        print_formatted(n)


if __name__ == "__main__":
    main()
