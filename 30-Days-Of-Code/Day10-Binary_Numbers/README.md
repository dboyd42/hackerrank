# Python3 One-Liner

`print(len(max(bin(int(input().strip()))[2:].split('0'))))`

## Explanation

Working from inside out:

1. `input()`: gets the input from the user
2. `int(input)`: converts string to int
3. `bin(int)`: converts the int to binary
4. `max(bin)`: returns the "biggest" item in a single iterable argument
5. `len(max)`: returns the number of items in a container
6. `print(len)`: outputs the length

### Code Breakdown
```
# 1. Get input
str_n = "439"
print("string input:", str_n)

# 2. Convert str to int
int_n = int(str_n)
print("int:", int_n)

# 3a. Convert int into binary
bin_n = bin(int_n)
print("bin:", bin_n)

# 3b. Strip binary to remove "0b"
start_idx = bin_n[2:]
print("splice:", start_idx)

# 3c. Split binary into list using "0" as your delimeter
split_bin_n = bin_n[2:].split('0')
print("split:", split_bin_n)

# 4. Find the max number in list
max_split_bin_n = max(split_bin_n)
print("max:", max_split_bin_n)

# 5. Find the length of the biggest number
len_max_split_bin_n = len(max_split_bin_n)
print("len:", len_max_split_bin_n)
```

### The Output
```
string input: 439
int: 439
bin: 0b110110111
splice: 110110111
split: ['11', '11', '111']
max: 111
len: 3
```

### Credit: Thank you [ali_roustaei](https://www.hackerrank.com/ali_roustaei) for the code!

