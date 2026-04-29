"""
Exercise: Dataclasses
Sprint 5 Prep
 
Demonstrates:
- Using @dataclass(frozen=True) to create a value type
- Automatic __init__, __repr__, __eq__ generation
- Using datetime.date for date of birth instead of int age
- Adding a custom method (is_adult) to a dataclass
"""
 
import datetime
from dataclasses import dataclass
 
 
@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: datetime.date
    preferred_operating_system: str
 
    def is_adult(self) -> bool:
        """Return True if the person is 18 or older based on date of birth."""
        today = datetime.date.today()
        age = (
            today.year - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
        return age >= 18
 
 
# --- Demonstration ---
 
imran = Person(
    name="Imran",
    date_of_birth=datetime.date(2002, 5, 14),
    preferred_operating_system="Ubuntu",
)
imran2 = Person(
    name="Imran",
    date_of_birth=datetime.date(2002, 5, 14),
    preferred_operating_system="Ubuntu",
)
eliza = Person(
    name="Eliza",
    date_of_birth=datetime.date(1990, 3, 22),
    preferred_operating_system="Arch Linux",
)
 
# @dataclass generates a nice __repr__
print(imran)
 
# @dataclass generates __eq__ based on field values
print(f"imran == imran2: {imran == imran2}")   # True
print(f"imran == eliza: {imran == eliza}")     # False
 
print(f"Is {imran.name} an adult? {imran.is_adult()}")
print(f"Is {eliza.name} an adult? {eliza.is_adult()}")
 