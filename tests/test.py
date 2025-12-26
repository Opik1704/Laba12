import unittest

from src.main import *

class TestCalculator(unittest.TestCase):
    """Тесты для калькулятора обратной польской нотации"""
    def test_operations(self):
        """Тесты обычных"""
        self.assertEqual(calculate_rpn("3 4 +"), 7)
        self.assertEqual(calculate_rpn("10 5 -"), 5)
        self.assertEqual(calculate_rpn("4 5 *"), 20)
        self.assertEqual(calculate_rpn("20 4 /"), 5)
        self.assertEqual(calculate_rpn("2 3 ^"), 8)

    def test_complex_expressions(self):
        """Тесты сложных выражений"""
        self.assertEqual(calculate_rpn("3 4 2 * +"), 11)
        self.assertEqual(calculate_rpn("5 4 28 + *"), 160)

    def test_unar(self):
        """Тесты унарных операторов"""
        self.assertEqual(calculate_rpn("-5 3 +"), -2)
        self.assertEqual(calculate_rpn("+5 3 +"), 8)
        self.assertEqual(calculate_rpn("+3 -4 *"), -12)
        self.assertEqual(calculate_rpn("- -5 2 +"), 7)
        self.assertEqual(calculate_rpn("10 -3 /"), -10 / 3)

    def test_otric_numbers(self):
        """Тесты отрицательных чисел"""
        self.assertEqual(calculate_rpn("-5 -3 +"), -8)
        self.assertEqual(calculate_rpn("-5 -3 *"), 15)

    def test_error(self):
        """Тесты ошибочных случаев"""
        with self.assertRaises(ValueError):
            calculate_rpn("5 0 /")

        with self.assertRaises(ValueError):
            calculate_rpn("3 +")

        with self.assertRaises(ValueError):
            calculate_rpn("3 4 $")

        with self.assertRaises(ValueError):
            calculate_rpn("3 4 + 5")

        with self.assertRaises(ValueError):
            calculate_rpn("3 4 5")

if __name__ == '__main__':
    unittest.main()