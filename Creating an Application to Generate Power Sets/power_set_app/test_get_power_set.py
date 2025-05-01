import unittest
from get_power_set import get_power_set

class TestPowerSet(unittest.TestCase):

    # Normal test cases
    def test_three_elements(self):
        input_set = {'a', 'b', 'c'}
        result = get_power_set(input_set)
        self.assertEqual(len(result), 8)

    def test_two_elements(self):
        input_set = {'x', 'y'}
        result = get_power_set(input_set)
        self.assertEqual(len(result), 4)

    def test_numeric_elements(self):
        input_set = {1, 2}
        result = get_power_set(input_set)
        expected_subsets = [set(), {1}, {2}, {1, 2}]
        for subset in expected_subsets:
            self.assertIn(subset, result)

    # Edge test cases
    def test_empty_set(self):
        input_set = set()
        result = get_power_set(input_set)
        self.assertEqual(result, [set()])

    def test_single_element(self):
        input_set = {'z'}
        result = get_power_set(input_set)
        self.assertEqual(result, [set(), {'z'}])

    def test_duplicates_removed(self):
        input_list = ['a', 'a', 'b']
        input_set = set(input_list)
        result = get_power_set(input_set)
        self.assertEqual(len(result), 4)

if __name__ == "__main__":
    unittest.main()