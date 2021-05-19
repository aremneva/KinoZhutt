import unittest, checks

class Assert_correct_date(unittest.TestCase):
    def test_correctDates(self):
        correct_dates_list = ['2021-01-01','1999-03-17','2020-02-29','2002-09-19']
        for date in correct_dates_list:
            self.assertTrue(checks.input_check.written_date_correct(date))

if __name__ == '__main__':
    unittest.main()


