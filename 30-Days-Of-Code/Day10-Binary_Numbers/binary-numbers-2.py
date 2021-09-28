#!/bin/python3

def binCount(n):
    # Convert int to binary (n = 5, binary = 101)
    res = binary = format(n, 'b') # format(<value>, <[format_spec]>)
    counter, matches = 0, 0
    flag = False
    for bit in range(len(binary)):
        # type: bit=int, len(binary)=int, binary[bit]=str
        if (binary[bit] == "1"):
            flag = True
            counter += 1
        elif (binary[bit] == "0"):
            matches = compare(counter, matches)
            flag = False
            counter = 0
        # Test last index
        if (flag == True) and (bit == len(binary)-1):
           matches = compare(counter, matches)
    return matches

def compare(counter, matches):
    if (counter > matches):
        return counter
    return matches

if __name__ == '__main__':
    n = int(input().strip())
    print(binCount(n))

