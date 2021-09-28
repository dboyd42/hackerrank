#!/bin/python3

def hourglass(a):
    accumulator, greatest_sum = 0, 0
    sum_list = []
    arr_size = len(a)
    hg_size = int(arr_size/2)+1
    step = 2 # rows: 1,3

    # Iterate the main hourglass
    for row in range(hg_size):
        for col in range(hg_size):

            # Single/One hourglass
            if (col < hg_size):
                accumulator += a[row+1][col+1]  # middle row
            for in_row in range(row, row+hg_size, step):
                for in_col in range(col, col+hg_size-1):
                    accumulator += a[in_row][in_col]
            # Append accumulator to list
            sum_list.append(accumulator)
            accumulator = 0

    return(max(sum_list))

if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglass(arr))

