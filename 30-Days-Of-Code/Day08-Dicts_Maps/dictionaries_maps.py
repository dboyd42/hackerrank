#!/usr/bin/python3

# Get number entries
n_entries = int(input())

# Add key-value pairs: <class dict(<object>)>
phonebook = dict(input().split() for _ in range(n_entries))

# Query dictionary
while True: # number of query inputs are unknown
    try:
        key = input()
    except EOFError:  # no more input from a FILE
        break
    if phonebook.get(key):
        print(key+'='+phonebook.get(key))
    else:
        print('Not found')

