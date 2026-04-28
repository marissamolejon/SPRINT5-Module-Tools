"""
Unit tests for exercise_enums.py
Tests: parse_operating_system, parse_age, count_laptops_for_os
(main() is not tested as it requires interactive input)
"""
 
import sys
import unittest
from enums import (
    OperatingSystem,
    Laptop,
    parse_operating_system,
    parse_age,
    count_laptops_for_os,
    LIBRARY_LAPTOPS,
)
 
 
class TestParseOperatingSystem(unittest.TestCase):
 
    def test_parses_ubuntu_exact(self):
        self.assertEqual(parse_operating_system("Ubuntu"), OperatingSystem.UBUNTU)
 
    def test_parses_arch_linux_exact(self):
        self.assertEqual(parse_operating_system("Arch Linux"), OperatingSystem.ARCH)
 
    def test_parses_macos_exact(self):
        self.assertEqual(parse_operating_system("macOS"), OperatingSystem.MACOS)
 
    def test_case_insensitive_ubuntu(self):
        self.assertEqual(parse_operating_system("ubuntu"), OperatingSystem.UBUNTU)
 
    def test_case_insensitive_arch(self):
        self.assertEqual(parse_operating_system("ARCH LINUX"), OperatingSystem.ARCH)
 
    def test_strips_whitespace(self):
        self.assertEqual(parse_operating_system("  Ubuntu  "), OperatingSystem.UBUNTU)
 
    def test_invalid_os_exits_with_nonzero_code(self):
        with self.assertRaises(SystemExit) as cm:
            parse_operating_system("Windows")
        self.assertNotEqual(cm.exception.code, 0)
 
    def test_empty_string_exits(self):
        with self.assertRaises(SystemExit):
            parse_operating_system("")
 
 
class TestParseAge(unittest.TestCase):
 
    def test_valid_age(self):
        self.assertEqual(parse_age("25"), 25)
 
    def test_zero_is_valid(self):
        self.assertEqual(parse_age("0"), 0)
 
    def test_strips_whitespace(self):
        self.assertEqual(parse_age("  30  "), 30)
 
    def test_negative_age_exits(self):
        with self.assertRaises(SystemExit) as cm:
            parse_age("-1")
        self.assertNotEqual(cm.exception.code, 0)
 
    def test_non_numeric_exits(self):
        with self.assertRaises(SystemExit):
            parse_age("twenty")
 
    def test_float_string_exits(self):
        with self.assertRaises(SystemExit):
            parse_age("25.5")
 
    def test_empty_string_exits(self):
        with self.assertRaises(SystemExit):
            parse_age("")
 
 
class TestCountLaptopsForOs(unittest.TestCase):
 
    def setUp(self):
        self.laptops = [
            Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
            Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
            Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
            Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
        ]
 
    def test_counts_ubuntu_laptops(self):
        self.assertEqual(count_laptops_for_os(self.laptops, OperatingSystem.UBUNTU), 2)
 
    def test_counts_arch_laptops(self):
        self.assertEqual(count_laptops_for_os(self.laptops, OperatingSystem.ARCH), 1)
 
    def test_counts_macos_laptops(self):
        self.assertEqual(count_laptops_for_os(self.laptops, OperatingSystem.MACOS), 1)
 
    def test_empty_list_returns_zero(self):
        self.assertEqual(count_laptops_for_os([], OperatingSystem.UBUNTU), 0)
 
    def test_library_laptops_ubuntu_count(self):
        # LIBRARY_LAPTOPS has 2 Ubuntu laptops (id 2 and 3)
        self.assertEqual(count_laptops_for_os(LIBRARY_LAPTOPS, OperatingSystem.UBUNTU), 2)
 
    def test_library_laptops_macos_count(self):
        # LIBRARY_LAPTOPS has 2 macOS laptops (id 4 and 5)
        self.assertEqual(count_laptops_for_os(LIBRARY_LAPTOPS, OperatingSystem.MACOS), 2)
 
 
if __name__ == "__main__":
    unittest.main()
 