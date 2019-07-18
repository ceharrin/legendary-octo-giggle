# A simple representation of a bin.  Has number and lower and upper bound


class Bin:

    def __init__(self, bin_num, lower_bound, upper_bound):
        self.bindex = bin_num
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.count = 0

    def is_in_bin(self, random_int):
        return self.lower_bound <= random_int <= self.upper_bound

    def bincrement(self):
        self.count += 1

    def print_me(self):
        print("Bindex: " + str(self.bindex))
        print("\tLower bound: " + str(self.lower_bound))
        print("\tUpper bound: " + str(self.upper_bound))
        print("\tBinventory count: " + str(self.count))
        print()

    def output_me(self, file):
        file.write(str(self.count))