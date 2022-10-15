#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment:  7.25 LAB: Pig latin
# Date: 10 14 2022

def pig_latin(word):
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"
    cluster = "bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw wh wr".split()

    pig_word = ""
    for word in word.split():
        # If a word starts with a consonant (or cluster of consonants that form one sound), move the
        # consonant(s) to the end of the word, and add “ay” to the end
        if word[0] in consonants:
            if word[0:2] in cluster:
                pig_word += word[2:] + word[0:2] + "ay"
            else:
                pig_word += word[1:] + word[0] + "ay"
        # If a word starts with a vowel, add “yay” on to the end of the word
        elif word[0] in vowels:
            pig_word += word + "yay"
        # else return word
        else:
            pig_word += word

        pig_word += ' '
    return pig_word

word = input("Enter word(s) to convert to Pig Latin: ")
print(f'In Pig Latin, "{word}" is: {pig_latin(word)}')
