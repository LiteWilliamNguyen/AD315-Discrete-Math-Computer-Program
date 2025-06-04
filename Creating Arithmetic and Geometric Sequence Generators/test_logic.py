import unittest
import logic_sequence_generator

class TestLogicSequenceGenerator(unittest.TestCase):

    # Test the generate_arithmetic_sequence function
    def test_generate_arithmetic_sequence(self):
        sequence = logic_sequence_generator.generate_arithmetic_sequence(1, 2, 5)
        self.assertEqual(sequence, [1, 3, 5, 7, 9])

    # Test the generate_geometric_sequence function
    def test_generate_geometric_sequence(self):
        sequence = logic_sequence_generator.generate_geometric_sequence(1, 2, 3)
        self.assertEqual(sequence, [1, 2, 4])
    
    # Test the calculate_sum function
    def test_calculate_sum(self):
        sequence = [1, 2, 3, 4, 5]
        self.assertEqual(logic_sequence_generator.calculate_sum(sequence), 15)

    # Edge Case
    # Test the generate_arithmetic_sequence function with zero terms
    def test_generate_arithmetic_sequence_zero_terms(self):
        sequence = logic_sequence_generator.generate_arithmetic_sequence(1, 2, 0)
        self.assertEqual(sequence, None)

    # Test the generate_geometric_sequence function with zero terms
    def test_generate_geometric_sequence_zero_terms(self):
        sequence = logic_sequence_generator.generate_geometric_sequence(1, 2, 0)
        self.assertEqual(sequence, None)

    # Test the calculate_sum function with empty sequence
    def test_calculate_sum_empty_sequence(self):
        sequence = []
        self.assertEqual(logic_sequence_generator.calculate_sum(sequence), 0)

if __name__ == '__main__':
    unittest.main()