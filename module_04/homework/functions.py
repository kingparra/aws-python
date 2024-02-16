#!/usr/bin/env python3


# 1
# As part one of your homework, you are asked to write
# a program that prints the sum of all the numbers from
# 1 to 777 that are divisible by 7. Please make sure that
# numbers 1, 7, 77, and 777 are not included. This program
# must be using “while” loop.
def sum_sequence():
    sum = 0
    count = 1
    while count < 777:
        if count % 7 == 0 and count not in [1, 7, 77, 777]:
            sum = count + sum
        count += 1
    return sum


print(sum_sequence())


# 2
# As part two of your homework, you are asked to write a program
# that is using a “for” loop and prints the sum of all the even
# numbers from 1 to 777.
def sum_even_to():
    sum = 0
    for x in range(1, 778):
        if x % 2 == 0:
            sum += x
    return sum


print(sum_even_to())


# 3
# As part three of your homework, you are asked to write
# a program(function) that accepts a number as an argument.
# It will return the square of that number.
def sqr(n):
    return n * n


# 4
# As part four of your homework, you are asked to write a program
# (function) that accepts a number as an argument. It adds 77
# to it and returns the result.
def add_77(n):
    return n + 77


# 5
# As part five of your homework, you are asked to write a
# program(function) that accepts a list of integers. It will
# return the sum of all the numbers that are in the list.
# Make an assumption that the input list contains only numbers
# (no other characters). Make sure to not use the built-in
# sum() function.
def sum(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum


# 6
# return a sorted list of the keys in a dictionary
def keys(d):
    return sorted(d.keys())
