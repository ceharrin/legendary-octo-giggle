import random

import src.BinManager as BinManager

# Some constants and default values
min_int = 20001
max_int = 380000
bin_size = 36000
range_size = 1000
num_bins = 10


# Main entry point. Prompt for user input and then create the bins based on the provided input.
# Generate the random numbers and bin them.
# Output the results into a csv file that can be loaded into Excel.
#
# This is a naive implementation.  Inputs are not constrained beyond int type checking and
# string length.  Bin sizes are calculated based upon homework specification and not dynamically
# determined.
#
# File output is not verified.  Basic unit tests are available in ../test/
#
# Author: Chris Harrington
# July 2019
# CSC 540 Homework assignment #3
# Histograms
def main():
    show_banner()

    n_bins = read_int_input("Please enter the number of bins to create: ")
    rand_num_cnt = read_int_input("Please enter the count of random numbers to generate: ")
    file_name = input(
        "Please enter the file name to store the output: (an existing file with the same name will be overwritten)")

    # Default to constant if needed
    if n_bins < 1:
        n_bins = num_bins

    # Create an instance of the BinManager using the inputs.
    bin_manager = BinManager.BinManager(n_bins, min_int, max_int, bin_size)

    # Default to constant if needed
    if rand_num_cnt < 1:
        rand_num_cnt = range_size

    # Generate a random int N times and bin it
    for x in range(rand_num_cnt):
        res = random.randint(min_int, max_int)
        bin_manager.bin(res)

    # Output summary data to console and then write the data out in a csv file
    bin_manager.print_me()
    bin_manager.output_me(file_name)


# Read an int from input.  Little validation performed other than
# throwing an error if the user enters a non-int.  Use can re-enter value
def read_int_input(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("The input must be an integer.  Please enter a new value.")
            continue
        else:
            return userInput


# Read a string from input.  Little validation performed other than
# checking the string length.  User can re-enter data
def read_string_input(message):
    while True:
        userInput = input(message)
        if userInput.__len__() == 0:
            print("Please enter a file name: ")
            continue
        else:
            return userInput


# A fun banner is displayed when the program runs
def show_banner():
    with open("../resources/banner.txt") as f:
        line = f.read()
        print(line)


if __name__ == "__main__":
    main()
