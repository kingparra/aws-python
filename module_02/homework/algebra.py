#!/usr/bin/env python3
# Assignment 2 - calculate an algebraic expressions and print it out


def calculate_formulat(x):
    y = (x * x) + (7 * x) - (77 * x) + (777 * x)
    return str.join("\n", [f"y = xx + 7x - 77x + 777x where x = {x}",
                           f"y = {x*x} + {7*x} - {77*x} + {777*x}",
                           f"y = {y}"])


print(calculate_formulat(int(input("Enter a number: "))))
