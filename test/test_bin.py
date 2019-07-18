from unittest import TestCase

from src import Bin


class TestBin(TestCase):
    def test_init(self):
        b = Bin.Bin(1, 100, 250)

        self.assertTrue(b.count == 0)
        self.assertTrue(b.lower_bound == 100)
        self.assertTrue(b.upper_bound == 250)

    def test_bincrement(self):
        b = Bin.Bin(1, 100, 250)

        self.assertTrue(b.count == 0)
        b.bincrement()
        self.assertTrue(b.count == 1)

    def test_is_in_bin(self):
        b = Bin.Bin(1, 100, 250)

        self.assertTrue(b.is_in_bin(200))
        self.assertFalse(b.is_in_bin(300))
