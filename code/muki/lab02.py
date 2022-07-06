# Muki - Lab03 Numbers to Phrases


'''
Lab 3: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.

This block was borrowed from class
'''
# imports just in case, I will remove these if I don't use them
import numbers
import math
import random

#   Version 1:
numbah = input('please enter a number between 0 and 99:\n')
numbah = int(numbah)
ones_place = numbah%10
tens_place = numbah//10

print(f'{numbah}\t Thanks for your entry.')
print(ones_place)
print(tens_place)


single_digits = {
    '0':'',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
}
tens_digits = {
    '0':'',
    '1':'',
    '2':'twenty',
    '3':'thirty',
    '4':'fourty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety',
}
hundreds_digits = {
    '0':'',
    '1':'one hundred',
    '2':'two hundred',
    '3':'three hundred',
    '4':'four hundred',
    '5':'five hundred',
    '6':'six hundred',
    '7':'seven hundred',
    '8':'eight hundred',
    '9':'nine hundred',
}

print(f'{numbah}\t Thanks for your entry.')
str(ones_place)
str(tens_place)
print(f'{tens_digits[tens_place]}')
print(f'{single_digits[ones_place]}')
