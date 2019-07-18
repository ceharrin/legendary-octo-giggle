import src.Bin as Bin


# A class for managing bins.  Bins are stored in an array upon initialization.
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
        return self.bins

    def bin(self, res):
        for idx in range(self.num_bins):
            b = self.bins[idx]
            if b.is_in_bin(res):
                b.bincrement()
                break

    def print_me(self):
        for idx in range(self.num_bins):
            b = self.bins[idx]
            b.print_me()

    def output_me(self):
        f = open("../output/histo.csv", 'w')
        f.write("Bindex,Lower,Upper,Bin count\n")
        for idx in range(self.num_bins):
            b = self.bins[idx]
            b.output_me(f)
