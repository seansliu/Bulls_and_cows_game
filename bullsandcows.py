#******************************************************************************
# Shih-Chun Liu
# sl3497
# 4/21/2013
# file: bullsandcows.py
#
# This program contains useful functions for the game Bulls and Cows.
#******************************************************************************
import random


def random_number(size):
    '''selects a random nonrepeating number of the given size'''
    digits = '0123456789'
    generated = random.sample(digits, size)
    number = ''
    for x in generated:
        number += x
    return number

def bullscows(guess, comp_num):
    '''evaluates the player's guess and returns the bulls and cows'''
    bulls = cows = 0
    for i in range(len(comp_num)):
        if guess[i] in comp_num:
            repeats = guess.count(guess[i])
            cows += (1. / repeats)
            if guess[i] == comp_num[i]:
                bulls += 1
                cows -= 1
    return str(bulls), str(int(round(cows)))

def check_guess(guess, length):
    '''checks whether guess is a string of numbers of the correct length'''
    g = list(guess)
    if all(x in '1234567890' for x in g) and (len(guess) == length):
        return True
    else:
        return False
