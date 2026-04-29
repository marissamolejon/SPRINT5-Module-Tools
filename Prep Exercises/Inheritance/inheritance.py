"""
Exercise: Inheritance
Sprint 5 Prep
 
Covers two exercises from the Inheritance section:
 
1. Reading + running the ImmutableNumberList / SortedImmutableNumberList example
   (with the crashing line commented out and explained)
 
2. "Play computer" with the Parent / Child example
"""
 
# =============================================================================
# Exercise 1: ImmutableNumberList and SortedImmutableNumberList
# =============================================================================
 
from typing import Iterable, Optional
 
 
class ImmutableNumberList:
    def __init__(self, elements: Iterable[int]):
        # Copy so external mutations don't affect us
        self.elements = [element for element in elements]
 
    def first(self) -> Optional[int]:
        if not self.elements:
            return None
        return self.elements[0]
 
    def last(self) -> Optional[int]:
        if not self.elements:
            return None
        return self.elements[-1]
 
    def length(self) -> int:
        return len(self.elements)
 
    def largest(self) -> Optional[int]:
        # Scans every element - O(n)
        if not self.elements:
            return None
        largest = self.elements[0]
        for element in self.elements:
            if element > largest:
                largest = element
        return largest
 
 
class SortedImmutableNumberList(ImmutableNumberList):
    def __init__(self, elements: Iterable[int]):
        # Extra work upfront: sort the elements
        super().__init__(sorted(elements))
 
    def largest(self) -> Optional[int]:
        # Override: because we're sorted, largest is always the last element - O(1)
        return self.last()
 
    def max_gap_between_values(self) -> Optional[int]:
        if not self.elements:
            return None
        previous_element = None
        max_gap = -1
        for element in self.elements:
            if previous_element is not None:
                gap = element - previous_element
                if gap > max_gap:
                    max_gap = gap
            previous_element = element
        return max_gap
 
 
values = SortedImmutableNumberList([1, 19, 7, 13, 4])
print(values.largest())               # 19  (overridden method - just reads last element)
print(values.max_gap_between_values()) # 6  (sorted: [1,4,7,13,19] -> max gap is 13->19 = 6)
 
unsorted_values = ImmutableNumberList([1, 19, 7, 13, 4])
print(unsorted_values.largest())      # 19  (original method - scans all elements)
 
# unsorted_values.max_gap_between_values()
# ^^^ This would raise AttributeError: 'ImmutableNumberList' has no attribute 'max_gap_between_values'
# Inheritance flows downward only: Child gets Parent's methods, NOT the other way around.
print("(max_gap_between_values only exists on SortedImmutableNumberList, not ImmutableNumberList)")
 
 
# =============================================================================
# Exercise 2: Play computer with Parent / Child
# =============================================================================
#
# PREDICTIONS (written before running):
#
# person1 = Child("Elizaveta", "Alekseeva")
#
# person1.get_name()
#   -> Child inherits get_name from Parent -> "Elizaveta Alekseeva"
#
# person1.get_full_name()
#   -> previous_last_names is [] -> suffix = "" -> "Elizaveta Alekseeva"
#
# person1.change_last_name("Tyurina")
#   -> appends "Alekseeva" to previous_last_names, sets last_name = "Tyurina"
#
# person1.get_name()
#   -> last_name is now "Tyurina" -> "Elizaveta Tyurina"
#
# person1.get_full_name()
#   -> previous_last_names[0] = "Alekseeva" -> "Elizaveta Tyurina (née Alekseeva)"
#
# person2 = Parent("Elizaveta", "Alekseeva")
#
# person2.get_name()
#   -> "Elizaveta Alekseeva"
#
# person2.get_full_name()
#   -> AttributeError: Parent has no attribute 'get_full_name'
#
# person2.change_last_name("Tyurina")
#   -> AttributeError: Parent has no attribute 'change_last_name'
 
 
class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
 
    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
 
 
class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: list[str] = []
 
    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name
 
    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"
 
 
print("\n--- Play computer ---")
person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())        # Elizaveta Alekseeva
print(person1.get_full_name())   # Elizaveta Alekseeva
person1.change_last_name("Tyurina")
print(person1.get_name())        # Elizaveta Tyurina
print(person1.get_full_name())   # Elizaveta Tyurina (née Alekseeva)
 
person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())        # Elizaveta Alekseeva
 
# These would raise AttributeError - Parent does not inherit Child's methods:
# print(person2.get_full_name())
# person2.change_last_name("Tyurina")
print("(person2.get_full_name() and person2.change_last_name() raise AttributeError - "
      "Parent does not have these methods, only Child does)")
 