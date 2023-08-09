#!/usr/bin/env python3

def door_mat_design(rows, columns):
    pattern = [('.|.' * (2 * i + 1)).center(columns, '-') for i in range(rows // 2)]
    welcome = 'WELCOME'.center(columns, '-')
    pattern = '\n'.join(pattern + [welcome] + pattern[::-1])
    return pattern


# Read input
n, m = map(int, input().split())

# Generate and print door mat design
design = door_mat_design(n, m)
print(design)
