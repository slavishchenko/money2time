import unittest

from main import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator(50000)

    def test_daily_wage(self):
        self.assertEqual(self.calc.daily_wage, 2273)

    def test_hourly_wage(self):
        self.assertEqual(self.calc.hourly_wage, 284)

    def test_money_to_time(self):
        hours, days = self.calc.money_to_time(25000).values()
        self.assertEqual(hours, 88)
        self.assertEqual(days, 11)

if __name__ == '__main__':
    unittest.main()