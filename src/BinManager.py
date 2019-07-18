import src.Bin as Bin


# A simple class for managing bins
class BinManager:

    # Binitialize...
    def __init__(self, num_bins, min_bin_idx, max_bin_idx, bin_size):
        self.bins = []
        self.num_bins = num_bins
        self.min_int = min_bin_idx
        self.max_int = max_bin_idx
        self.bin_size = bin_size
        self.create_bins()

    # Create the bins used to track the randomly generated numbers
    def create_bins(self):
        curr_bin_min = self.min_int

        for y in range(self.num_bins):
            b = Bin.Bin(y, curr_bin_min, curr_bin_min + self.bin_size)
            self.bins.append(b)
            b.print_me()
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
        f = open("histo.txt", 'w')
        for idx in range(self.num_bins):
            b = self.bins[idx]
            b.output_me(f)