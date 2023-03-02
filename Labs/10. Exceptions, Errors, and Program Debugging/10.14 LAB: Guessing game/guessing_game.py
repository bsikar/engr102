#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 10.14 LAB: Guessing game
# Date: 11 03 2022

# get the guess from the user by using recusion and a try/except block
def get_guess(x):
    try:
        guess = int(input(x))
        return guess
    except:
        return get_guess("Bad input! Try again: ")

# play the game
def game(secret):
    count = 1
    # inital prompt
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    # while loop to keep the game going
    while True:
        guess = get_guess("What is your guess? ")
        if guess == secret:
            # if the guess is correct break from the loop
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        count += 1
    # ending prompt
    print(f"You guessed it! It took you {count} guesses.")

# for testing use secret = 26
secret = 26
# play the game
game(secret)
