# Enter your code here. Read input from STDIN. Print output to STDOUT
# Get Input
n_words = int(input())  # prints: 2
users_words = []

# Append user's words to a users_words list
for get_words in range(n_words):
    users_words.append(input()) # prints: ['Hacker', 'Rank']

### Calculate data ###
# Iterate through users_words list
for word in users_words:
    even, odd = [], []
    w_length = len(word) # prints: 6, 4
    # Iterate letters in word
    for i in range(w_length):
        even.append(word[i]) if (i % 2 == 0) else odd.append(word[i])

    ### Output result ###
    # print(''.join(even), ''.join(odd))  # method 1: str.join(<list>)
    print(*even, ' ', *odd, sep='')  # method 2: unpacking syntax

'''
# One-liner (src: HR>Discussions)
for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])

    Explanation:
        for in range( int( input() )):  # T0: << 2
            s=input();                  # string=input //NOTE: ';' is a statement sep
            # Uses methods(unpacking, str.join)
            print(*[]) # unpack // in this case, unpacks a string's chars
                *[ ''.join(s[::2])  ] # joins (cats) var s's indices to an empty str
                s[ ::2 ] # str[ start : end : step ] # ==> 0->2 all even indices
                s[ 1::2 ] # str[ start : end : step ] # ==> all odd indices
'''

