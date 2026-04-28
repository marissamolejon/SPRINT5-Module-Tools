"""
Unit tests for exercise_generics.py
Tests: Person (with children), find_possible_laptops with List[str] preferred_operating_systems
"""
 
import unittest
from generics import Person, PersonWithOS, Laptop, find_possible_laptops
 
 
class TestPersonWithChildren(unittest.TestCase):
 
    def test_person_with_no_children(self):
        p = Person(name="Fatma", age=8, children=[])
        self.assertEqual(p.children, [])
 
    def test_person_stores_children(self):
        fatma = Person(name="Fatma", age=8, children=[])
        aisha = Person(name="Aisha", age=5, children=[])
        imran = Person(name="Imran", age=38, children=[fatma, aisha])
        self.assertEqual(len(imran.children), 2)
        self.assertEqual(imran.children[0].name, "Fatma")
        self.assertEqual(imran.children[1].name, "Aisha")
 
    def test_children_have_correct_ages(self):
        fatma = Person(name="Fatma", age=8, children=[])
        imran = Person(name="Imran", age=38, children=[fatma])
        self.assertEqual(imran.children[0].age, 8)
 
 
class TestFindPossibleLaptops(unittest.TestCase):
 
    def setUp(self):
        self.laptops = [
            Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
            Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
            Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
            Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
        ]
 
    def test_finds_matching_laptops_for_single_os(self):
        person = PersonWithOS(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"])
        result = find_possible_laptops(self.laptops, person)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
 
    def test_finds_multiple_matches(self):
        person = PersonWithOS(name="Imran", age=22, preferred_operating_systems=["Ubuntu"])
        result = find_possible_laptops(self.laptops, person)
        self.assertEqual(len(result), 2)
        ids = [l.id for l in result]
        self.assertIn(2, ids)
        self.assertIn(3, ids)
 
    def test_finds_matches_across_multiple_preferred_os(self):
        person = PersonWithOS(name="Imran", age=22, preferred_operating_systems=["Ubuntu", "Arch Linux"])
        result = find_possible_laptops(self.laptops, person)
        self.assertEqual(len(result), 3)
 
    def test_no_match_returns_empty_list(self):
        person = PersonWithOS(name="Nobody", age=25, preferred_operating_systems=["Windows"])
        result = find_possible_laptops(self.laptops, person)
        self.assertEqual(result, [])
 
    def test_empty_laptop_list_returns_empty(self):
        person = PersonWithOS(name="Imran", age=22, preferred_operating_systems=["Ubuntu"])
        result = find_possible_laptops([], person)
        self.assertEqual(result, [])
 
    def test_empty_preferred_os_returns_empty(self):
        person = PersonWithOS(name="Imran", age=22, preferred_operating_systems=[])
        result = find_possible_laptops(self.laptops, person)
        self.assertEqual(result, [])
 
 
if __name__ == "__main__":
    unittest.main()
 