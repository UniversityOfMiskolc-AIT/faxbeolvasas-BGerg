import unittest
from faxreader.core.handle_data import *


class MyTestCase(unittest.TestCase):

    def test_get_digit_with_valid_input(self):
        test_account_one = [
            "    _  _     _  _  _  _  _ ",
            "  | _| _||_||_ |_   ||_||_|",
            "  ||_  _|  | _||_|  ||_| _|",
            "                           "
        ]
        for j in range(1):
            for i in range(1, 10):
                self.assertEqual(str(i), get_digit(j, i, test_account_one))

        test_account_two = [
            "    _  _     _  _  _  _  _ ",
            "  | _| _||_||_ |_   ||_||_|",
            "  ||_  _|  | _||_|  ||_| _|",
            "                           ",
            "    _  _     _  _  _  _  _ ",
            "  | _| _||_||_ |_   ||_||_|",
            "  ||_  _|  | _||_|  ||_| _|",
            "                           "
        ]
        for j in range(2):
            for i in range(1, 10):
                self.assertEqual(str(i), get_digit(j, i, test_account_two))

    def test_get_digit_with_invalid_input(self):
        test_account = [
            "\ /       fg             5 ",
            " X     dsd        @ä       ",
            "/ \ @&                #    "
        ]
        for j in range(1):
            for i in range(1, 10):
                self.assertEqual("?", get_digit(j, i, test_account))

    def test_checksum_ERR_suffix(self):
        self.assertEqual(check_account_number("664371495"), "664371495 ERR")

    def test_checksum_no_suffix(self):
        self.assertEqual(check_account_number("000000000"), "000000000")

    def test_checksum_ILL_suffix(self):
        self.assertEqual(check_account_number("664371?95"), "664371?95 ILL")

    def test_get_number_of_accounts_odd(self):
        lines = [
            "line1",
            "line2",
            "line3",
            "line4",
            "line5"
        ]
        self.assertEqual(1,get_number_of_accounts(lines))

        lines = [
            "line1",
            "line2",
            "line3",
            "line4",
            "line5",
            "line6",
            "line7",
            "line8",
            "line9"
        ]
        self.assertEqual(2,get_number_of_accounts(lines))

    def test_get_number_of_accounts_even(self):

        lines_one = [
            "line1",
            "line2",
            "line3",
            "line4"
        ]
        self.assertEqual(1, get_number_of_accounts(lines_one))

        lines_two = [
            "line1",
            "line2",
            "line3",
            "line4",
            "line5",
            "line6",
            "line7",
            "line8",
        ]
        self.assertEqual(2, get_number_of_accounts(lines_two))
