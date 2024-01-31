#!/usr/bin/env python3
# Assignment 1 - Read a csv file and return a list of lines
from pprint import pp


def file_to_lines_list(fname):
    with open(fname) as file:
        lines_list = file.readlines()
        return lines_list


pp(file_to_lines_list("cars.csv"))
