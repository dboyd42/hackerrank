#!/usr/bin/env python3

# Score:            55%
#   - Correctness: 100%
#   - Performance:   0%
#   |--> Performance describes if the program behaves correctly for large
#                    inputs. Points are deducted if the prgm exceeds the time
#                    limit on large data sets, which indicates a sub-optimal
#                    approach.
def solution(A):

    missing = 1
    a = [x for x in set(sorted(A)) if x > 0]
    for i in a:
        if i >= missing and missing in a:
            missing = i+1
    return missing


def main():
    test_cases = [
        [1, 2, 3],
        [-1, -3],
        [1, 3, 6, 4, 1, 2]
    ]
    for i in test_cases:
        print(i)
        print(solution(i))


main()
