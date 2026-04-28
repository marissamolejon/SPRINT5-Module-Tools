"""
Unit tests for exercise_types_mypy.py
Tests: open_account, sum_balances, format_pence_as_string
"""
 
import unittest
from types_mypy import open_account, sum_balances, format_pence_as_string
 
 
class TestOpenAccount(unittest.TestCase):
 
    def test_adds_new_account_to_empty_dict(self):
        balances = {}
        open_account(balances, "Alice", 500)
        self.assertEqual(balances, {"Alice": 500})
 
    def test_adds_multiple_accounts(self):
        balances = {}
        open_account(balances, "Alice", 500)
        open_account(balances, "Bob", 1000)
        self.assertEqual(balances["Alice"], 500)
        self.assertEqual(balances["Bob"], 1000)
 
    def test_overwrites_existing_account(self):
        balances = {"Alice": 100}
        open_account(balances, "Alice", 999)
        self.assertEqual(balances["Alice"], 999)
 
    def test_account_with_zero_balance(self):
        balances = {}
        open_account(balances, "Charlie", 0)
        self.assertEqual(balances["Charlie"], 0)
 
 
class TestSumBalances(unittest.TestCase):
 
    def test_sums_single_account(self):
        result = sum_balances({"Alice": 500})
        self.assertEqual(result, 500)
 
    def test_sums_multiple_accounts(self):
        result = sum_balances({"Sima": 700, "Linn": 545, "Georg": 831})
        self.assertEqual(result, 2076)
 
    def test_empty_dict_returns_zero(self):
        result = sum_balances({})
        self.assertEqual(result, 0)
 
    def test_accounts_with_zero_balances(self):
        result = sum_balances({"Alice": 0, "Bob": 0})
        self.assertEqual(result, 0)
 
 
class TestFormatPenceAsString(unittest.TestCase):
 
    def test_zero_pence(self):
        self.assertEqual(format_pence_as_string(0), "0p")
 
    def test_less_than_100_pence(self):
        self.assertEqual(format_pence_as_string(99), "99p")
 
    def test_exactly_100_pence_is_one_pound(self):
        self.assertEqual(format_pence_as_string(100), "£1.00")
 
    def test_whole_pounds(self):
        self.assertEqual(format_pence_as_string(500), "£5.00")
 
    def test_pounds_and_pence(self):
        self.assertEqual(format_pence_as_string(913), "£9.13")
 
    def test_pence_with_leading_zero(self):
        # 705p = £7.05 — pence part should be padded to 2 digits
        self.assertEqual(format_pence_as_string(705), "£7.05")
 
    def test_large_amount(self):
        self.assertEqual(format_pence_as_string(3702), "£37.02")
 
 
if __name__ == "__main__":
    unittest.main()
 