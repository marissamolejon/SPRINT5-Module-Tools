"""
Exercise: Generics
Sprint 5 Prep
 
The original code had a bug: it tried to print child.age, but Person has no age field.
With List["Person"] as the type for children, mypy can detect this.
 
Fix: give each child an explicit age field (or date_of_birth).
Here we use a simple `age: int` field so the print statement on line 17 works as-is.
"""
 
import datetime
from dataclasses import dataclass
from typing import List
 
 
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: List["Person"]
 
 
# --- Demonstration ---
 
fatma = Person(name="Fatma", age=8, children=[])
aisha = Person(name="Aisha", age=5, children=[])
 
imran = Person(name="Imran", age=38, children=[fatma, aisha])
 
 
def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")
 
 
print_family_tree(imran)
 
 
# --- Type-guided refactoring: preferred_operating_systems as a list ---
 
@dataclass(frozen=True)
class PersonWithOS:
    name: str
    age: int
    preferred_operating_systems: List[str]  # renamed from preferred_operating_system
 
 
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str
 
 
def find_possible_laptops(laptops: List[Laptop], person: PersonWithOS) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system in person.preferred_operating_systems:  # changed == to `in`
            possible_laptops.append(laptop)
    return possible_laptops
 
 
people_with_os = [
    PersonWithOS(name="Imran", age=22, preferred_operating_systems=["Ubuntu", "Arch Linux"]),
    PersonWithOS(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"]),
]
 
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]
 
for person in people_with_os:
    possible = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {[l.id for l in possible]}")
 