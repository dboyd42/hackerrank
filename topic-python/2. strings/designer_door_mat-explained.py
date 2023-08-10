#!/usr/bin/env python3

import random

cols = random.randint(21, 51)
rows = random.randint(3, 11)
if cols % 2 == 0:
    cols += 1
if rows % 2 == 0:
    rows += 1
print('cols=', cols, '\nrows=', rows, '\n\n', sep='')

# The '2' is to double the '.|.' ea. time ::> row 0 = (2*0 + 1) --> 1x('.|.')
rows_upper = [('.|.' * (2 * i + 1)).center(cols, '_') for i in range(rows // 2)]
rows_middle = 'WELCOME'.center(cols, '.')
rows_lower = rows_upper[::-1]

###
### Assembled patterns:
###
pattern = '\n'.join(rows_upper + [rows_middle] + rows_lower)
# pattern = '\n'.join(rows_upper + [rows_middle] + rows_upper[::-1])
# This works too, albeit redundant with the '\n' escape char
up = '\n'.join(rows_upper)
middle = ''.join(rows_middle)
lower = '\n'.join(rows_lower)

# print(rows_upper)
# print(rows_middle)
# print(rows_lower)
print("Broken up into pieces:")
print(up)
print(middle)
print(lower)
print("\nAssembled:")
print(pattern)
