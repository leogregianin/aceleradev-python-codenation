from main import ManagerDates
import unittest
import datetime

class ManagerDatesTests(unittest.TestCase):
    def test_date_is_valid(self):
        date = '01/02/2019'
        formatting_dates = ManagerDates()
        self.assertEqual(
            formatting_dates.date_is_valid(date),
            True
        )

    def test_date_weekday(self):
        date = datetime.datetime(2019,3,24)
        formatting_dates = ManagerDates()
        self.assertEqual(
            formatting_dates.date_weekday(date),
            "Sunday"
        )

    def test_convert_string_to_date(self):
        date = "19/01/2018"
        formatting_dates = ManagerDates()
        self.assertEqual(
            formatting_dates.convert_string_to_date(date),
            datetime.datetime(2018,1,19)
        )

    def test_get_all_dates(self):
        formatting_dates = ManagerDates()
        self.assertEqual(
            len(formatting_dates.get_all_dates("02", "2019")),
            28
        )

    def test_count_days_mounth(self):
        formatting_dates = ManagerDates()
        self.assertEqual(
            formatting_dates.count_days_mounth("03", "2019"),
            21
        )

    def test_get_first_monday(self):
        formatting_dates = ManagerDates()
        self.assertEqual(
            formatting_dates.get_first_monday("2019"),
            "06/05/2019"
        )

if __name__ == '__main__':
    unittest.main()
