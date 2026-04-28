"""
Exercise: Enums
Sprint 5 Prep
 
Demonstrates:
- Defining an Enum for operating systems
- Converting user string input to an enum early (fail-fast pattern)
- Using enums in type annotations with @dataclass
- Outputting errors to stderr and exiting with non-zero code on bad input
"""
 
import sys
from dataclasses import dataclass
from enum import Enum
from typing import List
 
 
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
 
 
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem
 
 
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
 
 
# The library's laptops
LIBRARY_LAPTOPS: List[Laptop] = [
    Laptop(id=1, manufacturer="Dell",  model="XPS",     screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell",  model="XPS",     screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell",  model="XPS",     screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="MacBook", screen_size_in_inches=15, operating_system=OperatingSystem.MACOS),
]
 
 
def parse_operating_system(raw: str) -> OperatingSystem:
    """Convert a string to an OperatingSystem enum, or exit with an error."""
    normalised = raw.strip()
    for os in OperatingSystem:
        if os.value.lower() == normalised.lower():
            return os
    valid = ", ".join(os.value for os in OperatingSystem)
    print(f"Error: '{raw}' is not a recognised operating system. Valid options: {valid}", file=sys.stderr)
    sys.exit(1)
 
 
def parse_age(raw: str) -> int:
    """Convert a string to an int age, or exit with an error."""
    try:
        age = int(raw.strip())
        if age < 0:
            raise ValueError
        return age
    except ValueError:
        print(f"Error: '{raw}' is not a valid age.", file=sys.stderr)
        sys.exit(1)
 
 
def count_laptops_for_os(laptops: List[Laptop], os: OperatingSystem) -> int:
    return sum(1 for l in laptops if l.operating_system == os)
 
 
def main() -> None:
    print("=== Library Laptop Allocation ===\n")
 
    name = input("Enter your name: ").strip()
    age = parse_age(input("Enter your age: "))
 
    print(f"\nAvailable operating systems: {', '.join(os.value for os in OperatingSystem)}")
    preferred_os = parse_operating_system(input("Enter your preferred operating system: "))
 
    person = Person(name=name, age=age, preferred_operating_system=preferred_os)
 
    # Count laptops for the person's preferred OS
    preferred_count = count_laptops_for_os(LIBRARY_LAPTOPS, person.preferred_operating_system)
    print(f"\nHello {person.name}! The library has {preferred_count} laptop(s) running {person.preferred_operating_system.value}.")
 
    # Find any OS with more laptops available
    best_os = max(OperatingSystem, key=lambda os: count_laptops_for_os(LIBRARY_LAPTOPS, os))
    best_count = count_laptops_for_os(LIBRARY_LAPTOPS, best_os)
 
    if best_os != person.preferred_operating_system and best_count > preferred_count:
        print(
            f"Tip: If you're willing to use {best_os.value}, there are {best_count} laptops "
            f"available — more than {preferred_count} for {person.preferred_operating_system.value}. "
            f"You'd have a better chance of getting one!"
        )
 
 
if __name__ == "__main__":
    main()
 