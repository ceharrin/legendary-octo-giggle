import src.Bin as Bin


# A class for managing bins.
# Initialize the array of bins using the provided input
class BinManager:

    def __init__(self, num_bins, min_bin_idx, max_bin_idx, bin_size):
        self.bins = []
        self.num_bins = num_bins
        self.min_int = min_bin_idx
        self.max_int = max_bin_idx
        self.bin_size = bin_size
        self.binitialize()

    # Create the bins used to track the randomly generated numbers
    def binitialize(self):
        curr_bin_min = self.min_int

        for y in range(self.num_bins):
            b = Bin.Bin(y, curr_bin_min, curr_bin_min + (self.bin_size - 1))
            self.bins.append(b)
            curr_bin_min += self.bin_size

    # Bin the random numnber. In this case just increment the count for the
    # bin
    def bin(self, res):
        for idx in range(self.num_bins):
            b = self.bins[idx]
            if b.is_in_bin(res):
                b.bincrement()
                break

    # Output a string summary of me to the console
    def print_me(self):
        for idx in range(self.num_bins):
            b = self.bins[idx]
            b.print_me()

    # Output my data to a file
    def output_me(self, file_name):
        f = open("../output/" + file_name + ".csv", 'w')
        f.write("Bindex,Bin count\n")
        for idx in range(self.num_bins):
            b = self.bins[idx]
            b.output_me(f)
