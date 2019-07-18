from unittest import TestCase

from src import BinManager


class TestBinManager(TestCase):

    def test_binitialize(self):
        bin_manager = BinManager.BinManager(3, 1, 30, 10)

        self.assertTrue(bin_manager.bins.__len__() == 3)

        self.assertTrue(bin_manager.bins[0].lower_bound == 1)
        self.assertTrue(bin_manager.bins[0].upper_bound == 10)

        self.assertTrue(bin_manager.bins[1].lower_bound == 11)
        self.assertTrue(bin_manager.bins[1].upper_bound == 20)

        self.assertTrue(bin_manager.bins[2].lower_bound == 21)
        self.assertTrue(bin_manager.bins[2].upper_bound == 30)

    def test_bin(self):
        bin_manager = BinManager.BinManager(3, 1, 30, 10)

        bin_manager.bin(5)
        bin_manager.bin(5)
        bin_manager.bin(15)
        bin_manager.bin(25)
        bin_manager.bin(35)

        self.assertTrue(bin_manager.bins[0].count == 2)
        self.assertTrue(bin_manager.bins[1].count == 1)
        self.assertTrue(bin_manager.bins[2].count == 1)