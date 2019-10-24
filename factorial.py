#!/usr/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Oct 2019
# This program display factorial of user integer


def main():
    # this function display factorial of user integer
    loop_counter = 1
    result = 1

    # input
    positive_integer = int(input("Enter the number you use factorial: "))
    print("")

    # process & output
    while loop_counter <= positive_integer:
        result = loop_counter * result
        loop_counter = loop_counter + 1
    print("{0}!(facotorial) is {1}".format(positive_integer, result))


if __name__ == "__main__":
    main()
