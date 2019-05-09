from main import calc_angle_mbc
import unittest


class CalcAngleTests(unittest.TestCase):
    def test_angle_one(self):
        self.assertEqual(calc_angle_mbc(10, 10), 45)

    def test_angle_two(self):
        self.assertEqual(calc_angle_mbc(1, 10), 6)

    def test_angle_three(self):
        self.assertEqual(calc_angle_mbc(100, 1), 89)



if __name__ == '__main__':
    unittest.main()
