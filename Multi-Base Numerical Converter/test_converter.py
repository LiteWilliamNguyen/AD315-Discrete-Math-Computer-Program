import unittest
from main import multi_base_numerical_converter  # Import the function from your main program


class TestBaseConverter(unittest.TestCase):
    def test_normal_cases(self):
        """Test normal cases for base conversion."""
        binary, octal, hexadecimal = multi_base_numerical_converter(255)
        self.assertEqual(binary, "11111111", "Binary conversion failed for 255")
        self.assertEqual(octal, "377", "Octal conversion failed for 255")
        self.assertEqual(hexadecimal, "FF", "Hexadecimal conversion failed for 255")


    """test large number"""
    def test_large_number(self):
        """Test large number for base conversion."""
        binary, octal, hexadecimal = multi_base_numerical_converter(2500)
        self.assertEqual(binary, "100111000100", "Binary conversion failed for 2500")
        self.assertEqual(octal, "4704", "Octal conversion failed for 2500")
        self.assertEqual(hexadecimal, "9C4", "Hexadecimal conversion failed for 2500")

    """test zero number"""
    def test_zero_number(self):
        """Test zero number for base conversion."""
        binary, octal, hexadecimal = multi_base_numerical_converter(0)
        self.assertEqual(binary, "0", "Binary conversion failed for 0")
        self.assertEqual(octal, "0", "Octal conversion failed for 0")
        self.assertEqual(hexadecimal, "0", "Hexadecimal conversion failed for 0")
    
    """test power of 2 number"""
    def test_power_of_2_number(self):
        """Test power of 2 number for base conversion."""
        binary, octal, hexadecimal = multi_base_numerical_converter(16)
        self.assertEqual(binary, "10000", "Binary conversion failed for 16")
        self.assertEqual(octal, "20", "Octal conversion failed for 16")
        self.assertEqual(hexadecimal, "10", "Hexadecimal conversion failed for 16")

    """Test a number that includes all digits of hexadecimal"""
    def test_hexadecimal_number(self):
        """Test hexadecimal number for base conversion."""
        binary, octal, hexadecimal = multi_base_numerical_converter(0xFF)
        self.assertEqual(binary, "11111111", "Binary conversion failed for 0xFF")
        self.assertEqual(octal, "377", "Octal conversion failed for 0xFF")
        self.assertEqual(hexadecimal, "FF", "Hexadecimal conversion failed for 0xFF")
    
    """Test a number that includes all digits of octal"""
    def test_octal_number(self):
        """Test octal number for base conversion."""
        binary, octal, hexadecimal = multi_base_numerical_converter(0o377)
        self.assertEqual(binary, "11111111", "Binary conversion failed for 0o377")
        self.assertEqual(octal, "377", "Octal conversion failed for 0o377")
        self.assertEqual(hexadecimal, "FF", "Hexadecimal conversion failed for 0o377")

if __name__ == "__main__":
    unittest.main()