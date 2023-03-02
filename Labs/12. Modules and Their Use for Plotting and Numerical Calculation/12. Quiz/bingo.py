#! /usr/bin/env python3

import numpy as np

row_header = ["B", "I", "N", "G", "O"]
col_header = ["1", "2", "3", "4", "5"]

board = [
    "t",
    "e",
    "x",
    "a",
    "s",
    "h",
    "b",
    "r",
    "p",
    "l",
    "y",
    "k",
    "i",
    "q",
    "z",
    "v",
    "o",
    "c",
    "w",
    "d",
    "g",
    "f",
    "m",
    "u",
    "n",
]

# reshape into a 5x5 matrix
board = np.array(board).reshape(5, 5)

# user input
user_input = input("Enter your message: ")

# decrypt message
message = ""
# iter by taking 2 letters at a time
for i in range(0, len(user_input), 2):
    # get the letter
    letter = user_input[i]
    # get the number
    number = int(user_input[i + 1])
    # get the index
    index = number - 1
    # get the letter
    message += board[index][row_header.index(letter)]
print(message)
