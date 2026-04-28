"""
Exercise: Classes and Objects
Sprint 5 Prep
 
Demonstrates:
- Defining a class with __init__
- Using mypy-friendly type annotations
- Writing a free function and a method that takes a Person
- Accessing a non-existent property causes a mypy error (demonstrated in comment)
"""
 
import datetime
 
 
class Person:
    def __init__(self, name: str, date_of_birth: datetime.date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system
 
    def is_adult(self) -> bool:
        """Return True if the person is 18 or older."""
        today = datetime.date.today()
        age = (
            today.year - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
        return age >= 18
 
 
def greet(person: Person) -> str:
    """A free function that takes a Person and returns a greeting string."""
    return f"Hello, {person.name}!"
 
 
# --- Demonstration ---
 
imran = Person("Imran", datetime.date(2002, 5, 14), "Ubuntu")
eliza = Person("Eliza", datetime.date(1990, 3, 22), "Arch Linux")
 
print(greet(imran))
print(greet(eliza))
 
print(f"Is {imran.name} an adult? {imran.is_adult()}")
print(f"Is {eliza.name} an adult? {eliza.is_adult()}")
 
# The line below would cause a mypy error: Person has no attribute 'address'
# print(imran.address)
 