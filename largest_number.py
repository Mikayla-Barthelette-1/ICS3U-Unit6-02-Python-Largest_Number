#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program calculates the average of 10 random numbers

import random

import constants


def finding_largest_number(random_numbers):
    # this function finds the largest number

    largest_number = random_numbers[9]

    for loop_counter in range(0, 10):
        if random_numbers[loop_counter] > largest_number:
            largest_number = random_numbers[loop_counter]

    return largest_number


def main():
    # this function calls other functions

    random_numbers = []

    # input
    print("Here is a list of random numbers: ")
    print("")

    # process
    for loop_counter in range(0, 10):
        a_random_number = random.randint(1, 100)  # a number between 1 and 100
        random_numbers.append(a_random_number)
        loop_counter1 = loop_counter + 1
        print(
            "The random number {0} is: {1}".format(
                loop_counter1, random_numbers[loop_counter]
            )
        )

    biggest_number = finding_largest_number(random_numbers)

    print("")
    print("\nThe largest number is {0}.".format(biggest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
