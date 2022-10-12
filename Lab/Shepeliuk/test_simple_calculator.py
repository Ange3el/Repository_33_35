import unittest
class SimpleCalculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b,):
        return a / b


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator =  SimpleCalculator()

    def tearDown(self):
        print("\ntear Down executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(10,5)
        self.assertEqual(result, 15)

    def test_subtraction_two_integers(self):
        result = self.calculator.sub(10,5)
        self.assertEqual(result, 5)

    def test_multiplication_two_integers(self):
        result = self.calculator.mult(10,5)
        self.assertEqual(result, 50)

    def test_divide_two_integers(self):
        result = self.calculator.div(10,5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()

