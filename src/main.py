import random
import src.BinManager as BinManager

# Some constants for repeated use
min_int = 20001
max_int = 380000
bin_size = 36000
range_size = 1000
num_bins = 10


# Main entry point. Create the bins. Generate the random numbers and bin them
# Output the results into a csv file.
def main():
    bin_manager = BinManager.BinManager(num_bins, min_int, max_int, bin_size)

    for x in range(range_size):
        res = random.randint(min_int, max_int)
        bin_manager.bin(res)
        # print(res)

    bin_manager.print_me()
    bin_manager.output_me()


if __name__ == "__main__":
    main()
