import unittest
from probability_experiment import coin_toss, die_roll, compound_coin_toss, drawing_card

class TestProbabilityExperiment(unittest.TestCase):
    #coin toss
    def test_toss_10_times(self):
        result = coin_toss(10)
        total = result["Heads"] + result["Tails"]
        self.assertEqual(total, 10)
    
    def test_result_contains_heads_and_tails(self):
        result = coin_toss(50)
        # It is probabilistic, so just check keys exist
        self.assertTrue("Heads" in result or "Tails" in result)


    def test_single_toss(self):
        result = coin_toss(1)
        total = result["Heads"] + result["Tails"]
        self.assertEqual(total, 1)
        self.assertIn(list(result.keys())[0], ["Heads", "Tails"])

    # die_roll
    def test_roll_10_times(self):
        result = die_roll(10)
        total = sum(result.values())
        self.assertEqual(total, 10)

    def test_single_roll(self):
        result = die_roll(1)
        self.assertEqual(sum(result.values()), 1)
        self.assertIn(list(result.keys())[0], [1, 2, 3, 4, 5, 6])


    #drawing card
    def test_draw_10_cards(self):
        red, black = drawing_card(10)
        self.assertEqual(red + black, 10)

    def test_draw_0_cards(self):
        red, black = drawing_card(0)
        self.assertEqual((red, black), (0, 0))

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            drawing_card(-5)

    #compound coin toss
    # Normal test cases
    def test_toss_10_times(self):
        result = compound_coin_toss(10)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertTrue(0 <= result[0] <= 10)  # both_heads
        self.assertTrue(0 <= result[1] <= 10)  # at_least_one_heads

    def test_zero_tosses(self):
        result = compound_coin_toss(0)
        self.assertEqual(result, [])   
    
if __name__ == '__main__':
    unittest.main()