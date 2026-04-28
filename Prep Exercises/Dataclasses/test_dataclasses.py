"""
Unit tests for exercise_dataclasses.py
Tests: Person dataclass — equality, repr, is_adult, immutability
"""
 
import datetime
import unittest
from exercise_dataclasses import Person

 
class TestPersonEquality(unittest.TestCase):
 
    def test_two_identical_persons_are_equal(self):
        p1 = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        p2 = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertEqual(p1, p2)
 
    def test_different_names_are_not_equal(self):
        p1 = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        p2 = Person("Eliza", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertNotEqual(p1, p2)
 
    def test_different_dob_are_not_equal(self):
        p1 = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        p2 = Person("Imran", datetime.date(2002, 5, 15), "Ubuntu")
        self.assertNotEqual(p1, p2)
 
    def test_different_os_are_not_equal(self):
        p1 = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        p2 = Person("Imran", datetime.date(2002, 5, 14), "Arch Linux")
        self.assertNotEqual(p1, p2)
 
 
class TestPersonRepr(unittest.TestCase):
 
    def test_repr_contains_name(self):
        p = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertIn("Imran", repr(p))
 
    def test_repr_contains_class_name(self):
        p = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertIn("Person", repr(p))
 
 
class TestPersonIsAdult(unittest.TestCase):
 
    def test_adult_returns_true(self):
        p = Person("Eliza", datetime.date(1990, 3, 22), "Arch Linux")
        self.assertTrue(p.is_adult())
 
    def test_child_returns_false(self):
        p = Person("Kid", datetime.date(2020, 1, 1), "Ubuntu")
        self.assertFalse(p.is_adult())
 
    def test_exactly_18_today_is_adult(self):
        today = datetime.date.today()
        dob = datetime.date(today.year - 18, today.month, today.day)
        p = Person("Alex", dob, "Ubuntu")
        self.assertTrue(p.is_adult())
 
 
class TestPersonImmutability(unittest.TestCase):
 
    def test_cannot_modify_frozen_dataclass(self):
        p = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        with self.assertRaises(Exception):
            p.name = "Someone Else"  # type: ignore
 
 
if __name__ == "__main__":
    unittest.main()
 