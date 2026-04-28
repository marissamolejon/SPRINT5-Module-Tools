"""
Unit tests for exercise_inheritance.py
Tests: ImmutableNumberList, SortedImmutableNumberList, Parent, Child
"""
 
import unittest
from inheritance import (
    ImmutableNumberList,
    SortedImmutableNumberList,
    Parent,
    Child,
)
 
 
# =============================================================================
# ImmutableNumberList
# =============================================================================
 
class TestImmutableNumberList(unittest.TestCase):
 
    def test_first_returns_first_element(self):
        lst = ImmutableNumberList([3, 1, 4, 1, 5])
        self.assertEqual(lst.first(), 3)
 
    def test_first_returns_none_for_empty(self):
        lst = ImmutableNumberList([])
        self.assertIsNone(lst.first())
 
    def test_last_returns_last_element(self):
        lst = ImmutableNumberList([3, 1, 4, 1, 5])
        self.assertEqual(lst.last(), 5)
 
    def test_last_returns_none_for_empty(self):
        lst = ImmutableNumberList([])
        self.assertIsNone(lst.last())
 
    def test_length(self):
        lst = ImmutableNumberList([1, 2, 3])
        self.assertEqual(lst.length(), 3)
 
    def test_length_empty(self):
        lst = ImmutableNumberList([])
        self.assertEqual(lst.length(), 0)
 
    def test_largest_finds_max(self):
        lst = ImmutableNumberList([1, 19, 7, 13, 4])
        self.assertEqual(lst.largest(), 19)
 
    def test_largest_single_element(self):
        lst = ImmutableNumberList([42])
        self.assertEqual(lst.largest(), 42)
 
    def test_largest_returns_none_for_empty(self):
        lst = ImmutableNumberList([])
        self.assertIsNone(lst.largest())
 
    def test_does_not_mutate_original_list(self):
        original = [3, 1, 4]
        lst = ImmutableNumberList(original)
        original.append(99)
        self.assertEqual(lst.length(), 3)
 
    def test_does_not_have_max_gap_method(self):
        lst = ImmutableNumberList([1, 2, 3])
        self.assertFalse(hasattr(lst, "max_gap_between_values"))
 
 
# =============================================================================
# SortedImmutableNumberList
# =============================================================================
 
class TestSortedImmutableNumberList(unittest.TestCase):
 
    def test_elements_are_sorted_on_creation(self):
        lst = SortedImmutableNumberList([1, 19, 7, 13, 4])
        self.assertEqual(lst.elements, [1, 4, 7, 13, 19])
 
    def test_largest_returns_max(self):
        lst = SortedImmutableNumberList([1, 19, 7, 13, 4])
        self.assertEqual(lst.largest(), 19)
 
    def test_largest_empty_returns_none(self):
        lst = SortedImmutableNumberList([])
        self.assertIsNone(lst.largest())
 
    def test_max_gap_between_values(self):
        # sorted: [1, 4, 7, 13, 19] -> gaps: 3, 3, 6, 6 -> max = 6
        lst = SortedImmutableNumberList([1, 19, 7, 13, 4])
        self.assertEqual(lst.max_gap_between_values(), 6)
 
    def test_max_gap_single_element_returns_negative_one(self):
        lst = SortedImmutableNumberList([5])
        self.assertEqual(lst.max_gap_between_values(), -1)
 
    def test_max_gap_empty_returns_none(self):
        lst = SortedImmutableNumberList([])
        self.assertIsNone(lst.max_gap_between_values())
 
    def test_inherits_first_and_last_from_parent(self):
        lst = SortedImmutableNumberList([5, 2, 8])
        # After sorting: [2, 5, 8]
        self.assertEqual(lst.first(), 2)
        self.assertEqual(lst.last(), 8)
 
    def test_inherits_length_from_parent(self):
        lst = SortedImmutableNumberList([5, 2, 8])
        self.assertEqual(lst.length(), 3)
 
 
# =============================================================================
# Parent
# =============================================================================
 
class TestParent(unittest.TestCase):
 
    def test_get_name_returns_full_name(self):
        p = Parent("Elizaveta", "Alekseeva")
        self.assertEqual(p.get_name(), "Elizaveta Alekseeva")
 
    def test_does_not_have_get_full_name(self):
        p = Parent("Elizaveta", "Alekseeva")
        self.assertFalse(hasattr(p, "get_full_name"))
 
    def test_does_not_have_change_last_name(self):
        p = Parent("Elizaveta", "Alekseeva")
        self.assertFalse(hasattr(p, "change_last_name"))
 
 
# =============================================================================
# Child
# =============================================================================
 
class TestChild(unittest.TestCase):
 
    def test_inherits_get_name(self):
        c = Child("Elizaveta", "Alekseeva")
        self.assertEqual(c.get_name(), "Elizaveta Alekseeva")
 
    def test_get_full_name_no_previous_names(self):
        c = Child("Elizaveta", "Alekseeva")
        self.assertEqual(c.get_full_name(), "Elizaveta Alekseeva")
 
    def test_change_last_name_updates_name(self):
        c = Child("Elizaveta", "Alekseeva")
        c.change_last_name("Tyurina")
        self.assertEqual(c.get_name(), "Elizaveta Tyurina")
 
    def test_change_last_name_stores_previous(self):
        c = Child("Elizaveta", "Alekseeva")
        c.change_last_name("Tyurina")
        self.assertIn("Alekseeva", c.previous_last_names)
 
    def test_get_full_name_after_name_change(self):
        c = Child("Elizaveta", "Alekseeva")
        c.change_last_name("Tyurina")
        self.assertEqual(c.get_full_name(), "Elizaveta Tyurina (née Alekseeva)")
 
    def test_get_full_name_shows_original_maiden_name_after_multiple_changes(self):
        c = Child("Elizaveta", "Alekseeva")
        c.change_last_name("Tyurina")
        c.change_last_name("Ivanova")
        # née should still show the *first* previous name
        self.assertEqual(c.get_full_name(), "Elizaveta Ivanova (née Alekseeva)")
 
    def test_previous_last_names_starts_empty(self):
        c = Child("Elizaveta", "Alekseeva")
        self.assertEqual(c.previous_last_names, [])
 
 
if __name__ == "__main__":
    unittest.main()
 