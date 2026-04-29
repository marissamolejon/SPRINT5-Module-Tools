from allocate import allocate_laptops, Person, Laptop, OperatingSystem

# Test 1: Everyone gets their top choice
people = [
    Person("Alice", 25, tuple([OperatingSystem.UBUNTU, OperatingSystem.MACOS])),
    Person("Bob",   30, tuple([OperatingSystem.MACOS,  OperatingSystem.UBUNTU])),
]
laptops = [
    Laptop(1, "Apple", "MacBook Pro", 14.0, OperatingSystem.MACOS),
    Laptop(2, "Dell",  "XPS",         15.0, OperatingSystem.UBUNTU),
]
result = allocate_laptops(people, laptops)
assert result[people[0]].operating_system == OperatingSystem.UBUNTU, "Alice should get Ubuntu"
assert result[people[1]].operating_system == OperatingSystem.MACOS,  "Bob should get macOS"
print("Test 1 passed ✅")

# Test 2: Minimises total sadness (not just individual)
people2 = [
    Person("Carol", 22, tuple([OperatingSystem.ARCH, OperatingSystem.UBUNTU])),
    Person("Dave",  28, tuple([OperatingSystem.ARCH, OperatingSystem.MACOS])),
]

laptops2 = [
    Laptop(3, "Lenovo", "ThinkPad", 13.0, OperatingSystem.ARCH),
    Laptop(4, "Dell",   "XPS",      15.0, OperatingSystem.UBUNTU),
]
result2 = allocate_laptops(people2, laptops2)
# Carol gets ARCH (sadness 0), Dave gets UBUNTU (sadness 100 — not in prefs)
# vs Carol gets UBUNTU (sadness 1), Dave gets ARCH (sadness 0) — total sadness 1
# Optimal is Carol→UBUNTU, Dave→ARCH (total sadness 1)
assert result2[people2[1]].operating_system == OperatingSystem.ARCH, "Dave should get Arch"
print("Test 2 passed ✅")

print("All tests passed! 🎉")