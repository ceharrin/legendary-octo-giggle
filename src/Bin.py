# A simple representation of a bin.  Has index, bin count and lower and upper bounds
class Bin:

    def __init__(self, bin_num, lower_bound, upper_bound):
        self.bindex = bin_num
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.count = 0

    # Is the given value within my lower and upper bound?
    def is_in_bin(self, random_int):
        return self.lower_bound <= random_int <= self.upper_bound

    # Increment my count
    def bincrement(self):
        self.count += 1

    # Output a string summary of me to the console
    def print_me(self):
        print("Bindex: " + str(self.bindex))
        print("\tLower bound: " + str(self.lower_bound))
        print("\tUpper bound: " + str(self.upper_bound))
        print("\tBinventory count: " + str(self.count) + "\n")

    # Output my data to the given file
    def output_me(self, file):
        file.write(str(self.bindex + 1) + "," + str(self.count) + "\n")
