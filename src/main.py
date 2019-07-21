import random

import src.BinManager as BinManager

# Some constants and default values
min_int = 20001
max_int = 380000
bin_size = 36000
range_size = 1000
num_bins = 10


# Main entry point. Create the bins. Generate the random numbers and bin them
# Output the results into a csv file.
def main():
    show_banner()

    n_bins = read_int_input("Please enter the number of bins to create: ")
    rand_num_cnt = read_int_input("Please enter the count of random numbers to generate: ")
    file_name = input(
        "Please enter the file name to store the output: (an existing file with the same name will be overwritten)")

    if n_bins < 1:
        n_bins = num_bins

    bin_manager = BinManager.BinManager(n_bins, min_int, max_int, bin_size)

    if rand_num_cnt < 1:
        rand_num_cnt = range_size

    for x in range(rand_num_cnt):
        res = random.randint(min_int, max_int)
        bin_manager.bin(res)

    bin_manager.print_me()
    bin_manager.output_me(file_name)


def read_int_input(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("The input must be an integer.  Please enter a new value.")
            continue
        else:
            return userInput


def read_string_input(message):
    while True:
        userInput = input(message)
        if userInput.__len__() == 0:
            print("Please enter a file name: ")
            continue
        else:
            return userInput


def show_banner():
    with open("../resources/banner.txt") as f:
        line = f.read()
        print(line)


if __name__ == "__main__":
    main()
