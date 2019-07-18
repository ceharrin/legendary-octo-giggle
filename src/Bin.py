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
        print("Bin lower bound: " + str(self.lower_bound))
        print("Bin upper bound: " + str(self.upper_bound))
        print("Bin count: " + str(self.count))