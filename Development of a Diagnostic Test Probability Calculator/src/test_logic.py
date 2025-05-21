import unittest
from logic import calculate_probability_disease_given_positive, calculate_probability_disease_given_negative

class TestLogic(unittest.TestCase):
    
    # Normal Case
    def test_calculate_positive_normal(self):
        probability_disease_given_positive = calculate_probability_disease_given_positive(0.1, 0.8, 0.9)
        self.assertEqual(probability_disease_given_positive,0.4706)
    
    def test_calculate_negative_normal(self):
        probability_disease_given_negative = calculate_probability_disease_given_negative(0.1, 0.8, 0.9)
        self.assertEqual(probability_disease_given_negative, 0.0241)

    def test_both_at_same_time(self):
        probability_disease_given_positive = calculate_probability_disease_given_positive(0.1, 0.8, 0.9)
        probability_disease_given_negative = calculate_probability_disease_given_negative(0.1, 0.8, 0.9)
        self.assertEqual(probability_disease_given_positive, 0.4706)
        self.assertEqual(probability_disease_given_negative, 0.0241)

    # Edge Case
    def test_calculate_positive_zero(self):
        probability_disease_given_positive = calculate_probability_disease_given_positive(0, 0, 0)
        self.assertEqual(probability_disease_given_positive, 0)
    
    def test_calculate_negative_zero(self):
        probability_disease_given_negative = calculate_probability_disease_given_negative(0, 0, 0)
        self.assertEqual(probability_disease_given_negative, 0)

    def test_calculate_negative_negative(self):
        with self.assertRaises(ValueError):
            calculate_probability_disease_given_negative(-1, -1, -1)

if __name__ == "__main__":
    unittest.main()