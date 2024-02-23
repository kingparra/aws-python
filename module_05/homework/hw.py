#!/usr/bin/env python3


# 1
def first_five_multiples():
    """Return a list of the first five multiples of n"""
    n = int(input("Enter a number: "))
    return [n * x for x in range(1, 6)]


# 2
def evens_between(x, y):
    """Return a list of even numbers from x up to but not including y"""
    return [n for n in range(x, y) if n % 2 == 0]


# 3
def triangle(x):
    """Print a string that is a triangle of numbers that increases in length until x"""
    print("\n".join([str(x) * x for x in range(1, x+1)]))


# 4
def square(ct):
    """Print a square of hash marks that has dimensions x * x"""
    print("\n".join(["#" * ct for count in range(0, ct)]))


# 5
def sum_codepoints(s):
    """Take a string and sum the codepoints of every character in it"""
    sum = 0
    for char in s:
        sum += ord(char)
    return sum
