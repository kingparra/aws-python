#!/usr/bin/env python3
# Assignment 1 - Ask for an age (int) and convert it into months, days, and hours


def age_calc(y):
    age_months = y * 12
    age_days = y * 365
    age_hours = age_days * 24
    print(f"{y} years = " +
          f"{age_months} months = " +
          f"{age_days} days = "
          f"{age_hours} hours")


age_calc(int(input("Enter your age in years: ")))
