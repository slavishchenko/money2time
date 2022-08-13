import unittest

from user import User
from money2time import Calculator


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user_1 = User(50000)
        self.user_2 = User(100, 5, 10)
        self.user_3 = User(50000, 0, 0)

        self.calc_1 = Calculator(self.user_1)
        self.calc_2 = Calculator(self.user_2)
        self.calc_3 = Calculator(self.user_3)


    def test_daily_wage(self):
        self.assertEqual(self.user_1.daily_wage, 2273)
        self.assertEqual(self.user_2.daily_wage, 10)
        self.assertEqual(self.user_3.daily_wage, 2273)


    def test_hourly_wage(self):
        self.assertEqual(self.user_1.hourly_wage, 284)
        self.assertEqual(self.user_2.hourly_wage, 2)
        self.assertEqual(self.user_3.hourly_wage, 284)


    def test_calculator(self):
        hours, days = self.calc_1.money_to_time(25000).values()
        self.assertEqual(hours, 88)
        self.assertEqual(days, 11)

        hours, days = self.calc_2.money_to_time(100).values()
        self.assertEqual(hours, 50)
        self.assertEqual(days, 10)

        hours, days = self.calc_3.money_to_time(25000).values()
        self.assertEqual(hours, 88)
        self.assertEqual(days, 11)    


if __name__ == '__main__':
    unittest.main()