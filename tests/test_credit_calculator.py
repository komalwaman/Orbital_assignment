import unittest
from app.credit_calculator import calculate_credits

class TestCreditCalculator(unittest.TestCase):
    def test_simple_message_exact(self):
        text = "What is the rent?"
        expected_credits = 1.05
        actual_credits = calculate_credits(text)
        self.assertAlmostEqual(actual_credits, expected_credits, places=2)

    def test_long_text_exact(self):
        text = "a" * 101
        expected_credits = 38.5
        actual_credits = calculate_credits(text)
        self.assertAlmostEqual(actual_credits, expected_credits, places=2)

    def test_palindrome_exact(self):
        text = "A man, a plan, a canal: Panama"
        expected_credits = 8.8
        actual_credits = calculate_credits(text)
        self.assertTrue(calculate_credits(text) > 1.0)
        self.assertAlmostEqual(actual_credits, expected_credits, places=2)

    def test_unique_words_bonus_exact(self):
        text = "Red blue green yellow black white purple"
        expected_credits = 3.2
        actual_credits = calculate_credits(text)
        self.assertLess(expected_credits, 10.0)
        self.assertAlmostEqual(actual_credits, expected_credits, places=2)

if __name__ == "__main__":
    unittest.main()