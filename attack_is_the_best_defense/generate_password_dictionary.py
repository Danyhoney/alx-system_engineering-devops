#!/usr/bin/python3

import itertools

# Define characters for the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Define password length
password_length = 11

# Calculate the maximum number of passwords
max_passwords = 50000000

# Generate all possible combinations of characters
combinations = itertools.product(characters, repeat=password_length)

# Write combinations to a file
with open('password_dictionary.txt', 'w') as f:
    for idx, combo in enumerate(combinations):
        if idx >= max_passwords:
            break
        password = ''.join(combo)
        f.write(password + '\n')

print("Password dictionary created.")
