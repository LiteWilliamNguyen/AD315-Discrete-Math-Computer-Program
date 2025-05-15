from logic_dice import roll_dice, simulate_rolling_dice, calculate_probability
import unittest


class TestDiceFunctions(unittest.TestCase):

    # Normal cases
    def test_roll_dice_once_normal(self):
        result = roll_dice(2, 6)
        self.assertTrue(2 <= result <= 12)

    def test_simulate_rolls_length(self):
        results = simulate_rolling_dice(2, 6, 10)
        self.assertEqual(len(results), 10)

    def test_probability_distribution_sum(self):
        dist = calculate_probability(2, 6, 10000)
        total_prob = sum(dist.values())
        self.assertAlmostEqual(total_prob, 1.0, places=2)

    # Edge cases
    def test_single_die_single_side(self):
        result = roll_dice(1, 1)
        self.assertEqual(result, 1)

    def test_probability_distribution_minimum_input(self):
        dist = calculate_probability(1, 1, 1)
        self.assertEqual(dist, {1: 1.0})

    def test_large_number_of_simulations(self):
        dist = calculate_probability(1, 6, 100000)
        self.assertAlmostEqual(sum(dist.values()), 1.0, places=2)

if __name__ == '__main__':
    unittest.main()