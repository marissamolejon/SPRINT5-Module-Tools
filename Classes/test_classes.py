"""
Unit tests for exercise_classes.py
Tests: Person class (is_adult method), greet free function
"""
 
import datetime
import unittest
from unittest.mock import patch
from classes import Person, greet
 
 
class TestPersonIsAdult(unittest.TestCase):
 
    def test_clearly_over_18_is_adult(self):
        person = Person("Eliza", datetime.date(1990, 1, 1), "Ubuntu")
        self.assertTrue(person.is_adult())
 
    def test_clearly_under_18_is_not_adult(self):
        person = Person("Sam", datetime.date(2020, 1, 1), "Ubuntu")
        self.assertFalse(person.is_adult())
 
    def test_exactly_18_birthday_today_is_adult(self):
        today = datetime.date.today()
        dob = datetime.date(today.year - 18, today.month, today.day)
        person = Person("Alex", dob, "Ubuntu")
        self.assertTrue(person.is_adult())
 
    def test_one_day_before_18th_birthday_is_not_adult(self):
        today = datetime.date.today()
        # Birthday is tomorrow, so they haven't turned 18 yet
        birthday_tomorrow = today + datetime.timedelta(days=1)
        dob = datetime.date(today.year - 18, birthday_tomorrow.month, birthday_tomorrow.day)
        person = Person("Jordan", dob, "Ubuntu")
        self.assertFalse(person.is_adult())
 
 
class TestPersonAttributes(unittest.TestCase):
 
    def test_name_is_stored(self):
        person = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertEqual(person.name, "Imran")
 
    def test_date_of_birth_is_stored(self):
        dob = datetime.date(2002, 5, 14)
        person = Person("Imran", dob, "Ubuntu")
        self.assertEqual(person.date_of_birth, dob)
 
    def test_preferred_os_is_stored(self):
        person = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertEqual(person.preferred_operating_system, "Ubuntu")
 
 
class TestGreet(unittest.TestCase):
 
    def test_greet_returns_hello_with_name(self):
        person = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
        self.assertEqual(greet(person), "Hello, Imran!")
 
    def test_greet_different_name(self):
        person = Person("Eliza", datetime.date(1990, 3, 22), "Arch Linux")
        self.assertEqual(greet(person), "Hello, Eliza!")
 
 
if __name__ == "__main__":
    unittest.main()
 