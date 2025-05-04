import unittest
from logic import conjunction, disjunction, negation, implication, biconditional

class TestLogicalOperations(unittest.TestCase):
    # Normal cases
    def test_conjunction(self):
        self.assertTrue(conjunction(True, True))
        self.assertFalse(conjunction(True, False))

    def test_disjunction(self):
        self.assertTrue(disjunction(False, True))
        self.assertFalse(disjunction(False, False))

    def test_implication(self):
        self.assertTrue(implication(False, False))
        self.assertTrue(implication(False, True))
        self.assertTrue(implication(True, True))
        self.assertFalse(implication(True, False))

    # Edge cases
    def test_negation(self):
        self.assertTrue(negation(False))
        self.assertFalse(negation(True))

    def test_biconditional(self):
        self.assertTrue(biconditional(True, True))
        self.assertTrue(biconditional(False, False))
        self.assertFalse(biconditional(True, False))

    def test_all_false_case(self):
        # A = False, B = False
        a, b = False, False
        self.assertFalse(conjunction(a, b))
        self.assertFalse(disjunction(a, b))
        self.assertTrue(negation(a))
        self.assertTrue(negation(b))
        self.assertTrue(implication(a, b))
        self.assertTrue(biconditional(a, b))

if __name__ == '__main__':
    unittest.main()
