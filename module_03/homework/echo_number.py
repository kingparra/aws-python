#!/usr/bin/env python3


def to_word(num):
    if num == 7:
        print("seven")
    elif num == 9:
        print("nine")
    elif num == 1:
        print("one")
    elif num == 10:
        print("ten")
    elif num == 5:
        print("five")
    else:
        print("bad guess")


def get_num():
    try:
        num = int(input("Guess a number: "))
    except ValueError:
        print("Invalid number. Must be an integer.")
    else:
        return num


def main():
    to_word(get_num())


if __name__ == "__main__":
    main()
