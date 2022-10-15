#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   Go Moves
# Date:         10 14 2022

"""
NOTE

I am using termcolor, if you cannot get it to work on your system via
(`pip3 install termcolor`) then try repl since it works on repl
"""

try:
    from termcolor import colored
except:
    def colored(a, b): return a

# 9x9 board
board = [[' ' for _ in range(10)] for _ in range(10)]
player = 'o'

while True:
    # get position from user
    try:
        pos = input("Enter position (e.g 1  2): ")
        x, y = pos.split()
        x, y = int(x), int(y)
    except:
        print("Invalid input")
        continue

    # check if position is valid
    if x < 0 or x > 9 or y < 0 or y > 9:
        print("Invalid position")
        continue

    # check if position is empty
    if board[x][y] != ' ':
        print("Position already occupied")
        continue

    # set position to symbol
    board[x][y] = player

    # switch symbol
    if player == 'o':
        player = 'O'
    else:
        player = 'o'

    # print board
    for row in board:
        for col in row:
            if col == 'o':
                print(colored(col, 'red'), end=' ')
            elif col == 'O':
                print(colored(col, 'blue'), end=' ')
            else:
                print(col, end=' ')
        print()

    # if the board doesnt have any ' ' then its full
    if ' ' not in [item for sublist in board for item in sublist]:
        break

