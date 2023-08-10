#!/usr/bin/env python3

import textwrap


def wrap(string, max_width):
    s = textwrap.wrap(string, width=max_width)
    ws = '\n'.join(s)

    return ws


if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)
